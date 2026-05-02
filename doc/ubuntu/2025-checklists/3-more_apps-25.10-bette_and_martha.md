
# 2025-checklists/3-more_apps-25.10-bette_and_martha.md

# More Apps

## Debian Installs or Snaps?

The producer of Ubuntu, Canonical, supports two ways of downloading and updating software packages:

o The traditional way, using debian packages:
  o [https://en.wikipedia.org/wiki/Deb_(file_format)](https://en.wikipedia.org/wiki/Deb_(file_format))
o Canonical's new way, using snap packages:
  o [https://en.wikipedia.org/wiki/Snap_(software)](https://en.wikipedia.org/wiki/Snap_(software))

For a comparison of the two, see [snapcraft.io/blog/a-technical-comparison-between-snaps-and-debs](https://snapcraft.io/blog/a-technical-comparison-between-snaps-and-debs)

For a list of differences, see the **Summary of differences** at the end of this page:
[snapcraft.io/blog/a-technical-comparison-between-snaps-and-debs](https://snapcraft.io/blog/a-technical-comparison-between-snaps-and-debs)

### Which Version to Use, Debian or Snaps?

- I kind of lean towards debian packages:
  - It feels safer
  - It uses less disk space because dependencies are shared
- But it seems like Canonical wants us to use snaps:
  - It seems to be more *"bleeding edge"*
  - It looks to be more flexible
  - It uses less disk space because dependencies are shared

Let's try out some of each, and take notes about the results, with an eye towards being able to recommend one or the other in certain circumstances.

At this point, I would say:

- It feels like debian packages are better for users who want a more mature, reliable software update system
- It feels like snaps are better for software developers who want to experiment and be able to control multiple versions of some packages

### Notes Concerning Debian vs. Snaps

Use this section to record some of my observations while I experiment with snaps vs. debian packages.

- Firefox is available via snaps *only*
- On 2026-04-02 I was using the *Manage* option in the *App Center* to try to update Firefox, and got this message:
  - *"Something went wrong."*
    - *"We're sorry, but we're not sure what the error is"*
    - *"OK"* button
  - -> Rebooting seems to have fixed the issue
  - **This sort of thing makes me feel like snaps are kinda flakey**


## Audio-Visual Apps

For now, install these on `bette` and `martha` -- and optionally maybe eventually install them on `ava` or `jane`.

When both snap and debian packages are available:

- Install the snap package version on `martha`
  - Mnemonic: it's a newer computer, so use the newer method
- Install the deb package version on `bette`
  - Mnemonic: it's an older computer, so use the  older method

Decide which method I like better.

### Checklist

- [X] VLC
  - Debian version doesn't have an icon, wtf?
  - [X] Install the snap package version on `martha`
  - [X] Install the debian package version on `bette`
- [X] OBS
  - [X] Install the snap package version on `martha`
  - [X] Install the debian package version on `bette`
- [X] Audacity
  - [X] Install the snap package version on `martha`
  - [X] Install the debian package version on `bette`

## Tracktion

Download the Tracktion Download Manager from [tracktion.com](tracktion.com) and use that to install the app.


## Optional, Nice-to-Have Apps

- `chrome`
  - **Note** that so far we have not installed Chrome yet on `barbara`, `bette`, or `martha`
  - We will eventually want to install it on `jane` and `ava` - and maybe `martha` (and others) later
  - Chrome is nice to have, but remember: **it is a pain to keep it update-to-date on ubuntu** because we have to do it manually.
  - If we install chrome, set up a shortcut for it:
    - Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Custom shortcuts [At bottom of list]
      - Ctrl-Alt-C: Chrome

