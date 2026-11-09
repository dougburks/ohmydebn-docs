## Choosing Your Lock Screen

OhMyDebn uses Cinnamon's own lock screen by default. You can switch to XScreenSaver instead, a hardened screen locker, by opening the OhMyDebn menu and selecting Appearance > Lock Screen. It explains the switch and asks before changing anything, and installs XScreenSaver from your distro if it isn't installed yet. Select Appearance > Lock Screen again to switch back to Cinnamon's.

## Why XScreenSaver

XScreenSaver keeps the keyboard and mouse locked in a small program that does nothing else, and checks your password and draws its window in separate ones. A bug in the password window can't leave your desktop open. Cinnamon's lock screen is one larger program, and has had bugs that let keystrokes through to the locked desktop.

## What Stays the Same

Everything that decides when your screen locks is still Cinnamon's, in its screensaver settings (Appearance > Screensaver):

- Delay before starting the screensaver, for when you step away
- Lock the computer after the screensaver starts, and the Delay before locking: with locking off, your screen just goes black when you step away, and with a delay, coming back before it ends doesn't need your password
- Lock the computer when put to sleep

Turning the screen off when you're inactive is still Cinnamon's too (Turn off the screen when inactive for, in Power Management), and it still happens while the screen is locked.

The [hotkey](hotkeys.md) `Ctrl + Alt + L`, Lock in the Cinnamon menu, and System > Lock in the OhMyDebn menu all lock with XScreenSaver too, and videos still keep your screen from going black while they play.

## What Changes

The lock screen goes black, and pressing a key or moving the mouse shows XScreenSaver's password box. It uses your [desktop theme's](desktop-themes.md) colors and OhMyDebn's font, and shows the date in the same 12 or 24 hour format as your clock. It always shows your username.

XScreenSaver doesn't have Cinnamon's lock screen extras: media controls, notifications, the away message, the on-screen keyboard, and the keyboard layout switcher.

XScreenSaver only works when you log in to Cinnamon's usual X11 session, not a Wayland session, so OhMyDebn won't switch to it there.

If something seems wrong with your lock screen, the [doctor](updating.md#checking-your-installation) checks that XScreenSaver is set up and running.
