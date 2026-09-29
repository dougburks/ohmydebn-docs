## Rhythmbox

Some distros include the [Rhythmbox](https://en.wikipedia.org/wiki/Rhythmbox) music player. If yours doesn't, you can install it:

```bash
sudo apt install rhythmbox
```

![OhMyDebn Rhythmbox](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-rhythmbox.png)

## Cava

To visualize your system audio, run `cava` in a terminal or use [hotkey](hotkeys.md) `Ctrl + Super + A`.

![OhMyDebn Cava audio visualizer](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-cava-audio.png)

## cliamp

[cliamp](https://github.com/bjarneo/cliamp) is a terminal music player. Hotkey `Ctrl + Alt + M` will check to see if it's installed and install if necessary. Alternatively, you can install via the OhMyDebn menu (Apps > Media).

![OhMyDebn cliamp](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-cliamp.png)

## AirPlay

The OhMyDebn menu (Apps > Media) includes [UxPlay](https://github.com/FDH2/UxPlay), an AirPlay receiver. Choosing it installs UxPlay if needed, then starts it listening on ports 6000 to 6002. To start it yourself in a terminal, use the same ports:

```bash
uxplay -p 6000
```

The [firewall](firewall.md) blocks those ports until you open them, along with 5353/udp, which Apple devices use to find the receiver:

```bash
sudo ufw allow 6000:6002/tcp
sudo ufw allow 6000:6002/udp
sudo ufw allow 5353/udp
```

Once the ports are open, any Apple devices on the same network should then see the receiver in their list of AirPlay devices.
