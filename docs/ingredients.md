Here's what you get in OhMyDebn by default:

- Base OS: [Debian](https://www.debian.org/)-based distro for stability and compatibility (including systemd-free [Devuan and LCOS](installation.md#devuan-6-excalibur))
- Desktop environment: [Cinnamon](https://github.com/linuxmint/Cinnamon) for a premium desktop experience
- Desktop themes: beautiful themes from Omarchy and [Fausto Korpsvart](https://github.com/Fausto-Korpsvart)
- Desktop icons: artfully polished icons from [Linux Mint](https://linuxmint.com/)
- Theme builder: [Aether](https://github.com/omacom/aether) by [Bjarne Øverli](https://x.com/iamdothash)
- Terminal emulator: [Alacritty](https://alacritty.org/) with Caskaydia Nerd Fonts
- Shell: [Zsh](https://en.wikipedia.org/wiki/Z_shell) with [Oh My Zsh](https://ohmyz.sh/)
- Shell prompt: [Starship](https://starship.rs/)
- Text editors: [gedit](text-editor.md#gedit) and [neovim](text-editor.md#neovim) with [LazyVim](https://www.lazyvim.org/)
- Performance monitoring: [btop](utilities.md#system-monitoring)
- Application launcher: custom GTK app launcher
- Shell cat command alternative: [bat](https://github.com/sharkdp/bat) with syntax highlighting
- Shell commands for directories: [Zoxide](https://github.com/ajeetdsouza/zoxide) for a smarter `cd` command and [eza](https://github.com/eza-community/eza) for beautiful directory listings
- Web browser: [Brave Origin](browser.md) with its built-in Shields content blocker
- Password management: [KeePassXC](https://keepassxc.org/)
- Default image viewer: [Ristretto](documents.md#ristretto)
- PDF editor: [Xournal++](documents.md#xournal)
- System summary: [fastfetch](utilities.md#system-summary)
- Window automation: [xdotool](https://github.com/jordansissel/xdotool)
- Firewall: [ufw](firewall.md) with default deny for inbound traffic
- Eye candy: dazzling terminal effects via [ttfx](https://github.com/omacom-io/ttfx) for demoscene nostalgia
- Audio visualizer: [Cava](media.md#cava)

Your base distro may add more. For example, most of them turn on [AppArmor](https://wiki.debian.org/AppArmor/HowToUse) mandatory access control (LCOS doesn't), and some include the [Rhythmbox](media.md#rhythmbox) music player.

Here are some additional components that you can optionally install:

- AI: [OpenCode](ai.md#opencode) with free and paid models, [Claude Code](ai.md#claude-code), [ChatGPT](ai.md#chatgpt), [Codex](ai.md#codex), [Pi](ai.md#pi), [Oh My Pi](ai.md#oh-my-pi), [Grok Build](ai.md#grok-build), [T3 Code](ai.md#t3-code), [VS Code](ai.md#visual-studio-code-with-github-copilot-ai) with GitHub Copilot AI, [Antigravity](ai.md#antigravity-with-google-agentic-ai) with Google Agentic AI
- VPN: [Cloudflare Warp](vpn.md#cloudflare-warp) or [Tailscale](vpn.md#tailscale)
- Virtualization: run virtual machines via [Boxes](virtualization.md#boxes) or [Virtual Machine Manager](virtualization.md#virtual-machine-manager)
- Containerization: run containers via [Docker](containerization.md#docker) or [Podman](containerization.md#podman)
- Terminal music player: [cliamp](media.md#cliamp)
- Image editor: [GIMP](documents.md#gimp)
- Text editor: [Emacs](text-editor.md#emacs)
- Remote access: [SSH server, Remote Desktop server and client](utilities.md#ssh-server)
- anything from the massive [Debian repo](https://packages.debian.org/trixie/)!
