#!/usr/bin/python3
"""Builds a release's social media video from the raw clips record.sh made:
1920x1080, 30 fps, H.264 with a silent AAC track. Every frame is drawn
with PIL (title cards, captions, pans over the docs screenshots, the
recordings, theme backgrounds) and piped to ffmpeg.

Each release edits this for its own New and Improvements items: VERSION,
the scenes between scene_new and scene_fixes, FIXES and UPDATED, and the
segment lists cut to its recordings. This is 4.16.0's, and git history
keeps each release's from then on.

Usage: build.py <work dir> <output.mp4>
       build.py <work dir> <prefix> --preview t1,t2,...   (PNGs at those times)"""
import math
import os
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

VERSION = "4.16"  # as the title cards show it
W, H, FPS = 1920, 1080, 30
# This repo's own screenshots, for the opening pans.
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "images")
THEMES = "/usr/share/ohmydebn-themes"
BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
MONO = "/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf"
if not os.path.exists(MONO):
    MONO = BOLD

VOID = (30, 30, 46)
TEXT = (205, 214, 244)
CYAN = (148, 226, 213)
EMERALD = (166, 227, 161)
VIOLET = (137, 180, 250)
DIM = (140, 146, 170)

_fonts = {}


def font(path, size):
    key = (path, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def fade(t, dur, fin=0.4, fout=0.4):
    """Opacity of something shown from 0 to dur, fading in and out."""
    return clamp(min(t / fin if fin else 1, (dur - t) / fout if fout else 1))


# ---------- drawing helpers ----------

def logo(size):
    """The OhMyDebn grin, drawn from config/icons/ohmydebn.svg's shapes."""
    s = size * 4
    u = s / 16
    grad = Image.new("RGB", (s, s))
    stops = [(0, (0x48, 0x8b, 0xff)), (0.5, (0xb2, 0xe7, 0xde)), (1, (0x57, 0xea, 0xf7))]
    gpx = grad.load()
    for y in range(s):
        for x in range(s):
            p = clamp(((x / u - 1) + (y / u - 1)) / 28)
            (a0, c0), (a1, c1) = (stops[0], stops[1]) if p < 0.5 else (stops[1], stops[2])
            k = (p - a0) / (a1 - a0)
            gpx[x, y] = tuple(int(c0[i] + (c1[i] - c0[i]) * k) for i in range(3))
    mask = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([1 * u, 1 * u, 15 * u, 15 * u], fill=255)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    out.paste(grad, (0, 0), mask)
    d = ImageDraw.Draw(out)
    for cx in (5.6, 10.4):
        d.ellipse([(cx - 1.2) * u, 4.5 * u, (cx + 1.2) * u, 6.9 * u], fill=VOID)
    d.pieslice([4.2 * u, 4.6 * u, 11.8 * u, 12.2 * u], 0, 180, fill=VOID)
    return out.resize((size, size), Image.LANCZOS)


def backdrop():
    """Dark background with a soft glow, for the title cards."""
    bg = Image.new("RGB", (W, H), VOID)
    glow = Image.new("RGB", (W // 8, H // 8), VOID)
    g = ImageDraw.Draw(glow)
    g.ellipse([W // 8 * 0.2, H // 8 * -0.1, W // 8 * 0.8, H // 8 * 0.9], fill=(44, 58, 86))
    glow = glow.filter(ImageFilter.GaussianBlur(18)).resize((W, H), Image.BICUBIC)
    return Image.blend(bg, glow, 0.9)


BACKDROP = None


def text_center(img, y, text, fnt, fill, alpha=1.0, dy=0):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    w = d.textlength(text, font=fnt)
    d.text(((W - w) / 2, y + dy), text, font=fnt, fill=fill + (int(255 * alpha),))
    img.alpha_composite(layer)


def keycap_width(d, label, fnt):
    return d.textlength(label, font=fnt) + 44


def draw_keycaps(d, x, y, keys, fnt, alpha):
    """Keys like ["Super", "`"] drawn as caps joined by '+'. Returns width."""
    a = int(255 * alpha)
    cx = x
    plus = font(BOLD, 34)
    for i, k in enumerate(keys):
        kw = keycap_width(d, k, fnt)
        d.rounded_rectangle([cx, y + 4, cx + kw, y + 62], 12, fill=(17, 17, 27, a))
        d.rounded_rectangle([cx, y, cx + kw, y + 56], 12, fill=(69, 71, 90, a), outline=(110, 115, 141, a), width=2)
        d.text((cx + 22, y + 6), k, font=fnt, fill=TEXT + (a,))
        cx += kw
        if i < len(keys) - 1:
            d.text((cx + 14, y + 6), "+", font=plus, fill=DIM + (a,))
            cx += 50
    return cx - x


def caption(img, t, dur, title, sub=None, keys=None, accent=CYAN):
    """A lower-third card, sliding up as it fades in."""
    a = fade(t, dur, 0.35, 0.3)
    if a <= 0:
        return
    dy = int((1 - ease_out(t / 0.45)) * 24)
    tf, sf, kf = font(BOLD, 54), font(REG, 34), font(MONO, 34)
    probe = ImageDraw.Draw(img)
    tw = probe.textlength(title, font=tf)
    kw = 0
    if keys:
        kw = sum(keycap_width(probe, k, kf) for k in keys) + 50 * (len(keys) - 1) + 30
    sw = probe.textlength(sub, font=sf) if sub else 0
    bw = int(max(tw + kw, sw) + 96)
    bh = 150 if sub else 104
    x0 = (W - bw) // 2
    y0 = H - bh - 70 + dy
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], 26, fill=(24, 24, 37, int(222 * a)),
                        outline=(255, 255, 255, int(40 * a)), width=2)
    d.rounded_rectangle([x0 + 22, y0 + 26, x0 + 28, y0 + bh - 26], 3, fill=accent + (int(255 * a),))
    tx = x0 + 48
    d.text((tx, y0 + 18), title, font=tf, fill=TEXT + (int(255 * a),))
    if keys:
        draw_keycaps(d, tx + tw + 30, y0 + 22, keys, kf, a)
    if sub:
        d.text((tx, y0 + 90), sub, font=sf, fill=(186, 194, 222, int(255 * a)))
    img.alpha_composite(layer)


# ---------- sources ----------

_stills = {}


def still(name, width=2300):
    if name not in _stills:
        im = Image.open(os.path.join(IMG, name)).convert("RGB")
        h = round(im.height * width / im.width)
        _stills[name] = im.resize((width, h), Image.LANCZOS)
    return _stills[name]


def kenburns(name, p, z0=1.0, z1=1.08, fx=0.5, fy=0.5):
    """A slow zoom on a screenshot; p goes 0..1 over the shot."""
    im = still(name)
    z = z0 + (z1 - z0) * ease(p)
    # Fill 1920x1080, then zoom in by z around (fx, fy).
    base = max(W / im.width, H / im.height)
    cw, ch = W / (base * z), H / (base * z)
    cx = fx * im.width
    cy = fy * im.height
    x = clamp(cx - cw / 2, 0, im.width - cw)
    y = clamp(cy - ch / 2, 0, im.height - ch)
    return im.resize((W, H), Image.BILINEAR, box=(x, y, x + cw, y + ch)).convert("RGBA")


class Clip:
    """Frames of a recording, as segments of (start, end, speed) in source
    seconds, scaled to fill 1920x1080 (cropping the sides), in order."""

    def __init__(self, path, segments):
        parts, n = [], len(segments)
        for i, (a, b, sp) in enumerate(segments):
            parts.append(f"[0:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp}[s{i}]")
        chain = ";".join(parts) + ";" + "".join(f"[s{i}]" for i in range(n)) + \
            f"concat=n={n}:v=1:a=0,fps={FPS},scale=-2:{H}:flags=lanczos,crop={W}:{H}[out]"
        self.proc = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-i", path, "-filter_complex", chain, "-map", "[out]",
             "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        self.index = -1
        self.frame = None
        self.length = sum((b - a) / sp for a, b, sp in segments)

    def at(self, t):
        want = int(t * FPS)
        while self.index < want:
            raw = self.proc.stdout.read(W * H * 3)
            if len(raw) < W * H * 3:
                break
            self.frame = Image.frombytes("RGB", (W, H), raw)
            self.index += 1
        return self.frame.convert("RGBA")


# ---------- scenes: each takes local time t and returns an RGBA frame ----------

def scene_intro(t, dur):
    img = BACKDROP.copy().convert("RGBA")
    s = 0.6 + 0.4 * ease_out(t / 0.9)
    size = int(300 * s)
    lg = LOGO.resize((size, size), Image.LANCZOS)
    la = clamp(t / 0.5)
    if la < 1:
        lg.putalpha(lg.getchannel("A").point(lambda v: int(v * la)))
    img.alpha_composite(lg, ((W - size) // 2, 250 + (300 - size) // 2))
    text_center(img, 600, "OhMyDebn", font(BOLD, 128), TEXT, clamp((t - 0.5) / 0.5), int((1 - ease_out((t - 0.5) / 0.6)) * 30))
    text_center(img, 780, "Linux, refined.", font(REG, 60), CYAN, clamp((t - 1.1) / 0.5), int((1 - ease_out((t - 1.1) / 0.6)) * 30))
    return img


def scene_what(t, dur):
    half = dur / 2
    a = kenburns("ohmydebn.png", t / dur, 1.0, 1.06, 0.45, 0.45)
    b = kenburns("ohmydebn-tiling.png", clamp((t - half + 0.5) / (half + 0.5)), 1.04, 1.0, 0.45, 0.5)
    k = ease((t - half + 0.4) / 0.8)
    img = Image.blend(a, b, k) if k > 0 else a
    if t < half:
        caption(img, t, half, "A debonair Linux desktop for power users",
                "Cinnamon on Debian, Linux Mint, Ubuntu and more", accent=CYAN)
    else:
        caption(img, t - half, half, "Themes, window tiling, hotkeys and AI",
                "Everything one hotkey away", accent=VIOLET)
    return img


def scene_new(t, dur):
    img = BACKDROP.copy().convert("RGBA")
    text_center(img, 330, "What's new in", font(REG, 64), CYAN, clamp(t / 0.4), int((1 - ease_out(t / 0.5)) * 24))
    text_center(img, 420, VERSION, font(BOLD, 260), TEXT, clamp((t - 0.25) / 0.4), int((1 - ease_out((t - 0.25) / 0.5)) * 36))
    return img


MENU_SEGS = [(0.3, 6.3, 1.0)]
# The three unlock dialogs, without the blank screen between them: the
# first keeps the locked, blank screen just before it opens.
LOCK_SEGS = [(2.0, 6.6, 1.0), (7.85, 11.5, 1.0), (13.1, 17.6, 1.0)]
THEME_AT = [0.0, 4.6, 4.6 + 3.65]
THEME_NAMES = ["OhMyDebn", "Retro 82", "Jade Horse"]


def zoom(img, z, fx=0.5, fy=0.5):
    """Crops img around (fx, fy) by z and scales it back to full size."""
    if z <= 1.001:
        return img
    cw, ch = W / z, H / z
    x = clamp(fx * W - cw / 2, 0, W - cw)
    y = clamp(fy * H - ch / 2, 0, H - ch)
    return img.resize((W, H), Image.BICUBIC, box=(x, y, x + cw, y + ch))


def scene_menu(t, dur):
    # The menu is small on a 2540-wide screen: closer, around it.
    z = 1.6 + 0.5 * ease(t / 1.6)
    img = zoom(MENU.at(t), z, 0.5, 0.27)
    caption(img, t, dur, "New: XScreenSaver lock screen", "OhMyDebn menu > Appearance > Lock Screen",
            accent=CYAN)
    return img


def scene_lock(t, dur):
    img = zoom(LOCK.at(t), 2.0, 0.5, 0.5)
    i = max(k for k, at in enumerate(THEME_AT) if t >= at)
    end = THEME_AT[i + 1] if i + 1 < len(THEME_AT) else dur
    if i == 0:
        caption(img, t, end, "A hardened screen locker", "Same lock settings and hotkeys", accent=VIOLET)
    else:
        caption(img, t - THEME_AT[i], end - THEME_AT[i], "Takes your theme's colors", THEME_NAMES[i],
                accent=VIOLET)
    return img


BACKGROUNDS = [("ethereal/backgrounds/3-roadster-starlight.webp", "Ethereal"),
               ("hackerman/backgrounds/2-geometric.webp", "Hackerman")]
_bgs = {}


def background(path, w, h):
    if path not in _bgs:
        im = Image.open(os.path.join(THEMES, path)).convert("RGB")
        s = max(w / im.width, h / im.height)
        im = im.resize((math.ceil(im.width * s), math.ceil(im.height * s)), Image.LANCZOS)
        x, y = (im.width - w) // 2, (im.height - h) // 2
        _bgs[path] = im.crop((x, y, x + w, y + h)).convert("RGBA")
    return _bgs[path]


def scene_backgrounds(t, dur):
    img = BACKDROP.copy().convert("RGBA")
    gap, tw, th = 40, 860, 560
    gx = (W - (2 * tw + gap)) // 2
    gy = 150
    z = 1 + 0.03 * ease(t / dur)
    for i, (path, name) in enumerate(BACKGROUNDS):
        p = ease_out((t - 0.2 * i) / 0.6)
        if p <= 0:
            continue
        sw, sh = int(tw * (0.88 + 0.12 * p) * z), int(th * (0.88 + 0.12 * p) * z)
        im = background(path, tw, th).resize((sw, sh), Image.BILINEAR)
        m = Image.new("L", (sw, sh), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, sw - 1, sh - 1], 18, fill=int(255 * p))
        im.putalpha(m)
        x = gx + i * (tw + gap) + (tw - sw) // 2
        img.alpha_composite(im, (x, gy + (th - sh) // 2))
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        f = font(BOLD, 40)
        nw = d.textlength(name, font=f)
        d.text((gx + i * (tw + gap) + (tw - nw) / 2, 50), name, font=f, fill=TEXT + (int(255 * p),))
        img.alpha_composite(layer)
    caption(img, t - 0.8, dur - 0.8, "Themes updated to Omarchy 4.5's final release",
            "Two backgrounds, touched up", accent=VIOLET)
    return img


FIXES = [
    ("SO-CRATES opens in your browser by itself", CYAN),
    ("Docker and Tailscale fixed on MX Linux and LCOS", EMERALD),
    ("SSH and Remote Desktop servers: firewall notes, and status on Devuan and LCOS", EMERALD),
]
UPDATED = "OpenCode 2.2.6  ·  Codex 0.167  ·  Crush 0.100  ·  Oh My Pi 18.18  ·  SO-CRATES 5.3  ·  fastfetch 2.71"


def scene_fixes(t, dur):
    img = BACKDROP.copy().convert("RGBA")
    text_center(img, 170, "Plus fixes and updates", font(BOLD, 96), TEXT, clamp(t / 0.4),
                int((1 - ease_out(t / 0.5)) * 24))
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = font(REG, 42)
    rows = [d.textlength(line, font=f) for line, _ in FIXES]
    x0 = (W - max(rows) - 48) / 2
    y = 380
    for i, (line, accent) in enumerate(FIXES):
        p = ease_out((t - 0.4 - 0.25 * i) / 0.4)
        if p > 0:
            a = int(255 * p)
            yy = y + int((1 - p) * 16)
            d.rounded_rectangle([x0, yy + 12, x0 + 12, yy + 50], 6, fill=accent + (a,))
            d.text((x0 + 48, yy), line, font=f, fill=TEXT + (a,))
        y += 92
    img.alpha_composite(layer)
    p = clamp((t - 1.4) / 0.5)
    text_center(img, 760, "Updated", font(BOLD, 40), CYAN, p)
    text_center(img, 830, UPDATED, font(REG, 36), DIM, p)
    return img


def scene_outro(t, dur):
    img = BACKDROP.copy().convert("RGBA")
    lg = LOGO.resize((220, 220), Image.LANCZOS)
    la = clamp(t / 0.5)
    lg.putalpha(lg.getchannel("A").point(lambda v: int(v * la)))
    img.alpha_composite(lg, ((W - 220) // 2, 230))
    text_center(img, 500, f"OhMyDebn {VERSION}", font(BOLD, 110), TEXT, clamp((t - 0.3) / 0.5))
    text_center(img, 660, "ohmydebn.org", font(BOLD, 72), CYAN, clamp((t - 0.7) / 0.5))
    text_center(img, 790, "Free and open source", font(REG, 40), DIM, clamp((t - 1.1) / 0.5))
    # Fade to black at the very end.
    k = clamp((t - (dur - 0.6)) / 0.6)
    if k > 0:
        img = Image.blend(img, Image.new("RGBA", (W, H), (0, 0, 0, 255)), k)
    return img


# ---------- timeline ----------

XF = 0.5  # crossfade between scenes

if __name__ == "__main__":
    RAW = os.path.join(sys.argv[1], "raw")
    out = sys.argv[2]
    preview = None
    if len(sys.argv) > 4 and sys.argv[3] == "--preview":
        preview = [float(x) for x in sys.argv[4].split(",")]

    BACKDROP = backdrop()
    LOGO = logo(600)
    MENU = Clip(os.path.join(RAW, "menu.mp4"), MENU_SEGS)
    LOCK = Clip(os.path.join(RAW, "lock.mp4"), LOCK_SEGS)

    scenes = [
        (scene_intro, 3.6),
        (scene_what, 8.4),
        (scene_new, 2.2),
        (scene_menu, MENU.length),
        (scene_lock, LOCK.length),
        (scene_backgrounds, 5.0),
        (scene_fixes, 6.0),
        (scene_outro, 4.6),
    ]
    starts, s = [], 0.0
    for fn, dur in scenes:
        starts.append(s)
        s += dur - XF
    total = s + XF
    frames = int(total * FPS)
    print(f"total {total:.1f}s, {frames} frames", file=sys.stderr)

    def frame_at(t):
        layers = []
        for (fn, dur), st in zip(scenes, starts):
            if st <= t < st + dur:
                layers.append((fn(t - st, dur), st, dur))
        img = layers[0][0]
        if len(layers) > 1:
            _, st, _ = layers[1]
            k = ease((t - st) / XF)
            img = Image.blend(layers[0][0], layers[1][0], k)
        return img.convert("RGB")

    if preview:
        # Clips only read forward, so render in time order up to each preview point.
        want = sorted(preview)
        for i in range(frames):
            t = i / FPS
            needed = [p for p in want if abs(p - t) < 0.5 / FPS]
            # Keep clip readers in step even when not saving.
            img = frame_at(t)
            for p in needed:
                img.save(f"{out}-{p:05.1f}.png")
            if t > want[-1]:
                break
        sys.exit(0)

    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
         "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-shortest",
         "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p", "-profile:v", "high",
         "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for i in range(frames):
        enc.stdin.write(frame_at(i / FPS).tobytes())
        if i % 150 == 0:
            print(f"{i}/{frames}", file=sys.stderr)
    enc.stdin.close()
    enc.wait()
