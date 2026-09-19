## OhMyDebn Logo

To show the OhMyDebn logo in all of its glory, press `Ctrl + Shift + O`.

![OhMyDebn logo gui](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-logo-gui.png)

## OhMyDebn Demo

To show an animated OhMyDebn logo demo, open the OhMyDebn menu and choose the Demo option or just use [hotkey](hotkeys.md) `Ctrl + Alt + D`.

![OhMyDebn animated logo demo](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-demo.gif)

## System Summary

To see a system summary, open the OhMyDebn menu and choose the About option or just use [hotkey](hotkeys.md) `Ctrl + Shift + S`.

![OhMyDebn system summary via fastfetch](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-fastfetch-gui.png)

## System Monitoring

To monitor your system performance, launch btop via Cinnamon menu or via [hotkey](hotkeys.md) `Super + T`.

![OhMyDebn btop](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-btop.png)

## Speed Test

To test your network or disk speed, open the OhMyDebn menu and choose `Trigger` - `Speed Test` - `Network Speed Test` or `Disk Speed Test`. Each shows a live dial readout while it measures, running a download/read pass followed by an upload/write pass. If you'd rather see the results in a [terminal](terminal.md) instead, run `ohmydebn-network-speedtest` or `ohmydebn-disk-speedtest`.

![OhMyDebn network speed test](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-network-speedtest.png)

![OhMyDebn disk speed test](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-disk-speedtest.png)

## Deskflow

[Deskflow](https://github.com/deskflow/deskflow) is available as an optional installation. You can install via OhMyDebn menu (Apps->Utility). You can then run via menu and share your keyboard and mouse with other systems running Deskflow.

## LocalSend

[LocalSend](https://github.com/localsend/localsend) is available as an optional installation. You can install via OhMyDebn menu (Apps->Utility). You can then run via menu and transfer files to other systems running LocalSend.

## SSH Server

SSH server is available as an optional installation. You can install via OhMyDebn menu (Apps->Utility). You can then SSH to the system from other systems.

OhMyDebn's [firewall](firewall.md) denies inbound connections by default and OhMyDebn never opens a port for you, so the server stays unreachable until you allow port 22. The installer and the menu's status window print the two commands: allow from one address or range (recommended), or allow from anywhere.

## Remote Desktop

Remote desktop access over RDP, using [XRDP](https://www.xrdp.org/), is available as an optional installation via OhMyDebn menu (Apps->Utility->Remote Desktop). It installs XRDP, sets up a Cinnamon session for remote logins, and starts the service. Connect from another machine with [Remmina](https://remmina.org/) or any RDP client, using the address the menu shows and port 3389.

Some things to know:

- As with SSH, the firewall stays closed to port 3389 until you allow it. The installer and status window print the commands for allowing one address or range, or anywhere.
- Log in over RDP as a user who isn't logged into the local desktop. Running one user's Cinnamon desktop both locally and remotely at the same time causes conflicts, so OhMyDebn refuses a remote login for a user who already has a local graphical session. A separate user for remote access is simplest.
- If you already have your own `~/.xsession`, OhMyDebn leaves it alone and XRDP runs it as your remote session.

To remove it later, run `ohmydebn-remote-desktop-remove`. It removes the packages and the settings OhMyDebn added, and leaves any firewall rule you created for you to remove.
