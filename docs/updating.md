OhMyDebn automatically checks for updates every 6 hours by default. If it finds a new version of OhMyDebn, it will pop up a notification. You can click the notification to update to the latest version.

Before updating, please review the [Release Notes](https://github.com/dougburks/ohmydebn/releases) so that you are aware of any changes.

Also make sure that you have stable power and Internet access to avoid any interruptions to the update process.

In addition to the pop-up notification, there are a few other ways to start the update process:

- open the OhMyDebn menu and select Update - OhMydebn
- use [hotkey](hotkeys.md) Ctrl + Super + U
- if you're already in a [terminal](terminal.md) and want to run from there then you can use:
```bash
ohmydebn-update
```

This will update the base OS packages, our OhMyDebn packages, and any config files if necessary.

## Reboots

If the update installs a new kernel, or a package asks for a reboot, the update finishes with a notice saying so. Nothing is broken in the meantime, the new kernel simply isn't in use until you reboot, so reboot whenever it's convenient.

## Logs

Every update is logged to `~/.local/state/ohmydebn-logs/`, one file per run, with `update-latest.log` always pointing at the most recent one. The ten most recent logs are kept. If an update fails, that log is the thing to look at (or to include when asking for help):

```bash
less ~/.local/state/ohmydebn-logs/update-latest.log
```

## One update at a time

Only one update can run at a time. If you start a second one, whether from the menu, the hotkey, the notification, or a terminal, it tells you an update is already running and exits. Wait for the first one to finish.

If the update can't refresh the package lists, for example with no Internet access or a broken third-party repository, it stops before changing anything and tells you which repository failed. Fix or remove that repository, then run the update again.
