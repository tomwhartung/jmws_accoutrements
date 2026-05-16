
# 7-checklist-optional_apps.md

This version of `7-checklist-optional_apps.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Optional Apps

Checklists for installing apps that we want on a limited number of hosts.

- **Be sure to make a note in the in the file for that host of whether we install the debian package or the snap version**
  - In particular, make a note of any reasons for picking one over the other, for possible future reference

## Contemplating Chromium

I am thinking seriously about installing `chromium` on all 26.04 hosts.

- [ ] `chrome` - or `chromium`?
  - **Note** that so far we have not installed Chrome yet on `barbara`, `bette`, or `martha`
  - We will eventually want to install it on `jane` and `ava` - and maybe `martha` (and others) later
  - Chrome is nice to have, but remember: **it is a pain to keep it update-to-date on ubuntu** because we have to do it manually.
  - Maybe if we install **chromium** (as a snap) instead of chrome it will be less of a pain to keep it update-to-date??
  - [ ] If we install chrome, set up a shortcut for it:
    - [ ] Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Custom shortcuts [At bottom of list]
      - Ctrl-Alt-C: Chrome

## Music Apps: `ava` and `barbara`

For now, install these on `ava` and `barbara` -- and optionally maybe eventually install them on `jane`.

- [ ] Clementine
  - [ ] Details TBD
- [ ] Strawberry
  - [ ] Details TBD

## Audio-Visual Apps: `martha` and `bette`

For now, install these on `martha` and `bette` -- and optionally maybe eventually install them on `ava` or `jane`.

Idea for A/V apps:

- Note that `bette` [2011] is the oldest Linux host on the LAN and `martha` [2023] is the youngest
- Install the snap package version on `martha`
  - Mnemonic: it's a newer computer, so use the newer method
- Install the deb package version on `bette`
  - Mnemonic: it's an older computer, so use the older method

Decide which method I like better.

### Checklist

- [ ] VLC
  - Debian version [in 25.10] doesn't have an icon, wtf?
  - [ ] Install the snap package version on `martha`
  - [ ] Install the debian package version on `bette`
- [ ] OBS
  - [ ] Install the snap package version on `martha`
  - [ ] Install the debian package version on `bette`
- [ ] Audacity
  - [ ] Install the snap package version on `martha`
  - [ ] Install the debian package version on `bette`

## Tracktion

Download the Tracktion Download Manager from [tracktion.com](tracktion.com) and use that to install the app.

## Other Optional, Nice-to-Have Apps

- [ ] TBD

