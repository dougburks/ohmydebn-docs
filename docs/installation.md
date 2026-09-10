## Choosing a base distro

OhMyDebn installs on top of an existing Debian-based distro: Debian 13, or a supported derivative like Linux Mint 22, Linux Mint Debian Edition (LMDE) 7, Kali Linux (Rolling), or Ubuntu 24.04/26.04. If you already have a favorite, start there - see the sections below for any distro-specific notes.

If you don't have a favorite, we recommend [Linux Mint Cinnamon Edition](https://linuxmint.com/download.php) on x86_64 hardware. Mint develops the Cinnamon desktop, so it ships a newer version of Cinnamon than Debian 13 does, and it adds a friendly installer, a driver manager, and multimedia codecs out of the box. Linux Mint is only available for x86_64, so on ARM hardware start with [Debian 13](#debian-13-live-cinnamon) or [Raspberry Pi OS](#raspberry-pi) instead.

## Installation with Linux Mint Cinnamon

1. Download the latest Linux Mint Cinnamon Edition ISO image from <https://linuxmint.com/download.php> and install it.

    !!! tip
        If your hardware is very new and the standard ISO won't boot or is missing drivers, use the [Linux Mint HWE ISO](https://www.linuxmint.com/hwe.php) instead - it's the same Mint with a newer kernel for hardware enablement. Otherwise, stick with the standard ISO as Mint recommends, since proprietary drivers and third-party modules (NVIDIA, Broadcom, VirtualBox, etc.) may have limited support with newer kernels.

2. In your new Linux Mint Cinnamon desktop, download the installation script:
```
curl -LO https://ohmydebn.org/install.sh
```
3. Once you have reviewed install.sh and the rest of the [source code](source-code.md), you can run the install script as your normal non-root user:
```
bash install.sh
```

Our installer will detect Mint and continue on with OhMyDebn installation. It will also disable a few Mint-specific autostart apps (Update Manager, System Reports, Welcome Screen, Warpinator, and Sticky Notes) that either duplicate something OhMyDebn already provides (Warpinator vs. our LocalSend integration) or just add unrequested noise on first login - you can always re-enable any of them from Cinnamon's Startup Applications settings.

## Installation Options

By default, the installation script leaves existing packages like Firefox, Thunderbird, and LibreOffice in place. The installation script supports the following options:

- `--power-user` - removes optional apps that ship in your base distro (Firefox, LibreOffice, etc.) and installs a curated set of power-user extras: [Virtual Machine Manager](virtualization.md#virtual-machine-manager), Brave Origin, GIMP, Podman, keepassxc-minimal, rclone, openssh-server, pdftk-java, rsync, ethtool, traceroute, lshw, shellcheck, and iperf3. It also enables the [screen magnifier](screen-magnifier.md). On Kali Linux, Firefox is left in place even with this option since Kali doesn't ship an alternative browser by default.
- `--yes` - skips every confirmation prompt for unattended installs (for example, scripted or automated provisioning). Everything the prompts warn about still happens; this only removes the pause to read them, so make sure you understand those warnings before using it.

Example:
```
bash install.sh --power-user
```

If you didn't use `--power-user` during installation but want to apply that same profile later, you don't need to reinstall - just run this from a [terminal](terminal.md) on an already-installed system:
```
ohmydebn-power-user-install
```
## Alternative installations

### Linux Mint Debian Edition 7

Linux Mint Debian Edition (LMDE) 7 is based on Debian 13 and our installer allows for installation on LMDE 7.

### Debian 13 Live Cinnamon

If you prefer vanilla Debian, start with the Debian Live 13 Cinnamon ISO image on x86_64 hardware. Download it from <https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/> and install it. Reboot into your newly installed Debian 13 Cinnamon and then run our installer as shown above.

### Debian 13 Minimal

Instead of starting from a Debian Live 13 Cinnamon ISO image, an alternative is to start from a Debian 13 minimal netinst installer on x86_64 or ARM64 hardware. Once the Debian netinst installer completes, reboot into your new installation and then start our installer as shown above. It will automatically install the necessary Cinnamon desktop packages and continue on with OhMyDebn installation. Once installation is complete, reboot and enjoy your new OhMyDebn desktop!

### Kali Linux

Kali Linux (Rolling) is also supported. Once you're connected to the Internet, run our installer as shown above and it will detect Kali and continue on with OhMyDebn installation.

### Ubuntu

Ubuntu 24.04 LTS and 26.04 LTS (on x86_64 hardware) are also supported. Once you're connected to the Internet, run our installer as shown above and it will detect Ubuntu and continue on with OhMyDebn installation. Chromium is only available as a snap on Ubuntu, so that's how OhMyDebn installs and configures it there - functionally equivalent, though its Appearance settings currently can't follow your OhMyDebn theme's dark/light mode automatically due to a snap packaging limitation.

### Raspberry Pi

!!! tip
    For best results, we recommend a Raspberry Pi 5 with SSD and at least 4GB RAM.

The default OS for Raspberry Pi is Raspberry Pi OS and the latest version is based on Debian 13. Once you're running this version and are connected to the Internet, you can run our installer as shown above. It will automatically update /etc/lightdm/lightdm.conf to log into our Cinnamon desktop. Once our installer is complete, reboot and enjoy your new OhMyDebn desktop!

If you are running an older Raspberry Pi or the desktop otherwise feels sluggish, consider disabling desktop effects. Instructions can be found in the [Desktop Effects](desktop-effects.md) section.
