You can start a terminal session from the Cinnamon menu, Apps menu, or via [hotkey](hotkeys.md) `Super + Enter`. This launches a beautiful and powerful [Alacritty](https://alacritty.org) terminal window that includes:

- Caskaydia Nerd Fonts
- [Zsh](https://en.wikipedia.org/wiki/Z_shell) shell with [Oh My Zsh](https://ohmyz.sh/)
- [Starship](https://starship.rs/) shell prompt
- [Zoxide](https://github.com/ajeetdsouza/zoxide) for a smarter `cd` command
- [eza](https://github.com/eza-community/eza) for beautiful directory listings via `ls` and `lt`

![OhMyDebn terminal screenshot](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-terminal.png)

It also includes [bat](https://github.com/sharkdp/bat), which is a `cat` clone with syntax highlighting and git integration.

![OhMyDebn bat screenshot](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-bat.png)

A few more terminal-focused tools are available from the OhMyDebn menu's Apps->Terminals section:

## tmux

[tmux](https://github.com/tmux/tmux) is available as an optional installation. You can install via OhMyDebn menu (Apps->Terminals) or [hotkey](hotkeys.md) `Super + Alt + Return`. That hotkey checks to see if it's installed first so even on a new installation you can just press `Super + Alt + Return` and it will install and then attach to a persistent session named `main` - closing and reopening the terminal returns you to where you left off.

## PowerShell

[Microsoft PowerShell](https://github.com/PowerShell/PowerShell) is available as an optional installation. You can install via OhMyDebn menu (Apps->Terminals) or [hotkey](hotkeys.md) `Ctrl + Alt + P`.

## herdr

[herdr](https://herdr.dev/) is a persistent runtime for AI coding agents (Claude Code, Codex, opencode, and others) - it owns their terminal sessions on a server you control, so an agent keeps working on long-running tasks even after you disconnect or close your laptop, and you can reconnect from any device to check on it. It's available as an optional installation. You can install via OhMyDebn menu (Apps->Terminals) or [hotkey](hotkeys.md) `Ctrl + Super + Return`. That hotkey checks to see if it's installed first so even on a new installation you can just press `Ctrl + Super + Return` and it will install and then run.
