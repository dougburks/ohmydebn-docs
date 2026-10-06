This page lists what's new in each OhMyDebn release, newest first. To get the latest release, see [Updating](updating.md).

Release notes for 4.8.0 and earlier are on [GitHub](https://github.com/dougburks/ohmydebn/releases).

## 4.10.0

### Updated components

Updating OhMyDebn brings you these new versions automatically. The [AI tools](ai.md) are updated if you've installed them.

- [Codex](ai.md#codex) updated to version 0.160.1
- [OpenCode](ai.md#opencode) updated to version 1.18.34
- [Pi](ai.md#pi) updated to version 1.0.4
- [SO-CRATES](cybersecurity.md) updated to version 4.4.0

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
