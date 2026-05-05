
# 5-checklist-command_line_sanity.md.md

This version of `5-checklist-command_line_sanity.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Basic Command Line Functionality

These steps help us to finish acheiving what I like to call *"Sanity"*.

## Github; Clone the `jmws_accoutrements` Repo

- [ ] Update ssh key for *[hostname]* on github.com
  - [ ] Access User Menu [photo in upper right corner] -> Settings -> Access -> SSH and GPG keys
    - [ ] Delete the old ssh key for *[hostname]*
    - [ ] Add the new ssh key, that was created above, as `*[hostname]*-ubuntu-25.10`
- [ ] Make a subdirectory in `/var` named `/var/www` and change the owner of it to `tomh`:
  - [ ] As the `root` user run: `cd /var; mkdir www; chown tomh:tomh www`
- [ ] Clone the `jmws_accoutrements` repo:
  - [ ] As the `tomh` user run: `cd /var/www; git clone [ssh url from github for the repository]`
    - We probably want to run `git clone git@github.com:tomwhartung/jmws_accoutrements.git`, but check github to be sure

## Populate `~/bin`

Hopefully `~/bin` was populated from files on the thumb drive.

If however we forgot to put them on there, then once ssh is working, push the files in `~/bin` from one of the other
linux hosts over to the newly-upgraded host.

## Keyboard Shortcuts

Define these in the Settings app:

- [ ] Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Launchers
  - [ ] Ctrl-Alt-M: Launch calculator (for **M**ath)
  - [ ] Ctrl-Alt-F: Launch web browser (**F**irefox)
  - [ ] Ctrl-Alt-S: **S**ettings
- [ ] Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Custom shortcuts [At bottom of list]
  - [ ] Ctrl-Alt-K: **K**onsole - `/usr/bin/konsole`

## Konsole Sanity

Konsole -> [Hamburger] Menu -> Settings -> Configure Konsole

1. Create a new profile so we can update some options:
- [ ] Profiles page -> "+ New" Button
- [ ] General page -> General Settings tab
  - [ ] [Fill in a name:] tomh
  - [ ] [Check the box:] Default profile
  - [ ] [Verify Command:] `/bin/bash`
  - [ ] [Terminal bell mode:] Ignore Bell Events
- [ ] Click "OK" button at bottom of page to close General page dialog

2. Fix mouse click-and-drag word delimiters
- [ ] Konsole window Hamburger Menu -> Edit Current Profile ...
- [ ] Mouse page -> Text interaction tab
  - [ ] Word characters: "_" [I.e., Underline character *only*]
  - [ ] Click "OK" button at bottom of page to close Mouse page dialog
- [ ] Click "OK" button at bottom of page to close Configure dialog box
- [ ] Test mouse double-click select setting
  - [ ] Close all konsole windows and tabs - to ensure we are using the new settings
  - [ ] Open a new konsole window
  - [ ] Go to any directory with more than one level, e.g., `/art/music/songs/mp3`
  - [ ] Double-click on a word in the directory name to test the click-and-drag select setting

3. Adjust font size
- [ ] Konsole window Hamburger Menu -> Edit Current Profile ...
- [ ] Appearance page -> Color scheme & font tab
  - [ ] Find the "Font:" row near the bottom of the page
  - [ ] Click Choose...
  - [ ] Change the Size to "9", or whatever works
- [ ] Click "OK" button at the bottom of the dialog box to close it
- [ ] Click "OK" button at the bottom of the page to close the Edit Profile dialog box


