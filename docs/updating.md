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

Alongside it, `stages-latest.log` is a short timeline of the same run: one line per stage with the clock time and how long into the run it started, which is the quickest way to see which stage took the time.

## One update at a time

Only one update can run at a time. If you start a second one, whether from the menu, the hotkey, the notification, or a terminal, it tells you an update is already running and exits. Wait for the first one to finish.

If the update can't reach OhMyDebn's own package repository, for example with no Internet access, it stops before changing anything and tells you. Any other repository that fails to refresh, such as a third-party one that is down or no longer exists, is listed in a warning and skipped for that run, and the update continues. If a listed repository is one you no longer need, remove it from `/etc/apt/sources.list.d/`.

## Checking your installation

OhMyDebn includes a read-only self-check that looks at everything the installer sets up and reports one line per item: packages and the OhMyDebn apt repository, the Cinnamon extension and its settings, the current theme, the login session default, the update timer, the AI tools and their shell aliases, the custom hotkeys, and the tools other OhMyDebn commands rely on. It changes nothing.

Run it from the OhMyDebn menu (Update -> Doctor), or from a terminal:

```bash
ohmydebn-doctor
```

Anything marked `FAIL` is worth a look, and the summary at the end lists them. If something on your system seems off after an update, running the doctor and including its output when asking for help is the quickest way to get a useful answer.

Run it from a terminal inside your Cinnamon session so it can check the desktop settings too. Over SSH it still runs, but the desktop-specific checks are marked as skipped rather than failed.
