## Why Debian?

Here are my requirements for a base OS:

- can run on bare metal and virtualized
- can be virtualized via Proxmox, Parallels, and other hypervisors
- must be supported by Parallels Tools
- must support x86 and ARM architectures

Debian satisfies these requirements and is well known for stability, simplicity, and versatility.

## Why Cinnamon desktop?

Here are my requirements for a desktop environment:

- must be available on my preferred base OS (Debian)
- able to support a traditional program menu
- able to support a traditional taskbar with the ability to re-arrange the order in which running programs are listed
- support hotkeys
- stable and reliable
- relatively light on resources
- must be responsive and not slow me down

Cinnamon satisfies these requirements and has some nice eye candy!

## Should I start with Debian or Linux Mint?

Either works great, and our installer supports both. If you're on x86_64 hardware and don't have a favorite, we recommend [Linux Mint Cinnamon Edition](installation.md#installation-with-linux-mint-cinnamon) - Mint develops the Cinnamon desktop, so it ships a newer version of Cinnamon than Debian 13 does, plus a friendly installer, a driver manager, and multimedia codecs out of the box. If your hardware is very new, Mint also offers an [HWE ISO](https://www.linuxmint.com/hwe.php) with a newer kernel.

That said, Debian remains the project's foundation, and there are cases where it's the right choice:

- Linux Mint is only available for x86 architecture. If you're on ARM, you need a distro compiled for ARM that can run Cinnamon (like Debian).
- Raspberry Pi OS is based on Debian 13. You can use this repo to turn it into OhMyDebn!
- You want the most vanilla base possible - for fun and for science!

Linux Mint Debian Edition (LMDE) splits the difference - it's Debian-based and already ships Cinnamon. Our [installer supports installing directly onto LMDE 7](installation.md#linux-mint-debian-edition-7) if you'd rather have Mint's extras on a Debian base.

Plain Ubuntu works too - our [installer also supports installing directly onto Ubuntu 24.04/26.04](installation.md#ubuntu) if that's where you're already set up.


## What is the relationship between OhMyDebn and Security Onion?

OhMyDebn is not directly related to the [Security Onion](https://github.com/Security-Onion-Solutions/securityonion) project. OhMyDebn is sponsored by [Security Onion Solutions](https://securityonion.com) (SOS); however, SOS does not provide any technical support for it. OhMyDebn is intended to provide a general purpose desktop environment so, of course, you could use the included [Chromium web browser](browser.md) to connect to your [Security Onion Console](https://docs.securityonion.net/en/3/main/security-onion-console/)!

