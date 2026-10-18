This page lists what's new in each OhMyDebn release, newest first. To get the latest release, see [Updating](updating.md).

Release notes for 4.8.0 and earlier are on [GitHub](https://github.com/dougburks/ohmydebn/releases).

## 4.12.0

### Improvements

- The OhMyDebn Menu now has its own button on the panel, the grinning face right next to the Cinnamon menu. You can still open it with `Super + Space`. If you remove the button, updates won't put it back.
- OhMyDebn's notifications now show the OhMyDebn icon, and so do its own windows, such as the menu and the update window, in the window list and window switcher. The icon follows your theme's colors.
- The system summary (`Ctrl + Shift + S`) now shows the OhMyDebn grin, in your theme's colors, instead of your distro's logo. The first line of the summary still names your distro. Every few seconds a shimmer of light crosses the grin, and then it winks. It stays still if you turn off Desktop and window effects in System Settings > Effects.
- On a laptop with AMD's Radeon 890M graphics, such as the Framework Laptop 13 Pro (AMD), the [doctor](updating.md#checking-your-installation) now checks two settings that laptop needs. On Linux kernel 7, it checks that TearFree is on. Without it, small parts of the screen can briefly flash corrupted. On any kernel, it checks the boot setting that stops the laptop from freezing. The doctor links to the [Hardware Notes](hardware-notes.md#framework-laptop-13-pro-amd-ryzen-ai-300-series) steps for both.

### Fixes

- The OhMyDebn Menu has a new icon, a grinning face that takes the theme's colors like the other icons on the panel: solid on dark themes and an outline on light themes. The old icon was missing on LMDE 7, so the menu showed up there with no icon.
- Automatic tiling no longer animates windows into place when you turn off Desktop and window effects in System Settings > Effects. It also stays still if you turn off just Window effects or Resizing and tiling windows there.
- Neovim's start screen no longer has a dark bar along the bottom of the window.
- On a distro OhMyDebn doesn't support, such as Ubuntu 26.10, updating no longer stops at the unsupported-distro warning every time. It asks once, and asks again only if you move to another unsupported release.
- Installing Cloudflare WARP on a new Ubuntu release that Cloudflare doesn't have packages for yet, such as Ubuntu 26.10, now uses its packages for Ubuntu 26.04 instead of failing.

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
