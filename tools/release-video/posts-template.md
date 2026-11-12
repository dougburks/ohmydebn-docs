# OhMyDebn <version> announcement posts

<!--
The template for each release's posts.md, which lives with that release's
video in ~/git/ohmydebn-<version>-video/, outside the repositories: each
release's own wording isn't kept in git, so start from the previous
release's posts.md when it's still there, and from this when it isn't.

What every release's posts have in common:

- Lead with what readers gain, not the version number. The release's
  biggest New item usually leads; a release with news beyond OhMyDebn
  (4.16.0's lock screen vulnerability) can lead with that instead.
- Name features as users see them: menu paths and hotkeys, never script
  names or file paths. Match the release notes' wording and claim nothing
  they don't.
- Every post links to the release's section of the release notes:
  https://ohmydebn.org/release-notes/#<version without dots>, such as
  #4160 for 4.16.0. A feature with its own page can link there too.
- Count every post against its limit before calling it done:
  - X: 280 characters, with each link counted as 23 whatever its length.
  - Bluesky: 300 characters. Count links in full, to be safe.
  - Mastodon: 500 characters on most servers (links count as 23), but
    each server sets its own; check the one you post from.
  - LinkedIn: 3,000 characters.
- Mastodon ends with hashtags. LinkedIn is the longest: what OhMyDebn is,
  for readers who haven't heard of it, the release's items as a list, and
  how to get it.
- The alt text describes what the video shows, in order, for someone who
  can't see it: no marketing, and no claims the video doesn't show.
-->

Video: `ohmydebn-<version>.mp4` (1920x1080, <length> s, H.264 with a silent audio track, <size> MB). Still: `ohmydebn-<version>-still.jpg`. <Anything about how the clips were recorded that a reader of the video should know, such as made-up passwords or a nested display.>

## X

<Headline: the release's biggest gain, in one sentence.>

<One or two sentences on what else is in it.>

https://ohmydebn.org/release-notes/#<version without dots>

## Bluesky

<Usually the X post, with the extra 20 or so characters spent on one more detail.>

https://ohmydebn.org/release-notes/#<version without dots>

## Mastodon

<Headline.>

<A short paragraph on the biggest item: what it does and where to find it (menu path or hotkey).>

<A sentence or two on the rest: improvements, fixes, updated components.>

https://ohmydebn.org/release-notes/#<version without dots>

#Linux #Debian #Cinnamon <tags for the release's topics>

## LinkedIn

<Headline.>

OhMyDebn <version>, out today, <what it brings, in one sentence>. OhMyDebn is a debonair Linux desktop for power users: the stability of Debian or Ubuntu, the ease of use of the Cinnamon desktop, and the power of AI, containers and virtualization. It installs on <the supported distros, as installation.md lists them>.

New in this release:

- <Each New and Improvements item, in one or two sentences, with its menu path or hotkey.>
- Fixes: <the fixes users will notice, in one line>.
- Updated components: <names and versions, as the release notes list them>.

Already running OhMyDebn? Run ohmydebn-update. New here? Start at https://ohmydebn.org

Release notes: https://ohmydebn.org/release-notes/#<version without dots>

## Video description (alt text, for Mastodon and Bluesky)

A <length>-second look at OhMyDebn <version>, with captions and no sound. <Each scene in order: what's on screen, and what the caption says where it matters. Name colors and visible text; skip transitions.> It closes on OhMyDebn <short version> and ohmydebn.org.
