#!/bin/bash
# Records the raw clips for a release's social media video; build.py turns
# them into the video. Each release rewrites the clips for its own New and
# Improvements items; this is 4.16.0's, and git history keeps each
# release's from then on. Run it on an OhMyDebn desktop running the new
# release, with a work directory outside the repositories. Whatever the
# clips are, a recording leaves the desktop as it found it: a clip that
# changes a setting puts it back, clips play out on an empty workspace,
# and the real session is never locked.
#
# 4.16.0's clips: the menu clip is
# recorded on an empty workspace of this desktop; nothing in it changes a
# setting (it searches the menu and closes it). The lock screen clip is
# recorded in a nested X display (Xephyr), so this session is never
# locked: XScreenSaver runs there with a scratch HOME and its dialog
# themed by ohmydebn-theme-set-xscreensaver, from three themes' colors in
# turn. Neither is installed here: both run from Debian's packages
# unpacked into <xscreensaver root> (apt-get download xscreensaver
# xscreensaver-data xserver-xephyr libxcb-xv0, then dpkg-deb -x each).
# build.py's LOCK_SEGS and THEME_AT are cut to the sleeps below; change
# them together.
# Usage: record.sh <work dir> <xscreensaver root>   (clips go to <work dir>/raw)
set -uo pipefail
WORK="$1"
XS_ROOT="$2"
OUT="$WORK/raw"
mkdir -p "$OUT"
BIN=/usr/share/ohmydebn/bin
THEMES=/usr/share/ohmydebn-themes
SIZE=$(xdpyinfo | awk '/dimensions:/{print $2}')

rec() { # rec <name> <seconds> [display] [size]: records in the background
  ffmpeg -y -loglevel error -video_size "${4:-$SIZE}" -framerate 30 -f x11grab -draw_mouse 0 -i "${3:-$DISPLAY}" \
    -t "$2" -c:v libx264 -preset ultrafast -crf 14 -pix_fmt yuv420p "$OUT/$1.mp4" &
  REC=$!
}
done_rec() { wait "$REC"; echo "recorded $1 at $(date +%T)"; }

# The menu search, finding Appearance > Lock Screen.
ORIG_DESKTOP=$(xdotool get_desktop)
xdotool set_desktop 1
xdotool mousemove $(( ${SIZE%x*} / 2 )) $(( ${SIZE#*x} / 2 ))
sleep 1
rec menu 9
setsid "$BIN/ohmydebn-menu" </dev/null >/dev/null 2>&1 &
sleep 2; xdotool type --delay 120 "lock screen"; sleep 4.5
xdotool key Escape; sleep 0.4; xdotool key Escape
done_rec menu
xdotool set_desktop "$ORIG_DESKTOP"

# The lock screen, in a nested display.
NEST=:7
XHOME="$WORK/xshome"
rm -rf "$XHOME"
mkdir -p "$XHOME/.config/ohmydebn/current"
# What ohmydebn-lock-screen-set writes to ~/.xscreensaver that shows here:
# a blank screen, locking, and no fade.
printf 'mode:\t\tblank\nlock:\t\tTrue\nfade:\t\tFalse\nunfade:\t\tFalse\ntimeout:\t\t12:00:00\nsplash:\t\tFalse\n' >"$XHOME/.xscreensaver"
export LD_LIBRARY_PATH="$XS_ROOT/usr/lib/x86_64-linux-gnu"
"$XS_ROOT/usr/bin/Xephyr" "$NEST" -screen 1920x1080 -br -ac -noreset >"$WORK/xephyr.log" 2>&1 &
XEPHYR=$!
for _ in $(seq 50); do DISPLAY=$NEST xdpyinfo >/dev/null 2>&1 && break; sleep 0.1; done

nest() { # nest <command...>: runs it against the nested display
  DISPLAY=$NEST HOME="$XHOME" PATH="$XS_ROOT/usr/libexec/xscreensaver:$XS_ROOT/usr/bin:$PATH" "$@"
}
theme() { # theme <name>: that theme's dialog colors, for the next unlock dialog
  nest bash "$BIN/ohmydebn-theme-set-xscreensaver" "$THEMES/$1/colors.toml"
  nest xrdb -merge "$XHOME/.config/ohmydebn/current/xscreensaver.Xresources"
}
dialog() { # opens the unlock dialog and types a made-up password
  nest xdotool mousemove 960 540; nest xdotool key shift; sleep 1.2
  nest xdotool type --delay 140 "ohmydebn"; sleep 2.2
}

theme ohmydebn
echo "XScreenSaver*dateFormat: %a %b %-d, %-I:%M %p" | nest xrdb -merge
nest xscreensaver --no-splash >"$WORK/xscreensaver.log" 2>&1 &
XSS=$!
sleep 2
rec lock 21 "$NEST" 1920x1080
sleep 1
nest xscreensaver-command -lock >/dev/null; sleep 1.5
dialog                                          # OhMyDebn (source 2.5)
nest xdotool key Escape; sleep 0.6; theme retro-82; sleep 0.4
dialog                                          # Retro 82 (source ~8.6)
nest xdotool key Escape; sleep 0.6; theme jade-horse; sleep 0.4
dialog                                          # Jade Horse (source ~14.7)
done_rec lock
kill "$XSS" 2>/dev/null; sleep 0.5; kill "$XEPHYR" 2>/dev/null
echo "desktop back on workspace $(( $(xdotool get_desktop) + 1 ))"
