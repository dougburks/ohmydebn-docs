## Default Theme

The default OhMyDebn theme is based on a modified Catppuccin Mocha theme.

![OhMyDebn screenshot](images/ohmydebn.png)

## Theme Carousel

You can browse and change your theme by going to the OhMyDebn menu and selecting Appearance > Theme (or Appearance > Background), or via [hotkey](hotkeys.md) `Ctrl + Super + T` (or `Ctrl + Super + B`, which opens the same carousel).

![OhMyDebn desktop themes](images/ohmydebn-theme-carousel.png)

This opens a full-screen theme and background browser on whichever monitor your mouse pointer is on:

- `Left` / `Right` browse your installed themes.
- `Up` / `Down` browse the backgrounds for the theme currently shown, including any you've added yourself, when it has more than one. Each theme starts on the background it had when you last used it.
- `Enter` applies the theme and background currently shown.
- `Esc` cancels without changing anything.
- `S` opens a search box; type to jump the carousel straight to the first matching theme.
- `B` opens the [Omarchy Themes](https://bjarneo.github.io/omarchy-themes/) gallery in your browser to browse for more themes. Picking one there installs and applies it automatically. Since applying a theme this way is triggered from a link, OhMyDebn always shows a confirmation dialog first with the theme's source before applying it.
- `C` launches [Aether](https://github.com/omacom/aether) so you can build your own theme. You can also launch Aether directly using the hotkey `Ctrl + Shift + A` and use it to search for wallpaper and extract colors to build a desktop theme.
- `R` removes the theme currently shown (only available for themes you've installed yourself, not the themes bundled with OhMyDebn). Press it again to confirm.

OhMyDebn also automatically picks a matching icon color based on each theme's accent color, so icons stay legible on custom and Aether-generated themes, not just the themes bundled with OhMyDebn.

To add your own backgrounds to a theme, put the images in `~/.config/ohmydebn/backgrounds/<theme>/`, where `<theme>` is the theme's name in lowercase with dashes for spaces, such as `catppuccin-latte`. They show up in the carousel and in background cycling alongside the theme's own backgrounds.

## Theme Intros

When you switch themes, a short, silent intro plays full screen and then fades into the background you chose. It also plays when you log in. Click or press any key to skip it.

Every background has an intro. Most show the background itself at twilight: the light arrives from the top of the picture down, like a sunrise, and then a band of light crosses the scene, the same shimmer that crosses the OhMyDebn grin. That works for any background, including ones you add yourself and themes you install.

Some of the themes included from Omarchy have their own animated intros, made by Omarchy for one of their backgrounds. With that background selected, its intro plays instead: Catppuccin (three of its backgrounds), Catppuccin Latte, Ethereal, Everforest, Flexoki Light, Hackerman, Last Horizon, Lumon, Matte Black, Miasma, Nord, Osaka Jade, Retro 82, Ristretto, Rose Pine, Vantablack and White.

To turn intros off, or back on, go to the OhMyDebn menu and select Appearance > Theme Intros.

Intros don't play:

- when Desktop and window effects are off in System Settings > Effects
- when animations are turned off for accessibility
- on a Raspberry Pi

You can give one of your own backgrounds an animated intro of its own. Put the background in `~/.config/ohmydebn/backgrounds/<theme>/` (see [adding your own backgrounds](#theme-carousel) above), and the video in an `intros` folder inside that, with the same name as the image: `beach.png` plays `intros/beach.webm`. Use WebM (VP9), the format the included intros use, since other formats such as MP4 may not play; convert another format with, for example, `ffmpeg -i beach.mp4 -c:v libvpx-vp9 -an intros/beach.webm`. Any sound in the video is left out. Make the last frame match the image, since the intro fades into it. If the video can't be played, the background gets the usual intro instead.

## Themes Included from Omarchy

Here are some screenshots of the themes included from Omarchy.

### Catppuccin

![OhMyDebn with catppuccin theme](images/ohmydebn-theme-catppuccin.png)

### Catppuccin Latte

![OhMyDebn with catppuccin latte theme](images/ohmydebn-theme-catppuccin-latte.png)

### Ethereal

![OhMyDebn with ethereal theme](images/ohmydebn-theme-ethereal.png)

### Everforest

![OhMyDebn with everforest theme](images/ohmydebn-theme-everforest.png)

### Flexoki Light

![OhMyDebn with flexoki light theme](images/ohmydebn-theme-flexoki-light.png)

### Gruvbox

![OhMyDebn with gruvbox theme](images/ohmydebn-theme-gruvbox.png)

### Hackerman

![OhMyDebn with hackerman theme](images/ohmydebn-theme-hackerman.png)

### Kanagawa

![OhMyDebn with kanagawa theme](images/ohmydebn-theme-kanagawa.png)

### Last Horizon

![OhMyDebn with last horizon theme](images/ohmydebn-theme-last-horizon.png)

### Lumon

![OhMyDebn with lumon theme](images/ohmydebn-theme-lumon.png)

### Lupine

![OhMyDebn with lupine theme](images/ohmydebn-theme-lupine.png)

### Matte Black

![OhMyDebn with matte black theme](images/ohmydebn-theme-matte-black.png)

### Miasma

![OhMyDebn with miasma theme](images/ohmydebn-theme-miasma.png)

### Nord

![OhMyDebn with nord theme](images/ohmydebn-theme-nord.png)

### Osaka Jade

![OhMyDebn with osaka jade theme](images/ohmydebn-theme-osaka-jade.png)

### Retro 82

![OhMyDebn with retro 82 theme](images/ohmydebn-theme-retro-82.png)

### Ristretto

![OhMyDebn with ristretto theme](images/ohmydebn-theme-ristretto.png)

### Rose Pine

![OhMyDebn with rose pine theme](images/ohmydebn-theme-rose-pine.png)

### Solitude

![OhMyDebn with solitude theme](images/ohmydebn-theme-solitude.png)

### Tokyo Night

![OhMyDebn with tokyo night theme](images/ohmydebn-theme-tokyo-night.png)

### Vantablack

![OhMyDebn with vantablack theme](images/ohmydebn-theme-vantablack.png)

### White

![OhMyDebn with white theme](images/ohmydebn-theme-white.png)


