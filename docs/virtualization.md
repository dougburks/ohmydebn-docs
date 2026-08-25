## Virtualization

If you'd like to run a virtual machine (VM) on your OhMyDebn installation, you can use Boxes or Virtual Machine Manager. [Boxes](https://apps.gnome.org/Boxes/) is simpler and is the recommended option for most users. If you need more flexibility, then consider [Virtual Machine Manager](https://virt-manager.org/).

## Boxes

The hotkey for [Boxes](https://apps.gnome.org/Boxes/) is `Ctrl + Alt + B`. This will check to see if Boxes is installed and install it if necessary. Alternatively, you can install Boxes by running `ohmydebn-boxes-install` or launch the OhMyDebn menu and then select `Install` - `Virtualization` - `Boxes`.

At the prompt, press Enter to continue:

![OhMyDebn Boxes Prompt](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-boxes-0-prompt.png)

Installation complete:

![OhMyDebn Boxes Installed](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-boxes-1-installed.png)

You can then start Boxes from the Cinnamon menu or Apps menu or via [hotkey](hotkeys.md) `Ctrl + Alt + B`.

![OhMyDebn Boxes Interface](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-boxes-2-interface.png)


## Virtual Machine Manager

The hotkey for [Virtual Machine Manager](https://virt-manager.org/) is `Ctrl + Alt + V`. This will check to see if Virtual Machine Manager is installed and install it if necessary. Alternatively, you can install Virtual Machine Manager by running `ohmydebn-virtmanager-install` or launch the OhMyDebn menu and then select `Install` - `Virtualization` - `Virtual Machine Manager`.

At the prompt, press Enter to continue:

![OhMyDebn Virtualization Prompt](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-virtualization-0-prompt.png)

Installation complete:

![OhMyDebn Virtualization Installed](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-virtualization-1-installed.png)

You can then start Virtual Machine Manager from the Cinnamon menu or Apps menu or via [hotkey](hotkeys.md) `Ctrl + Alt + V`.

![OhMyDebn Virtualization Machine Manager](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-virtualization-2-vmm.png)

Once you've created a VM, if you want to create a snapshot then we recommend setting `Snapshot Mode` to `internal`:

![OhMyDebn Virtualization Snapshots](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-virtualization-3-snapshots.png)

## Networking

Virtual Machine Manager is set up to use an unprivileged, per-user connection (`qemu:///session`) rather than the traditional system-wide one. This means there's no `Virtual network 'default'` (NAT) option when creating a VM — when you reach the network selection step, choose `Usermode networking` instead.

By default, `Usermode networking` uses QEMU's older built-in SLIRP driver. The `passt` package is installed automatically alongside Virtual Machine Manager and offers substantially better throughput, but it isn't used automatically — libvirt still defaults to SLIRP even with `passt` installed. To use `passt`, either create the VM with `virt-install --network type=passt` instead of the graphical wizard, or edit the VM's network device XML afterward (`virsh --connect qemu:///session edit <vm-name>`) and add `<backend type="passt"/>` inside the `<interface type="user">` element.
