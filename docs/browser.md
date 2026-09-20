## Default Browser

The default browser is [Brave Origin](https://brave.com/), the minimal edition of Brave: the same Chromium engine with Brave's Shields content blocker built in, without the extras of the full Brave Browser.

Brave Origin is the default for new OhMyDebn installs. If you installed OhMyDebn before this change, you keep [Chromium](https://www.chromium.org/Home/) (with the uBlock Origin Lite content blocker) as your default browser - OhMyDebn never changes the default browser of an existing install. Brave Origin is one selection away in the Browsers menu if you'd like to try it. If your distribution already ships Brave Origin (LCOS does), OhMyDebn uses that copy and adds nothing.

Brave Origin is free on Linux, with an optional purchase to support Brave. OhMyDebn pre-accepts the free tier for you, so the first launch opens straight to the browser instead of Brave's buy-or-proceed dialog. You can still buy it later from Brave's settings. The first launch also skips Brave's welcome tour, since OhMyDebn has already made Brave Origin your default browser, leaves its theme following your system light/dark setting, and leaves diagnostic (crash) reports off. Brave's own privacy-preserving analytics stay at Brave's default; both can be changed under Settings > Privacy and security.

To launch the browser, you can open it from the Cinnamon menu, from the Apps menu, or via [hotkey](hotkeys.md) `Super + B`.

## Installing Other Browsers

If you prefer other browsers you can install them by going to OhMyDebn Menu > Apps > Browsers:

- [Brave](https://brave.com/) Browser (extras)
- [Chromium](https://www.chromium.org/Home/) with the uBlock Origin Lite content blocker
- [Firefox](https://www.mozilla.org/firefox/)
- [Google Chrome](https://www.google.com/chrome/)
- [Helium](https://helium.computer/)

After a browser is installed, you'll be asked whether to make it your default browser. The default answer is no, so your current default stays unless you type `y`.

## Changing the Default Browser

To change your default browser at any time, go to OhMyDebn Menu > Apps > Browsers > Set Default and pick one of the installed browsers. This sets everything in one step: the desktop-wide default that `Super + B` and links from other apps use, the `x-www-browser` alternative that command-line tools use, and the PDF viewer.
