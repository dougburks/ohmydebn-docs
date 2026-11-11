This page lists what's new in each OhMyDebn release, newest first. To get the latest release, see [Updating](updating.md).

Release notes for 4.8.0 and earlier are on [GitHub](https://github.com/dougburks/ohmydebn/releases).

## 4.17.0

### New

- `Super + K` now opens a fast, searchable list of the [hotkeys](hotkeys.md) that work on your desktop right now, including any you've added or changed, instead of this site's hotkey page in a browser window. Type any part of a hotkey to find it, and press `Enter` to run one of OhMyDebn's hotkeys or your own. Learn > Keybindings in the OhMyDebn menu opens the same list. The website's page is still its last row, for the shortcuts inside apps.

### Improvements

- When SSH Server or Remote Desktop Server shows how to let it through the firewall, the example range is now your machine's own network, such as 192.168.199.0/24. Before, it was always 192.168.1.0/24, which didn't let anyone in if your network was different.

### Fixes

- On MX Linux and LMDE, updating no longer prints a notice that OhMyDebn's package repository doesn't support i386.
- A first installation no longer calls itself "this update" in its messages about restarting Cinnamon and rebooting.

- On Devuan, LCOS and MX Linux with sysvinit, opening Cloudflare WARP or Tailscale from the OhMyDebn menu now explains that it needs systemd, which these systems don't use, and installs nothing. Before, Tailscale's install ended in an error, and WARP installed but could only say "Unable to connect". If you installed either one there, opening it now offers to remove it. The [installation notes](installation.md#devuan-6-excalibur) now say so too.
- On LCOS, opening Remote Desktop Server from the OhMyDebn menu now explains that it can't work with LCOS's X server, and installs nothing. Before, its install ended in an error.
- Opening Deskflow, AbiWord, rclone or Firefox from the OhMyDebn menu on a distro that doesn't have it now says so, and asks nothing. Before, the install ended in an error. Deskflow isn't available on Ubuntu 24.04, Linux Mint 22 or Pop!_OS 24.04, AbiWord and rclone on Kali, and Firefox ESR on Ubuntu, Linux Mint or Pop!_OS, where the menu now points you to your distro's own Firefox.

## 4.16.0

### New

- You can switch your [lock screen](lock-screen.md) to XScreenSaver, a hardened screen locker, in the OhMyDebn menu under Appearance > Lock Screen. It keeps your lock settings and hotkeys, and takes your theme's colors. Cinnamon's lock screen stays the default. While XScreenSaver has your screen locked, the screen may stay on when Power Management would turn it off, and on battery it can dim and brighten again every couple of minutes. To save power while you're away, suspend instead (System > Suspend in the OhMyDebn menu), or close your laptop's lid.

### Improvements

- [SO-CRATES](cybersecurity.md) now opens in your browser by itself once it's running, so you no longer need to click the link in its window.
- The [themes included from Omarchy](desktop-themes.md#themes-included-from-omarchy) are updated to Omarchy 4.5's final release, which touches up two backgrounds: Ethereal's sports car, and Hackerman's geometric one, now sharper.

### Fixes

- Installing Docker now installs its `docker` command too, on distros like MX Linux and LCOS that don't install recommended packages. Before, it could be left out. If yours is missing it, opening Docker from the OhMyDebn menu installs it.
- SSH Server and Remote Desktop Server now tell you whether the firewall lets them through, and how to allow them, on Debian and the distros based on it. Before, that note never appeared there.
- On Devuan, LCOS and other systems without systemd, the SSH Server and Remote Desktop Server windows now show whether the server is running. Before, they showed an error in its place.
- Installing Tailscale now installs Tailscale's signing key package too, on distros like MX Linux that don't install recommended packages. Without it, updates would stop working the next time Tailscale changes its key.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [cliamp](media.md#cliamp) updated to version 2.4.0
- [Codex](ai.md#codex) updated to version 0.167.0
- [Crush](ai.md#crush) updated to version 0.100.0
- fastfetch updated to version 2.71.0
- [Grok Build](ai.md#grok-build) updated to version 1.0.77
- lazygit updated to version 0.66.3
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.18.1
- [OpenCode](ai.md#opencode) updated to version 2.2.6
- [SO-CRATES](cybersecurity.md) updated to version 5.3.0
- [T3 Code](ai.md#t3-code) updated to version 0.1.7

## 4.15.0

### Supported distros

- [Parrot OS 7](installation.md#parrot-os-7) is now supported. OhMyDebn leaves Parrot's package sources as they are, and installs packages that need a library at the version Parrot ships from its backports.

### New

- A [drop-down console](ai.md#drop-down-console): press `Super` and the key left of `1` (`` ` `` on a US keyboard) for a terminal in the middle of your screen, above your other windows, running your default AI assistant. Press the same keys again to hide it; your assistant keeps working while it's hidden, and the console comes back with the same conversation on whichever workspace you're on. It stays floating when window tiling is on, and opens a shell when your default assistant is a desktop app.
- [Jade Horse](desktop-themes.md#jade-horse), a theme in jade greens from Omarchy, with three backgrounds.

### Improvements

- The [themes included from Omarchy](desktop-themes.md#themes-included-from-omarchy) are updated to Omarchy 4.5's, which adds a background to Ethereal. The first time you switch back to a theme after updating, it starts at its first background rather than the one you last had with it, unless that was one of your own.
- [Codex](ai.md#codex) and [herdr](terminal.md#herdr) no longer check for new versions themselves, since they're updated with OhMyDebn. Before, they could offer to update themselves with their own installer, outside the package OhMyDebn installed.

### Fixes

- If OhMyDebn set up Brave's package repository before version 4.5.0, updating now limits that repository to Brave's own packages, as newer installs already do. Before, it could supply any package, and the OhMyDebn doctor reported it as missing its pin.
- If installing Claude Code, Claude Desktop, Brave or Brave Origin can't refresh the vendor's package repository, that repository is now taken out again, as the other installers already do. Before, it stayed behind and made every later update fail.
- Installing OhMyDebn over SSH, if the firewall's question about SSH connections is answered no, now leaves the firewall to the next update to turn on. Before, it stayed off for good.
- Switching themes now keeps gedit's own light, dark or system setting. Before, every switch set it back to light.
- Switching themes now keeps an Alacritty or cava config that's a link into your own dotfiles, and changes the file it points to. Before, the link was replaced with a plain file.
- Remote Desktop Server, when XRDP was installed some other way, now says what it will change and asks before setting it up.
- Cleaning up old SO-CRATES images no longer tries to remove the newest one when it has more than one tag.

### Removed

- Antigravity is no longer offered. Google ends support for 1.x, the last version it released as a Debian package, on November 6, 2026, and newer versions aren't available as one. If you have it installed, it stays until you remove it (Remove > Package), and if it was your default AI assistant, OpenCode is now. Its hotkey, `Ctrl + Super + G`, is free again.
- The Osaka Jade theme is no longer included, since Omarchy replaced it with Jade Horse. If you were using Osaka Jade, updating switches you to Jade Horse.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Codex](ai.md#codex) updated to version 0.166.0
- [Crush](ai.md#crush) updated to version 0.99.0
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.15.0
- [OpenCode](ai.md#opencode) updated to version 2.2.5
- [Pi](ai.md#pi) updated to version 1.5.0
- [SO-CRATES](cybersecurity.md) updated to version 5.2.0
- [T3 Code](ai.md#t3-code) updated to version 0.1.6

## 4.14.0

### Supported distros

- [Zorin OS 18](installation.md#zorin-os-18) is now supported. OhMyDebn installs Cinnamon alongside Zorin's own desktop and leaves Zorin's package sources as they are.

### New

- [Sign a PDF](documents.md#sign-a-pdf), in the OhMyDebn Menu under Apps > Office and under Open With for PDFs in the file manager, lets you place your signature, text and today's date on a PDF and saves a signed copy next to the original, which stays unchanged. Add your signature once from a scan or photo of it on white paper: the paper is removed and the ink keeps its color. Undo, redo and hotkeys make it quick, and its commands let scripts and AI tools sign PDFs with your saved signatures too.
- [OpenCode Desktop](ai.md#opencode-desktop), OpenCode's desktop app, is now in the OhMyDebn Menu under Apps > AI as "OpenCode App (desktop GUI)". It shares your settings, sign-ins and conversations with the OpenCode terminal app, and updates along with it. It installs the first time you choose it.
- [Crush](ai.md#crush), Charm's terminal coding agent, is now in the OhMyDebn Menu under Apps > AI. Like OpenCode, it works with models from many AI companies, and you can switch models in the middle of a session. It installs the first time you choose it, updates with OhMyDebn, and takes its colors from your OhMyDebn theme.
- [velo](utilities.md#velo), a terminal speed test that also measures latency and bufferbloat (how much your connection slows down while it's busy), is now in the OhMyDebn Menu under Trigger > Speed Test > Speed and Bufferbloat (velo), next to the existing speed tests. It installs the first time you choose it.

### Improvements

- [OpenCode](ai.md#opencode) is now version 2, which also works fully with T3 Code. Your settings, sign-ins and conversations carry over, but OpenCode converts its data the first time it starts, so there's no going back to version 1. If you've written your own OpenCode plugins, they need porting to version 2. Its terminal app still takes its colors from your OhMyDebn theme, unless you've picked a theme of your own in OpenCode, and changes them as soon as you switch themes without interrupting conversations running in T3 Code or OpenCode Desktop.
- The Style menu in the OhMyDebn Menu is now called Appearance, and it gathers everything about how the desktop looks. It adds Background, which opens the theme carousel to pick a background, and Fonts and Panel, which open those Cinnamon settings. See [Menus](menus.md).
- Each theme now remembers its background. When you switch back to a theme you've used before, it shows the background you last had with it, instead of starting over at its first, and the theme carousel starts there too. See [Theme Carousel](desktop-themes.md#theme-carousel).
- Oh My Zsh now comes with OhMyDebn instead of being downloaded for each user, and it's updated along with OhMyDebn to a version that's been tested, rather than updating itself from the newest code on its own. Updating switches your Zsh setup over once, keeping a backup of your previous settings, and your own Oh My Zsh plugins and themes keep working. Installing OhMyDebn and resetting its config files no longer need an internet connection for it. See [Terminal](terminal.md).
- Installing Antigravity, Cloudflare WARP, Helium or Tailscale now checks that the key their packages are signed with is the vendor's own before your system trusts it, as installing Brave, Claude Code and PowerShell already did. A key that doesn't match stops the install, so packages signed by anyone else can't be installed in their place.
- Google Chrome and ChatGPT are now installed from their makers' own package repositories, so your system checks each package's signature before installing it, including the very first one. Before, the first install downloaded the package directly and installed it without any check.

### Fixes

- Updating from OhMyDebn 4.5.0, 4.6.0 or 4.7.0 now finishes when another program, such as the software updater, is using the package manager as the update starts. Before, the update could stop partway with a "No such file or directory" error.
- Picking an app from a search in the OhMyDebn Menu now just opens the app. Before, it could open an unrelated menu as well: on Linux Mint, for example, picking Update Manager also opened the Update menu.
- If your distro set up Brave's package repository itself, as Zorin OS does, the OhMyDebn doctor no longer reports it as missing its pin, and removing Brave no longer deletes that repository and its signing key.
- On displays with 2x scaling, the theme intro drawn for backgrounds without an animated intro of their own now fills the screen. Before, the background showed only in the top left quarter while the light and shimmer played.
- Your own Neovim and btop color themes are now kept when OhMyDebn updates. Before, a theme file you put in place of the one that follows OhMyDebn's theme was replaced on every update.
- Your own fastfetch configuration and eza color theme are now kept too. Before, your fastfetch configuration was replaced on every update and theme switch, and switching to a theme without eza colors deleted your eza theme.
- Switching to a theme that writes a color in short form, such as `#f80`, now works. Before, the switch stopped partway and left the desktop half changed.
- Neovim settings files that OhMyDebn adds, such as the one that turns off animated scrolling, now stay deleted if you delete them. Before, each update put them back.
- Installing OhMyDebn on a distro it doesn't officially support no longer replaces that distro's own package sources with Debian's. Before, going ahead on a distro such as Parrot OS or PureOS could swap its package sources for Debian's, which could break it.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Codex](ai.md#codex) updated to version 0.165.0
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.13.3
- [OpenCode](ai.md#opencode) updated to version 2.2.1
- [SO-CRATES](cybersecurity.md) updated to version 5.1.0
- [T3 Code](ai.md#t3-code) updated to version 0.1.5

## 4.13.0

### New

- Switching themes now plays a short intro that fades into the background you chose, and so does logging in. The background starts at twilight, the light arrives from the top down like a sunrise, and the shimmer from the OhMyDebn grin crosses the scene. Seventeen of the themes included from Omarchy play Omarchy's own animated intros for some of their backgrounds instead. A click or any key skips an intro, and Style > Theme Intros in the OhMyDebn Menu turns them off. See [Theme Intros](desktop-themes.md#theme-intros).

### Fixes

- Backgrounds you add for a theme yourself are now included when you cycle through backgrounds, and picking one of them in the theme carousel applies it. Before, the carousel showed them but applied a different background.
- Backgrounds in the WebP image format now display on the desktop and in the theme carousel. Before, they could fail to display unless an image viewer that supports WebP happened to be installed.
- On Kali, the clock is now kept in sync. Kali leaves newly installed network services turned off, including the time service OhMyDebn installs, so the clock could drift and cause errors when updating. Installing or updating turns it on once; if you turn it off yourself later, it stays off.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Codex](ai.md#codex) updated to version 0.164.0
- [Grok Build](ai.md#grok-build) updated to version 1.0.70
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.13.0
- [OpenCode](ai.md#opencode) updated to version 1.19.4
- [Pi](ai.md#pi) updated to version 1.4.0
- [SO-CRATES](cybersecurity.md) updated to version 5.0.1
- [T3 Code](ai.md#t3-code) updated to version 0.1.2
- ttfx updated to version 0.5.1

## 4.12.0

### New

- [Claude Desktop](ai.md#claude-desktop), Anthropic's desktop app for Claude with Claude Code built in, is available as an optional installation in Apps > AI. Its updates come with OhMyDebn's.
- A new [Hardware Notes](hardware-notes.md) page collects tips for machines that need a little extra work. It starts with the Framework Laptop 13 Pro (AMD): how to stop the screen briefly flashing corrupted on Linux kernel 7, and how to stop the laptop freezing.

### Improvements

- The OhMyDebn Menu now has its own button on the panel, the grinning face right next to the Cinnamon menu. You can still open it with `Super + Space`. If you remove the button, updates won't put it back.
- OhMyDebn's notifications now show the OhMyDebn icon, and so do its own windows, such as the menu and the update window, in the window list and window switcher. The icon follows your theme's colors.
- The system summary (`Ctrl + Shift + S`) now shows the OhMyDebn grin, in your theme's colors, instead of your distro's logo. The first line of the summary still names your distro. Every few seconds a shimmer of light crosses the grin, and then it winks. It stays still if you turn off Desktop and window effects in System Settings > Effects.
- The terminal prompt now starts with the OhMyDebn grin instead of your distro's logo, and each new prompt appears about three times faster, so holding down Enter no longer lags. If you changed the prompt's layout yourself, your version is kept as it is.
- On a laptop with AMD's Radeon 890M graphics, such as the Framework Laptop 13 Pro (AMD), the [doctor](updating.md#checking-your-installation) now checks two settings that laptop needs. On Linux kernel 7, it checks that TearFree is on. Without it, small parts of the screen can briefly flash corrupted. On any kernel, it checks the boot setting that stops the laptop from freezing. The doctor links to the [Hardware Notes](hardware-notes.md#framework-laptop-13-pro-amd-ryzen-ai-300-series) steps for both.
- Installing Antigravity now tells you that it's Antigravity 1.x, the last version Google released for Debian-based systems. Google no longer updates it, and it may stop working. The newer Antigravity 2 is a separate download from Google.

### Fixes

- The OhMyDebn Menu has a new icon, a grinning face that takes the theme's colors like the other icons on the panel: solid on dark themes and an outline on light themes. The old icon was missing on LMDE 7, so the menu showed up there with no icon.
- Automatic tiling no longer animates windows into place when you turn off Desktop and window effects in System Settings > Effects. It also stays still if you turn off just Window effects or Resizing and tiling windows there.
- Neovim's start screen no longer has a dark bar along the bottom of the window.
- When you uninstall your default browser, another installed browser now becomes the default, Brave Origin first. Before, `Super + B` and links could open in whichever browser happened to be left, such as Firefox. Removing a browser with Remove > Package in the OhMyDebn Menu switches right away, and the next update fixes a browser you removed some other way. See [Default Browser](browser.md#changing-the-default-browser).
- If your default browser has been uninstalled, web apps now open in whichever browser handles web links instead of not opening at all.
- Removing an app that comes from its vendor's own repository, such as Claude Code, Google Chrome or Claude Desktop, with Remove > Package or `apt` now removes that repository too, so updates stop checking it. Before, only removing the app from a terminal with its own remove command did this. Updating cleans up repositories left behind before.
- On a distro OhMyDebn doesn't support, such as Ubuntu 26.10, updating no longer stops at the unsupported-distro warning every time. It asks once, and asks again only if you move to another unsupported release.
- Installing Chromium could occasionally look for the wrong package and fail, on distros where Chromium comes straight from the distro's own repository, such as Debian. That no longer happens.
- Installing Cloudflare WARP on a new Ubuntu release that Cloudflare doesn't have packages for yet, such as Ubuntu 26.10, now uses its packages for Ubuntu 26.04 instead of failing.
- Installing Claude Code, a Brave browser or PowerShell now checks the vendor's signing keys against the ones the vendor publishes before trusting them, so keys that were tampered with on the way are refused. Existing PowerShell installs are moved to the checked setup on update.
- A theme installed from a git repository can no longer use a link in place of its color file to copy another of your files into the theme.
- Switching to a theme you made yourself no longer stops partway when one of its colors isn't written as `#rrggbb`. Claude Code keeps its current colors for that theme, and the rest of the theme is applied.
- The SO-CRATES image cleanup no longer stops partway when an old image is in use but podman doesn't say by which container. It reports that image and removes the rest.
- If updating the package lists fails while installing Tailscale, the install now stops there with apt's error, instead of skipping the install and failing later with a confusing message.
- When your login session has no runtime directory, as in some `su` and SSH sessions, updates now keep their lock file in your home folder, where another user on the same computer can't block them.
- The Gmail and Cloudflare WARP keybindings now show those names in Cinnamon's keyboard settings on installs from before 4.11.0, which still showed "GMail" and "Cloudflare Warp".
- When OhMyDebn switches your login screen's default session to Cinnamon, the backup it keeps of the original login screen settings is now made only once. Before, if the setting changed again later, the next update replaced that backup with a copy OhMyDebn had already edited, so the original was lost.
- `Ctrl + Super + L` and LocalSend in the OhMyDebn Menu open LocalSend again. Since LocalSend moved where it installs, they did nothing.
- The installers for touchpad gestures, LocalSend and SimpleScreenRecorder now say where they install from, and the unsupported-distro warning now lists Raspberry Pi OS among the supported distros.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Codex](ai.md#codex) updated to version 0.163.0
- [Grok Build](ai.md#grok-build) updated to version 1.0.63
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.11.3
- [OpenCode](ai.md#opencode) updated to version 1.19.3
- [Pi](ai.md#pi) updated to version 1.3.0
- [T3 Code](ai.md#t3-code) updated to version 0.1.0. It now works with Pi too. The first time it starts, it copies your existing threads into its new format, so they carry over. You may need to sign in again to websites you opened inside T3 Code.
- The terminal's Caskaydia Nerd Fonts updated to version 3.5.1
- [Starship](terminal.md), the shell prompt, updated to version 1.27.0, which includes security fixes
- [herdr](terminal.md#herdr) updated to version 0.9.5
- The tree-sitter tool that comes with [Neovim](text-editor.md#neovim) updated to version 0.27.1
- fastfetch updated to version 2.70.0
- lazygit updated to version 0.66.2

## 4.11.0

### Improvements

- The [doctor](updating.md#checking-your-installation) (Update > Doctor) now shows your display scale (such as 2 on a HiDPI screen at 200%) at the top of its report, which helps when reporting a problem.
- Applying the power-user profile to an existing install (`ohmydebn-power-user-install`) now removes only the optional apps your distro came with, and keeps apps that only come from the OhMyDebn menu, such as AI tools, VPNs and other browsers. It lists exactly which apps it will remove and asks first. Before, it also removed every AI tool, VPN and browser you'd installed from the menu.
- Resetting your config files (`ohmydebn-reset-config`) now resets only the app config files it lists, and keeps your current theme. Before, it also reset your panel, keybindings, theme and default apps, switched off other Cinnamon extensions, turned the firewall back on, and upgraded every package on your system. It also no longer moves your Aether folder aside, since OhMyDebn has no default to replace it with. It now also works without an internet connection.
- Removing a package from the menu (Remove > Package) now shows everything apt will remove and asks before going ahead. Before, it removed the packages you picked straight away, along with any other packages that depend on them.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Neovim](text-editor.md#neovim) updated to version 0.12.6
- [Codex](ai.md#codex) updated to version 0.162.1
- [Grok Build](ai.md#grok-build) updated to version 1.0.50
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.10.1
- [OpenCode](ai.md#opencode) updated to version 1.19.0
- [Pi](ai.md#pi) updated to version 1.1.0
- lazygit updated to version 0.66.1

### Fixes

- On HiDPI screens (such as a laptop set to 200% scaling), the [window tiling](window-tiling.md) grid now fits its contents instead of spilling out of its panel, and the gaps between tiled windows are the same size as on other screens instead of half as wide.
- Aborting an update (closing the update window and choosing Abort update) now really stops it: the package being installed finishes, then the update stops. Before, the window said the update was aborted while it carried on in the background.
- Installing ChatGPT, Visual Studio Code, Google Chrome or PowerShell now also installs any libraries they need, and stops with a clear message if the download fails instead of carrying on. The Visual Studio Code download is also checked against Microsoft's published checksum.
- The apt repository ChatGPT adds when you install it is now limited to ChatGPT itself, as OhMyDebn already does for the repositories other apps add. Updating OhMyDebn applies this to existing installs.
- On installs from before 4.10.0, removing an applet from the panel now takes effect right away. Two pairs of panel applets shared an ID, so removing one could leave it running until Cinnamon restarted. 4.10.0 fixed this for new installs, and updating now fixes existing panels. Cinnamon restarts once at the end of that update, so a second network icon that may appear while it runs goes away.
- Switching themes no longer leaves files behind. Each switch kept a full copy of every theme you had applied (over 100 MB on some machines), a new backup of your cava settings, and a Claude Code theme file. Now only the current theme's files are kept, plus one backup of your cava settings from before OhMyDebn first changed them. Your next theme switch clears out the ones left by earlier switches.
- Switching themes no longer creates Claude Code's settings when Claude Code isn't installed. Installing Claude Code now gives it your current theme right away.
- Switching themes no longer deletes a theme you've linked into your themes folder (one you're working on elsewhere, for example).
- On installs from before 4.9.0, Cinnamon's keyboard settings now list the Super + K shortcut as "Keybindings" instead of its old name, "Hotkeys".
- On a computer with more than one OhMyDebn user, a new user's first install or update no longer turns the firewall back on if someone has turned it off. OhMyDebn now sets up the firewall once per computer instead of once per user.
- Installing Virtual Machine Manager no longer restarts your desktop partway through. When your virtual machines can't use hardware acceleration until you log out and back in, it now tells you so.
- Web apps whose address contains `%` (such as `%20`) now open correctly, and a TUI app whose name contains quotes now gets the right window title. If the icon can't be downloaded, no launcher is created, instead of one with a broken icon.
- Removing a web app or TUI app by name no longer deletes an app launcher you made yourself with the same name.
- In the theme picker, choosing a background now always applies the one shown. With your own backgrounds whose names mixed upper and lower case, it could apply a different one.
- With two system info windows open (About), both now update when you change theme.
- The network speed test no longer hangs on "Fetching speed test endpoints..." when the connection stalls.
- Stopping the logo demo no longer stops the logo animation in another open window.
- Removing the remote desktop server now also removes its login check when the server was already removed some other way.
- Cleaning up old SO-CRATES images now keeps the version SO-CRATES starts by default, so the next launch doesn't download it again.
- Installing or removing a package from the menu now says when it didn't finish.
- Shell completions for the `ttfx` command now work on ARM64.
- Applying a theme from the online theme gallery no longer silently does nothing when the current theme's color settings file is damaged.
- Virtual Machine Networking (Apps > Virtualization) now explains when Virtual Machine Manager isn't installed or there are no virtual machines, instead of not opening at all. Its Upgrade button also works when your system isn't in English.
- Install > Package no longer lists apt's "Listing..." line as if it were a package.
- With two logo windows open, both now update when you change theme.
- Removing a line from your keybindings file now also restores Cinnamon keys like Looking Glass's, not just the others.
- Installing Helium now stops with a clear message, and leaves no package source behind, when its repository can't be reached.
- Visual Studio Code no longer tries to install an extension named "null" for themes that don't name one.
- Update > Firmware now asks before installing the tools it needs.
- The terminal speed tests (`ohmydebn-network-speedtest` and `ohmydebn-disk-speedtest`) now simply end when done, instead of leaving you in a second shell.
- SO-CRATES no longer leaves a stopped container behind each time you close it.
- If Oh My Zsh couldn't be downloaded during your first install, the update that later installed it could replace OhMyDebn's `~/.zshrc`, so Zsh started without its prompt and aliases. That no longer happens, and updating puts the file back on any system where it did.

## 4.10.0

### Supported distros

- [Raspberry Pi OS](installation.md#raspberry-pi-os) is now supported on regular x86_64 PCs and virtual machines, not just on Raspberry Pi hardware.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Aether](desktop-themes.md) updated to version 4.32.0
- [Codex](ai.md#codex) updated to version 0.160.1
- [Grok Build](ai.md#grok-build) updated to version 1.0.46
- [LocalSend](utilities.md#localsend) updated to version 1.18.2
- [Oh My Pi](ai.md#oh-my-pi) updated to version 18.8.0
- [OpenCode](ai.md#opencode) updated to version 1.18.35
- [Pi](ai.md#pi) updated to version 1.0.4
- [SO-CRATES](cybersecurity.md) updated to version 4.4.0
- [T3 Code](ai.md#t3-code) updated to version 0.0.45
- lazygit updated to version 0.66.0

### Fixes

- On Raspberry Pi OS, the installer now tells you to reboot to start Cinnamon. It used to tell you to log out and pick Cinnamon, but on Raspberry Pi OS the switch to Cinnamon only takes effect after a reboot.
- If the installer couldn't download the OhMyDebn repository key, for example during a network outage, running it again now works. It used to keep failing until a leftover file was deleted by hand.
- Changing your [desktop theme](desktop-themes.md) no longer stops partway when Claude Code's settings file isn't valid or your cava setup has no color section. The rest of the desktop used to keep its old colors.
- Switching to the next theme now moves on from your current theme. It used to pick the same theme every time.
- If installing an AI tool, cliamp or SO-CRATES from its hotkey or menu item fails, the window now stays open so you can read why.
- Cancelling an update at its first prompt, or starting one while another is already running, no longer makes `ohmydebn-doctor` report a failed update.
- `Ctrl + Shift + K` now opens KeePassXC even while a browser is using the KeePassXC extension.
- Installing Chromium from the menu now refreshes the package lists first, so it no longer fails when they're out of date.
- If installing a theme from a git repository fails, the copy of that theme you already had is kept.
- Reinstalling the Helium browser no longer resets your Helium settings.
- Resetting your configuration now keeps your update logs, and stops at a step that fails instead of carrying on.
- SO-CRATES now tells you when it can't start because your account has no subordinate user IDs, instead of failing partway through the download.
- On new installs, removing an applet from the panel takes effect right away. Two pairs of panel applets shared an ID, so removing one could leave it running until Cinnamon restarted.

## 4.9.0

### Supported distros

- [MX Linux 25](installation.md#mx-linux-25) is now supported, with either systemd or sysvinit.
- [Pop!_OS 24.04](installation.md#pop_os-2404) is now supported. OhMyDebn installs Cinnamon alongside Pop's own COSMIC desktop.

### New

- [Grok Build](ai.md#grok-build), xAI's coding agent, is available from Apps > AI. It needs a SuperGrok or X Premium+ subscription, or an xAI API key.
- [Oh My Pi](ai.md#oh-my-pi), Stencil Labs' extended version of Pi, is available from Apps > AI, and it matches your [desktop theme](desktop-themes.md).
- [T3 Code](ai.md#t3-code) is available from Apps > AI. It runs your AI coding agents (OpenCode, Claude Code, Codex, and Grok Build) side by side in one window, and it matches your [desktop theme](desktop-themes.md).
- New Update > Firmware, which checks your computer's firmware (such as the BIOS/UEFI and SSDs) for updates from the Linux Vendor Firmware Service and installs them. See [Firmware](updating.md#firmware).
- New Update > Channel menu, for choosing where updates come from. Switch OhMyDebn between its stable and testing channels, and Claude Code between its stable and latest channels. See [Channels](updating.md#channels).
- [Neovim](text-editor.md#neovim) now comes ready to use: its plugins, language tools, and syntax highlighting are installed with OhMyDebn, so it no longer downloads anything the first time you open it, and it works offline.
- New Setup > Defaults menu, for choosing your default [AI assistant](ai.md#default-ai-assistant) (the one `Super + A` opens) and your default [browser](browser.md#changing-the-default-browser). Each list shows what you have installed and marks your current default.

### Improvements

- When you install an AI tool from the menu, you're now asked whether to make it your default AI assistant. The default answer is no, so your current default stays unless you type `y`.
- The [desktop themes](desktop-themes.md) that come from Omarchy no longer include backgrounds showing the Omarchy name. Every theme still has at least one background, and a background you're using now stays until you change themes.
- Opening an AI tool from Apps > AI no longer changes your default AI assistant. Use Setup > Defaults > Agent to change it.
- Choosing a default browser has moved from Apps > Browsers > Set Default to Setup > Defaults > Browser, which now lists only the browsers you have installed.
- [Neovim](text-editor.md#neovim) is now the same current version on every supported distro, instead of the older one each distro ships. Its plugins are updated with OhMyDebn releases after they've been tested with it, rather than whenever they change. Plugins you've added yourself are kept.
- [Neovim](text-editor.md#neovim) now matches every [desktop theme](desktop-themes.md). Themes that don't include their own Neovim colors, such as Ethereal, Vantablack, and White, and themes you install from elsewhere, now get Neovim colors made from the theme's own palette instead of Neovim's default colors.
- The [doctor](updating.md#checking-your-installation) (Update > Doctor) checks more: whether your last update finished, free disk space, half-installed packages, the firewall, your clock, your default browser and AI assistant, whether your terminal settings are readable, Neovim and its plugins, and whether UxPlay and Podman have everything they need to run. It also tells you when a reboot is needed, and it checks for problems fixed in this release, such as a virtual machine's display not resizing.

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Neovim](text-editor.md#neovim) updated to version 0.12.5
- LazyVim updated to version 16.0.1
- [Aether](desktop-themes.md) updated to version 4.31.1
- [Codex](ai.md#codex) updated to version 0.159.2
- [OpenCode](ai.md#opencode) updated to version 1.18.33
- [Pi](ai.md#pi) updated to version 0.99.1
- [SO-CRATES](cybersecurity.md) updated to version 4.3.0
- [cliamp](media.md) updated to version 2.3.0
- fastfetch updated to version 2.69.0
- gum updated to version 2.0.2
- [herdr](terminal.md#herdr) updated to version 0.9.3
- ttfx updated to version 0.5.0

### Fixes

- Fixed an error when opening a file in [Neovim](text-editor.md#neovim), caused by a plugin update that no longer supported the version of Neovim included in Debian 13.
- Two [window tiling](window-tiling.md) settings, "UI always centered on monitor" and "Show UI on all monitors", could act as turned on while their settings showed them off, with no way to turn them off. Updating fixes them.
- On a Raspberry Pi, updating no longer says a reboot is needed every time. It was comparing kernels meant for other Raspberry Pi models.
- When OhMyDebn is installed in a virtual machine, the display now resizes with the VM window right away, instead of only after the first restart.
- Installing OhMyDebn on a distro based on Ubuntu that isn't supported yet, such as Zorin OS or elementary OS, no longer replaces that distro's package sources with Debian's.
- Updating over SSH or from a text console no longer ends with an error at its last step, so it now shows whether a reboot is needed.
- Updating no longer stops partway, or quietly skips its last steps, when Oh My Zsh can't be downloaded, when you've removed an app OhMyDebn sets up (such as gedit or cava), or when you use a Neovim configuration of your own.
- If you turned relative line numbers back on in [Neovim](text-editor.md#neovim), updating no longer turns them off again.
- Removing web apps or TUIs from the [menu](menus.md) now works when you have more than one. Before, the list showed them all as a single entry, and choosing it removed nothing.
- A [desktop theme](desktop-themes.md) installed from a git repository can no longer supply its own fastfetch configuration, which could run commands. It gets one made from its colors instead.
- [SO-CRATES](cybersecurity.md) can now be reached only from your own computer, not from other machines on your network. It also no longer changes your Podman settings. Earlier versions turned off IPv6 for every Podman container you run. That setting stays if you have it; to turn IPv6 back on, delete the `pasta_options = ["-4"]` line from `~/.config/containers/containers.conf`.
- Installing [Cloudflare Warp](vpn.md#cloudflare-warp) now works on Kali, Linux Mint, LMDE, Devuan, and LCOS. Before, the install failed there and left behind a package source that stopped every later update, including OhMyDebn's own. If you tried it on one of those and updates have failed since, remove that source with `sudo rm /etc/apt/sources.list.d/cloudflare-client.list`, then update.
- UxPlay, the [AirPlay receiver](media.md#airplay) in Apps > Media, now installs the video and audio plugins it needs, so it starts on distros such as Linux Mint that didn't already have them. If you installed it before, opening it from the menu adds them. It also now uses the ports its instructions tell you to open in the firewall. Before, it picked different ports each time, so Apple devices couldn't connect while the firewall was on. The instructions now give the exact commands to open those ports.
- The theme carousel (`Ctrl + Super + T`) now shows the accent color of themes made with [Aether](desktop-themes.md), instead of plain white.
- The theme carousel no longer shows empty boxes above and below a theme that has only one background, or the same background twice for a theme that has two.
- When a website asks Aether to apply a theme, the confirmation now has Cancel selected, so pressing Enter doesn't apply it. Links that could show one theme source in the confirmation while Aether downloads another are refused.
