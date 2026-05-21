
# 7-checklist-standard_apps.md

This version of `7-checklist-standard_apps.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Standard Apps - General Notes

This file contains checklists to use when installing apps that we want on all - or at least most - linux hosts.

## "*All*" Hosts Really Means "*Most*" Hosts

By default, "*all*" hosts implies to *just four* of them: `ava`, `barbara`, `jane`, and `martha`.

- Note that `bette` is the oldest of this group [2011], and her wireless connection is *painstakingly slow*
  - This slow connection makes it impractical to keep all of the `/art/*` files up-to-date on the host
  - As a laptop, she is also portable, and connecting an external disk would just interfere with her portablity

Therefore, **if we install any of these apps on `bette`, we will note that specifically in the section containing the checklist**

## Using the App Center

Although I am used to using the command line to install packages - and still use it on occasion - it's really easy to use the App Center app to install these.

- [X] Move the icon to run the App Center to the top of the Dock

Additionally, using the App Center makes it easy to see which apps are available as snaps, or debian packages, or both.
At this time, I am not sure which to prefer, so *it's good to know when we have a choice.*

## Setting up Keyboard Shortcuts

Let's put off creating shortcuts until we have most of these apps installed, and then do them all at once.

## Snaps Versus Debian Packages

For packages that are available as both snaps and debian packages, let's compare these two installation methods by using both of them.

### Default Installation Preference

When we have a choice of installing either the snap or the debian package, follow this guideline:

- Install snaps on `barbara` and `martha`
- Install debian packages on `ava` and `jane`

Because installing these apps on `bette` is optional, we can make a case-by-case decision as to which one to use when we decide to install the app.

### Important Considerations

- If we want to break from following the guideline above, that's fine
- Regardless, be sure to make a note in the section for the checklist in the file for that host of whether we install the snap or the debian package version
  - This is especially true when we are installing one or more of these apps on `bette`, because doing so is optional
- When deviating from the "*Default Installation Preference*" given above, make a note of any reasons for picking one over the other, for possible future reference


# Standard Apps - The Apps

## Chromium

Chrome is nice to have, but remember: **it is a pain to keep it update-to-date on ubuntu** because we have to do it manually.

- Let's try installing just Chromium, and install Chrome only if it turns out we need it fir some reason
- At this time, Chromium is *not avaiable for installation as a debian package*
- [X] Use the App Center to install Chromium as a snap

Apparently Chromium doesn't allow me to log in, making Chrome and Firefox much more worthwhile.

## Music Apps

Currently we are planning to use these mostly on `barbara` and possibly some on `ava`, because they are hooked up to the main stereo system.

We will probably not use these much on `jane` and `martha`, but it's easy to install them and they will have copies of all the mp3 files, so why not?
I can see how they might be useful at some point!

### Set up Rhythmbox, and Install and Set up Clementine and Strawberry

- [X] In a Konsole window, run these commands as `tomh`:
  - `cd ~/Music`
  - `ll `
  - `mkdir rhythmbox`      # if it is not already there
  - `mkdir clementine`     # if it is not already there
  - `mkdir strawberry`     # if it is not already there
- [X] These directories, and any others under `~/Music`, should be empty
- [X] Double check and **ensure there are *no* files or directories in or linked to *any* subdirectories of `~/Music`**

- [X] Run the App Center
- [X] Click on the **Manage** option and install any updates that may be pending
- [X] Install Clementine as a snap
  - [X] Pin the icon to run Clementine to the Dock
    - I tried installing Clementine as a snap, and when I ran it, set the library to `~/Music/clementine`, and told it to scan the entire collection
    - I do not know why this happened, hmmm...
    - However, after seeing the message that the Strawberry snap install displayed (see below), I uninstalled the snap and reinstalled it as a debian package
- [X] Install Strawberry as a **debian package**
    - I tried installing Strawberry as a snap, and when I ran it, it displayed a long message saying it's best to install the debian package
    - *Now why, if it's best to install the debian package, do they even allow it to be installed as a snap?*
      - We wont worry about that, just install it as a debian package
  - [X] Pin the icon to run Strawberry to the Dock

- [X] In a Konsole window, run these commands as `tomh`:
  - `cd ~/Music`
  - `ll `
  - `ll *`
- [X] Triple check and **ensure there are *no* files or directories in or linked to *any* subdirectories of `~/Music`**

At this point, it is safe to start up the apps and set the app-specific directories that will contain the files we want to listen to.

- [X] Use the Rhythmbox icon in the Dock to run it
  - [X] Click on the hamburger menu icon then click on Preferences
  - [X] Under the Music tab, set the Library Location to file:///home/tomh/Music/rhythmbox
  - [X] Under the Music tab, under Library Structure, set the Preferred format to - "*MPEG Layer 3 Audio*"
  - [X] Click on Close to close the dialog
- [X] Use the Clementine icon in the Dock to run it
  - [X] Click on the Tools menu option then click on Preferences
  - [X] In the General section, click on the Music Library menu option
  - [X] In the Music Library section, click on the *Add new folder* button and add the /home/tomh/Music/clementine directory
  - [X] Click on OK to close the dialog
- [X] Use the Strawberry icon in the Dock to run it
  - [X] Click on the Tools menu option then click on Settings
  - [X] In the General section, click on the Collection menu option
  - [X] At the top of the Collection page, click on the *Add new folder* button and add the /home/tomh/Music/strawberry directory
  - [X] Click on OK to close the dialog

At this point, the music libraries in the Rhythmbox, Clementine, and Strawberry apps should be empty!

### Create Links to Files in `/art`

- [X] Ensure that `/etc/fstab` is updated so that the external disks containing `/art` and `FATART` files automatically mount when the PC boots
  - For details, see the `4-checklist-bare_bones_essentials.md` checklist in this directory
- [X] Ensure that the `/art/videos` directory has been renamed to `/art/av`
  - For details, see the `6-checklist-rename_art_videos_dir.md` checklist in this directory
- [X] Open a Konsole window and run `sudo su -`
  - [X] In this window, run these commands as `root`:
    - `cd /`
    - `mkdir art`
    - `chown tomh:tomh art`
- [X] In a different Konsole window, run these commands as `tomh`:
  - `cd /art ; ll `
  - `ll /mnt/disks/art/art`       # this should show the `art` subdirectories, `av`, `books`, `classes`, `classes-jane`, `images`, `music`, and `podcasts`
  - `ln -s /mnt/disks/art/art/* .`
  - `ll `
  - `gogd ; ll `        # this should show my collection of Grateful Dead music

At this point, all art files - videos, images including photos, music, etc. should be available under `/art`.
This should be a no-brainer, but if something is missing somehow, fix it now!

### Run Rhythmbox, Clementine, and Strawberry

Note that the music libraries in the Rhythmbox, Clementine, and Strawberry apps should still be empty!

The next step is to start up the apps and link the files we will want to listen to into each of the app-specific directories.

- [X] Add music files to Rhythmbox's library
  - [X] In a Konsole window, run these commands as `tomh`:
    - `cd ~/Music/rhythmbox/`
    - `ll /art/music/songs/mp3`      # this should show the bands in my personal collection of mp3s
    - `ln -s /art/music/songs/mp3 .`
  - [X] Allow Rhythmbox to process all these mp3 files
    - Rhythmbox shows 27263 total songs in 1874 total albums by 414 total artists

- [X] Add music files to Clementine's library
  - [X] In a Konsole window, run these commands as `tomh`:
    - `cd ~/Music/clementine/`
    - `ll /art/music/songs/mp3`      # this should show the bands in my personal collection of mp3s
    - `ln -s /art/music/songs/mp3 .`
  - [X] Ensure that the totals displayed by Rhythmbox are not changing!
  - [X] Click on the Tools menu option then click on Do a full library rescan
    - As the scan progresses, watch the percentage displayed in the bottom margin of the app's window
  - [X] Allow Clementine to process all these mp3 files
    - Clementine shows 27286 total songs, but the total number of albums and artists is unknown

- [ ] Add music files to Strawberry's library
  - [X] In a Konsole window, run these commands as `tomh`:
    - `cd ~/Music/strawberry/`
    - `ll /art/music/songs/mp3`      # this should show the bands in my personal collection of mp3s
    - `ln -s /art/music/songs/mp3 .`
  - [X] Ensure that the totals displayed by Rhythmbox are not changing!
  - [X] Click on the Tools menu option then click on Do a full library rescan
    - As the scan progresses, watch the percentage displayed in the bottom margin of the app's window
  - [X] Allow Strawberry to process all these mp3 files
    - Verify that Strawberry shows 27284 total songs

### Test Rhythmbox, Clementine, and Strawberry

- [X] Test Rythmbox
  - [X] Try to play a song from 30 Days of Dead
  - [X] Fix any issues
  - [X] Don't worry about setting any preferences in additon to the library location at this time

- [ ] Test Clementine
  - [ ] Try to play a song from 30 Days of Dead
  - [ ] Fix any issues
  - [ ] Don't worry about setting any preferences in additon to the library location at this time

- [X] Test Strawberry
  - [X] Try to play a song from 30 Days of Dead
  - [X] Fix any issues
  - [X] Fine-tune Strawberry's settings as described in the next section

### Fine-tune Strawberry's Settings

Following are some important Settings we want to set in Strawberry:

#### General Settings

- [X] Behavior Page
  - [X] Using the menu to add a song will... - Never start playing
  - [X] Pressing "Previous" in player will... - Restart song, then jump to previous if pressed again
  - [X] Double clicking a song will... - Add to the queue and Play if there is nothing already playing
  - [X] Double clicking a song in the playlist will... - Add to the queue
- [X] Collection Page
  - [X] Collection: /home/tomh/Music/Strawberry
  - [X] Perform song EBU R 128 analysys ...
  - [X] Expire unavailable songs after 1 days
- [X] Backend Page
  - [X] Audio Normalization Section
    - [X] EBU R 128 Loudness Normalization -> Perform track loudness normaliztion - Check this option
- [X] Playlist Page
  - [X] Enable delete files in the right click context menu
  - [X] When saving a playlist, file paths should be - Absolute
- [X] Scrobbler Page
  - [X] Defaults are ok
- [X] Covers Page
  - [X] Saving album covers - Save album cuvers in album directory
- [X] Lyrics Page
  - [X] Defaults are ok
- [X] Transcoding Page
  - [X] Defaults are ok
- [X] Network Proxy Page
  - [X] Defaults are ok

#### User Interface Settings

- [X] Appearance Page
  - [X] Style Section
    - [X] Style - Fusion
  - [X] Tabbar colors Section
    - [X] Select tabbar color: - dark red works well
  - [X] Background image Section
    - [X] A Taste of Strawbs
- [X] Context Page
  - [X] Defaults are ok
- [X] Notifications Page
  - [X] Notification type - Disabled
- [X] Global Shortcuts Page
  - [X] None (Default) at this time
- [X] Moodbar Page
  - [X] Enabled
  - [X] Show a moodbar in the track progress bar
  - [X] Moodbar style: Happy

#### Streaming Settings

- [X] Defaults are ok

#### Columns

The columns are tedious to adjust, but after some time I've learned this is how I like them:

- 1. Artist
- 1. Album
- 1. Disk Number
- 1. Track Number
- 1. Title
- 1. Length
- 1. Play Count
- 1. Last Played

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

