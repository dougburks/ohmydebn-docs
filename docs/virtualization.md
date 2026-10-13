## Virtualization

If you'd like to run a virtual machine (VM) on your OhMyDebn installation, you can use Boxes or Virtual Machine Manager. [Boxes](https://apps.gnome.org/Boxes/) is the simpler of the two, but that simplicity comes from deliberately limited control - it's a good fit for spinning up a single VM every now and then, not much more. For anything beyond that (multiple VMs, snapshot management, custom hardware configuration, or any other fine-grained control), use [Virtual Machine Manager](https://virt-manager.org/) instead.

## Boxes

The hotkey for [Boxes](https://apps.gnome.org/Boxes/) is `Ctrl + Alt + B`. This will check to see if Boxes is installed and install it if necessary. Alternatively, you can install Boxes by running `ohmydebn-boxes-install` or launch the OhMyDebn menu and then select Apps > Virtualization > Boxes (Simple).

When asked, press Enter to continue, and wait for the installation to finish.

You can then start Boxes from the Cinnamon menu or OhMyDebn menu or via [hotkey](hotkeys.md) `Ctrl + Alt + B`.

## Virtual Machine Manager

The hotkey for [Virtual Machine Manager](https://virt-manager.org/) is `Ctrl + Alt + V`. This will check to see if Virtual Machine Manager is installed and install it if necessary. Alternatively, you can install Virtual Machine Manager by running `ohmydebn-virtmanager-install` or launch the OhMyDebn menu and then select Apps > Virtualization > Virtual Machine Manager (Advanced).

When asked, press Enter to continue, and wait for the installation to finish. If it then says to log out and back in, do that before starting a virtual machine: until then your virtual machines can't use hardware acceleration and run much more slowly.

You can then start Virtual Machine Manager from the Cinnamon menu or OhMyDebn menu or via [hotkey](hotkeys.md) `Ctrl + Alt + V`.

Once you've created a VM, you can take snapshots of it: open the VM, choose View > Snapshots, then click `+` at the bottom left.

!!! warning "Set Snapshot Mode to internal"
    In the Create snapshot window, make sure `Snapshot Mode` is set to `internal` before you click Finish. Internal snapshots are stored inside the VM's disk image, so they're much simpler to revert to and delete later. Check this every time you create a snapshot.

## Networking

Virtual Machine Manager is set up to use an unprivileged, per-user connection (`qemu:///session`) rather than the traditional system-wide one. This means there's no `Virtual network 'default'` (NAT) option when creating a VM - when you reach the network selection step, choose `Usermode networking` instead.

By default, `Usermode networking` uses QEMU's older built-in SLIRP driver. The `passt` package is installed automatically alongside Virtual Machine Manager and offers substantially better throughput, but it isn't used automatically - libvirt still defaults to SLIRP even with `passt` installed.

To upgrade an existing VM to `passt`, open the OhMyDebn menu and select Apps > Virtualization > Virtual Machine Networking. This lists the VMs in your user session (`qemu:///session`), whether they were created with Virtual Machine Manager or Boxes, along with each one's current networking backend, and lets you upgrade any VM that's still using SLIRP with one click. The VM must be shut off first, since a networking backend change only takes effect the next time it starts.

Alternatively, if you're creating a new VM from the command line, you can use `virt-install --network type=passt` from the start instead of the graphical wizard.
