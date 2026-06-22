
# 5-checklist-command_line_sanity.md.md

This version of `5-checklist-command_line_sanity.md` reflects the steps I am performing to install **Ubuntu 26.04** on `[hostname]` on **2026-05-??**.


# Basic Command Line Functionality

These steps help us to finish acheiving what I like to call *"Sanity"*.

Overview:

- 1. Clone the `jmws_accoutrements` Repo
- 1. Populate `~/bin`
- 1. Keyboard Shortcuts
- 1. Konsole Sanity

## Github; Clone the `jmws_accoutrements` Repo

- [X] Update ssh key for `ava` on github.com
  - [X] Access User Menu [photo in upper right corner] -> Settings -> Access -> SSH and GPG keys
    - [X] Add the new ssh key, that was created in `4-checklist-bare_bones_essentials.md`, with the title "*ava-ubuntu-26.04*"
    - [X] Delete the old ssh key for `ava`
- [X] Make a subdirectory in `/var` named `/var/www` and change the owner of it to `tomh`:
  - [X] As the `root` user run: `cd /var; mkdir www; chown tomh:tomh www`
- [X] Clone the `jmws_accoutrements` repo:
  - [X] As the user `tomh` run: `cd /var/www; git clone [ssh url from github for the repository]`
    - We probably want to run `git clone git@github.com:tomwhartung/jmws_accoutrements.git`, but check github to be sure

## Populate `~/bin`

Hopefully `~/bin` was populated from files on the thumb drive.

If however we forgot to put them on there, then once ssh is working, push the files in `~/bin` from one of the other
linux hosts over to the newly-upgraded host.

## Keyboard Shortcuts

Define these in the Settings app:

- [X] Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Launchers
  - [X] Ctrl-Alt-C: Launch **C**alculator
  - [X] Ctrl-Alt-F: Launch web browser (**F**irefox)
  - [X] Ctrl-Alt-S: **S**ettings
- [X] Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Custom shortcuts [At bottom of list]
  - [X] Ctrl-Alt-K: **K**onsole - `/usr/bin/konsole`

## Konsole Sanity

Konsole -> [Hamburger] Menu -> More ... -> Settings -> Manage Profiles

1. Create a new profile so we can update some options:
- [X] Profiles page -> "+ New" Button
- [X] General page -> General Settings tab
  - [X] [Fill in a name:] tomh
  - [X] [Check the box:] Default profile
  - [X] [Verify Command:] `/bin/bash`
  - [X] [Terminal bell mode:] Ignore Bell Events
- [X] Click "OK" button at bottom of page to close General page dialog

2. Fix mouse click-and-drag word delimiters
- [X] Konsole window Hamburger Menu -> Edit Current Profile ...
- [X] Mouse page -> Text interaction tab
  - [X] Word characters: "_" [I.e., Underline character *only*]
  - [X] Click "OK" button at bottom of page to close Mouse page dialog
- [X] Click "OK" button at bottom of page to close Configure dialog box
- [X] Test mouse double-click select setting
  - [X] Close all konsole windows and tabs - to ensure we are using the new settings
  - [X] Open a new konsole window
  - [X] Go to any directory with more than one level, e.g., `/art/music/songs/mp3`
  - [X] Double-click on a word in the directory name to test the click-and-drag select setting

3. Adjust font size
- [X] Konsole window Hamburger Menu -> Edit Current Profile ...
- [X] Appearance page -> Color scheme & font tab
  - [X] Find the "Font:" row near the bottom of the page
  - [X] Click Choose...
  - [X] Change the Size to "9", or whatever works
- [X] Click "OK" button at the bottom of the dialog box to close it
- [X] Click "OK" button at the bottom of the page to close the Edit Profile dialog box

## Konsole Sanity - Moving Tabs to the Left and Right

Konsole -> [Hamburger] Menu -> Settings -> Configure Keyboard Shortcuts

- [X] Move tab to the left
  - [X] Click on Ctrl+Alt+Left -> If a dialog box appears asking for permission to change this, Click on Allow
  - [X] Click on Ctrl+Alt+Left -> Click on Custom -> Click on None -> Press Shift+Ctrl+Left arrow -> Click on Reassign
- [X] Move tab to the right
  - [X] Click on Ctrl+Alt+Right -> Click on Custom -> Click on None -> Press Shift+Ctrl+Right arrow -> Click on Reassign
- [X] Click on OK to close the dialog box
- [X] Test moving the current tab to the left by pressing Shift+Ctrl+Left Arrow
- [X] Test moving the current tab to the right by pressing Shift+Ctrl+Right Arrow

