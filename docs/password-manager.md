OhMyDebn includes [KeePassXC](https://keepassxc.org/) to help you manage your passwords.

By default, you get the `keepassxc-full` package which includes browser extension support, ssh agent integration, and other features. If you don't need these extra features and just want a basic password manager, you can switch to the minimal version:

```
sudo apt install keepassxc-minimal
```

Ubuntu 24.04, Linux Mint 22, and Pop!_OS 24.04 have a single `keepassxc` package with every feature, so there's no minimal version to switch to.

You can launch KeePassXC from the Cinnamon menu or via hotkey `Ctrl + Shift + K`.

Once you have a KeePassXC database set up with your usernames and passwords, you can use the auto-type hotkey `Ctrl + Shift + P` to automatically type your username and password into your favorite sites.
