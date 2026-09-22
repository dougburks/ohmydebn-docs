## Containerization

If you'd like to run containers on your OhMyDebn installation, you can use [Docker](https://www.docker.com/) or [Podman](https://podman.io/). You can also install [Distrobox](https://distrobox.it/) which can use either Docker or Podman.

## Docker

To install [Docker](https://www.docker.com/), launch the OhMyDebn menu and then select `Apps` - `Containers` - `Docker`.

Your user is not automatically added to the `docker` group, since membership in that group is effectively passwordless root: any process running as you could use it to rewrite the host as root with no password prompt. Use `sudo docker ...` instead. If you understand the risk and want the convenience of running docker without `sudo`, you can opt in yourself:

```bash
sudo usermod -aG docker "$USER"
```

Then log out and back in for the change to take effect.

## Podman

To install [Podman](https://podman.io/), launch the OhMyDebn menu and then select `Apps` - `Containers` - `Podman`.

Podman runs rootless, as your own user. OhMyDebn installs the `uidmap` and `passt` packages alongside it and makes sure your user has the subordinate UID and GID ranges rootless containers need, so image pulls and networking work out of the box, including on distros like Devuan and LCOS whose installers don't set those up. If a bare Podman was installed some other way and is missing those pieces, the same menu entry repairs it.

## Distrobox

[Distrobox](https://distrobox.it/) allows you to use any Linux distro inside your terminal. It does this using containers and can use either Docker or Podman.

To install Distrobox, launch the OhMyDebn menu and then select `Apps` - `Containers` - `Distrobox`.
