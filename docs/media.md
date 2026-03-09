## Rhythmbox

OhMyDebn includes [Rhythmbox](https://en.wikipedia.org/wiki/Rhythmbox) music player by default.

![OhMyDebn Rhythmbox](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-rhythmbox.png)

## cliamp

The [OhMyDebn menu](ohmydebn-menu.md) includes an option to install [cliamp](https://github.com/bjarneo/cliamp) which is a terminal music player.

![OhMyDebn cliamp](https://raw.githubusercontent.com/dougburks/ohmydebn-docs/refs/heads/main/images/ohmydebn-cliamp.png)

## Airplay

The [OhMyDebn menu](ohmydebn-menu.md) includes an option to install [Uxplay](https://github.com/FDH2/UxPlay) which is an Airplay receiver. Once installed, you can run it like this to listen on ports starting at 6000:

```bash
uxplay -p 6000
```

You will need to open [firewall](firewall.md) ports 6000, 6001, and 6002 for both UDP and TCP. You will also need to allow 5353/udp for mdns.

Once the ports are open, any Apple devices on the same network should then see the receiver in their list of Airplay devices.
