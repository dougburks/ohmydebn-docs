## Installation with Debian Live 13 Cinnamon ISO image

For the quickest and easiest installation, the best option is to start with the Debian Live 13 Cinnamon ISO image on x86_64 hardware. If for some reason that doesn't work for your use case, see the [alternative installation options](#alternative-installations) below.

1. Download the Debian Live 13 Cinnamon ISO image from <https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/> and install it. Reboot into your newly installed Debian 13 Cinnamon and the default desktop should look like this:
![debian-cinnamon screenshot](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/debian-cinnamon.png)
2. In your Debian 13 Cinnamon desktop, download the installation script:
```
curl -LO https://ohmydebn.org/install.sh
```
3. Once you have reviewed install.sh and the rest of the [source code](#source-code), you can run the install script:
```
bash install.sh
```
## Installation Options

The installation script supports the following option:

- `--no-uninstall` - installs OhMyDebn without removing existing packages like Firefox, Thunderbird, etc.

Example:
```
bash install.sh --no-uninstall
```
## Alternative installations

### Debian 13 Minimal

Instead of starting from a Debian Live 13 Cinnamon ISO image, an alternative is to start from a Debian 13 minimal netinst installer on x86_64 or ARM64 hardware. Once the Debian netinst installer completes, reboot into your new installation and then start our installer as shown above. It will automatically install the necessary Cinnamon desktop packages and continue on with OhMyDebn installation. Once installation is complete, reboot and enjoy your new OhMyDebn desktop!

### Raspberry Pi

!!! tip
    For best results, we recommend a Raspberry Pi 5 with SSD and at least 4GB RAM.

The default OS for Raspberry Pi is Raspberry Pi OS and the latest version is based on Debian 13. Once you're running this version and are connected to the Internet, you can run our installer as shown above. It will automatically update /etc/lightdm/lightdm.conf to log into our Cinnamon desktop. Once our installer is complete, reboot and enjoy your new OhMyDebn desktop!

If you are running an older Raspberry Pi or the desktop otherwise feels sluggish, consider disabling desktop effects. Instructions can be found in the [Desktop Effects](desktop-effects.md) section.

### Proxmox 9

Proxmox 9 is based on Debian 13 and will work with our installer as well.

!!! warning
    We do not recommend installing OhMyDebn on a production Proxmox server! However, Proxmox + OhMyDebn makes for an amazing personal virtualization workstation.

In order to install on Proxmox 9, you will need to take care of a few prerequisites:

1. Make sure that Proxmox has full access to APT repos. By default, Proxmox is configured to use Proxmox subscription repos. If you don't have a subscription, then you will need to change to the no-subscription repo. For more information, please see <https://pve.proxmox.com/wiki/Package_Repositories>.
2. Make sure that sudo is installed (`apt -y install sudo`).
3. Make sure that you have a non-root user account (for example: `adduser yourusername`).
4. Make sure that your non-root user account has sudo privileges (for example: `usermod -aG sudo yourusername`).
5. Login as your non-root user account.
6. Start the installation as shown above.
7. Once the installation completes, reboot (`sudo reboot`), login as your non-root user, and enjoy your new OhMyDebn desktop!


