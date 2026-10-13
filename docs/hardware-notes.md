## Hardware Notes

OhMyDebn runs on any hardware your base distro supports, so most machines need nothing special. This page collects tips for specific machines that needed a little extra work.

## Framework Laptop 13 Pro (AMD Ryzen AI 300 Series)

Tested in October 2026 on Linux Mint 22.3, on a [Framework Laptop 13 Pro](https://frame.work/laptop13pro) with AMD Ryzen AI 300 Series and Radeon 890M graphics. These steps are for the AMD model, not the Intel one. To check whether your laptop has the same graphics chip, run `lspci -nn | grep 1002:150e`. Other laptops with this chip may need the same steps.

**The problem:** on Linux kernel 7, small rectangles of the screen briefly flash corrupted, for example when you open or close terminal windows or change themes. Kernel 6.17 doesn't do this. It's a bug in the kernel's AMD graphics driver, not in OhMyDebn, Cinnamon or Linux Mint, and it shows up on other distros too (upstream reports: [drm/amd #5950](https://gitlab.freedesktop.org/drm/amd/-/work_items/5950), [drm/amd #5524](https://gitlab.freedesktop.org/drm/amd/-/work_items/5524)). Turning on the graphics driver's TearFree setting avoids it, so you can keep getting kernel updates.

### 1. Install Linux Mint 22.3 from the HWE ISO

Linux Mint's regular 22.3 ISO comes with kernel 6.14, which is too old for this laptop. Download the [Linux Mint HWE ISO](https://www.linuxmint.com/hwe.php) instead, which comes with a newer kernel, and install it.

### 2. Turn on TearFree

First, check that the AMD driver for the X display server is installed. Linux Mint installs it by default. This command should show a line starting with `ii`:
```
dpkg -l xserver-xorg-video-amdgpu
```
If it doesn't, install it with `sudo apt install xserver-xorg-video-amdgpu`. Don't skip this check: the setting below names that driver, and without it your desktop won't start.

Then create the setting:
```
sudo mkdir -p /etc/X11/xorg.conf.d
sudo tee /etc/X11/xorg.conf.d/20-amdgpu-tearfree.conf <<'EOF'
Section "Device"
    Identifier "AMD"
    Driver "amdgpu"
    Option "TearFree" "true"
EndSection
EOF
```
Log out and back in (or reboot). To check that it's on, run this command. It should show `TearFree: on`:
```
xrandr --prop | grep -i tearfree
```
TearFree makes the graphics driver copy each frame into its own buffer before showing it, which avoids the bug. The extra copy costs very little on this graphics chip.

To undo it, delete the file with `sudo rm /etc/X11/xorg.conf.d/20-amdgpu-tearfree.conf`, then log out and back in.

### 3. Install OhMyDebn

Follow the [installation steps](installation.md#installation-with-linux-mint-cinnamon) as usual. The installer's system upgrade moves you to kernel 7, which is fine with TearFree on.

### 4. Optional: if your laptop freezes

If the screen freezes and you have to hold the power button to turn the laptop off, try adding this boot setting for the graphics driver. Edit `/etc/default/grub` so this line reads:
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.dcdebugmask=0xC10"
```
Then run this command and reboot:
```
sudo update-grub
```
It turns off three of the display's power-saving features: Panel Self Refresh, Panel Replay and Idle Power States. Battery life may be a little shorter, so only add it if you've had a freeze. Our test laptop froze once and hasn't frozen since we added it, but one freeze isn't enough to be sure it was the fix.

!!! note
    If you dual boot with another Linux install, the change only takes effect if this install's boot menu is the one that starts the laptop. Otherwise, add the setting in the other install's `/etc/default/grub`.

### 5. If you still see glitches

If the screen still flashes corrupted with TearFree on, go back to kernel 6.17 and stay there until a newer kernel fixes the bug:
```
sudo apt install linux-generic-6.17
sudo apt remove linux-generic-hwe-24.04 linux-image-generic-hwe-24.04 linux-headers-generic-hwe-24.04
```
Reboot. If the boot menu is hidden, hold `Shift` or press `Esc` while the laptop starts to show it, and choose the 6.17 kernel under *Advanced options*. Once you're running 6.17 (check with `uname -r`), remove the kernel 7 packages:
```
sudo apt remove 'linux-image-7.*'
```
You'll keep getting updates for kernel 6.17, but updates won't move you to kernel 7. To check, run `dpkg -l 'linux-*generic-hwe-24.04'`: it should list nothing as installed (`ii`). Kernel 6.17 will eventually stop getting security updates, so to try a newer kernel later, run `sudo apt install linux-generic-hwe-24.04` and reboot.
