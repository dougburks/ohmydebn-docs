To reset OhMyDebn's app config files to their defaults, run `ohmydebn-reset-config`. It resets the configs for Alacritty, bat, btop, cava, Neovim, Starship, Oh My Zsh and your `~/.zshrc`, and keeps your current ones as backups (each renamed to `<name>-backup-<date and time>`), so nothing you changed is lost.

```bash
ohmydebn-reset-config
```

It changes only those config files. Your desktop settings, panel, Cinnamon extensions, keybindings, theme, firewall and default apps stay as they are, and your current theme is applied to the fresh configs.
