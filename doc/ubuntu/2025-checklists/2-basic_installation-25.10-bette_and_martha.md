
# 2025-checklists/2-installation-25.10-all_linux_hosts.md

# Installing Ubuntu 25.10

Much of this is quite straightforward, answering several easy no-brainer questions that do not require further comment.

## Running the Install

Following is a list of steps, for future reference, even when it's simple, but has been a while since the last time I did this:

Suggestion: *copy and paste this checklist into the file we are using to log what I do during the installation.*

- [ ] Use the USB drive to boot the PC
  - [ ] May need to mess with the BIOS to get it to boot from the USB drive
- [ ] Running the install **on [note the date and time here]**
  - [ ] Answer easy no-brainer questions
  - [ ] Start with **Extended Selection**
  - [ ] Yes **Install recommended proprietary software**
  - [ ] **Erase disk and install Ubuntu**
     - Dual-boot installs were cool back in the day, but I do not see myself wanting to do those any longer
  - [ ] **No encryption**
  - [ ] **Create your account**:
    - [ ] My name, computer's name, my user id, password;
    - [ ] ** *Uncheck* Require my password to log in**
  - [ ] Install **started at [note the date and time here]** and **finished at [note the date and time here]**


# Bare Bones Essentials Common to All Hosts

Having these is also known as acheiving *"Sanity"*.

## Set Essential Keyboard Shortcuts

In reality I use these all the time and quickly go crazy without them.

- [ ] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts -> View and Customize Shorcuts
  - Navigation
    - [ ] Alt+[Left Arrow] - Switch to workspace on the left
    - [ ] Alt+[Right Arrow] - Switch to workspace on the right
    - [ ] Alt+F1 - Switch to Workspace 1
    - [ ] Alt+F2 - Switch to Workspace 2
    - [ ] Alt+F3 - Switch to Workspace 3
    - [ ] Alt+F4 - Switch to Workspace 4

## Install Essential Packages

- [ ] Use the Command Line or the Software Updater to update the installed packages to their latest versions
  - [ ] Using the Command Line:
    - [ ] Open a terminal window and run `sudo su -` so we can run additional install commands as root
    - [ ] Run `apt-get update` to identify the updated versions that apt can install
    - [ ] Run `apt-get upgrade` to download and install these updated versions
  - [ ] Using the Software Updater: *(TBD)*
     **TBD: This is probably what I will want to show people in the video**
    - [ ] Pin the Software Updater to the dock
    - [ ] Run the Software Updater to install updates made since 25.10 was released
- [ ] If not already done, open a terminal window and run `sudo su -` so we can run additional install commands as root
- [ ] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`

## Update Essential Files From Previous Install

Find old files on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

- [ ] Files in `/home/tomh`
  - [ ] Open a terminal window
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` and add the *not-a-log* message *"Installed version."*
  - [ ] Copy over all the files from `/home/tomh` on the `2023-32A` thumb drive
  - [ ] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [ ] `rcsdiff .bashrc`       # only CusTOMizations should show up
  - [ ] Set background to one of the files in `~/Pictures`
    - Settings -> Appearance -> Background -> + Add Picture
- [ ] Files in `/root`
  - [ ] Open a terminal window and run `sudo su -` so we can **run these commands as root**
  - [ ] Link the following files from `~tomh` to `/root`:
    - [ ] `ln -s ~tomh/.bash_aliases .`
    - [ ] `ln -s ~tomh/.bash_aliases-* .`
    - [ ] `ln -s ~tomh/.vimrc .`
    - [ ] `ln -s ~tomh/bin .`        # NOTE: these must be copied over before we can link to them
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` with the *not-a-log* message *"Installed version."*
    - [ ] Add the CusTOMizations from the `2023-32A` thumb drive
- [ ] Files in `/etc`
  - [ ] Open a terminal window and run `sudo su -` so we can run commands as root
  - [ ] Check in the installed versions: `cd /etc; ci -l fstab hosts # "Installed version."
  - [ ] Add CusTOMizations from versions on the `2023-32A` thumb drive

## Networking - `ssh`

- [ ] Get ssh working
  - [ ] Copy old `~/.ssh` directory into the new `/home/tomh` directory
    - In particular, we need the old `authorized_keys` file
    - Having the `pubs` subdirectory can help, if we have a problem someday
  - [ ] Run `ssh-keygen` to generate new keys
  - [ ] Copy `~/.ssh/id_ed25519.pub` to `~/.ssh/id_ed25519.pub-[hostname]`
  - [ ] Update `~/.ssh/authorized_keys` on all linux hosts, replacing old public key for [hostname] with the new one
    - *Else you will be asked for a password*
  - [ ] Remove `.ssh/known_hosts` file from all other hosts
    - *Else you will get a nasty error message*
  - [ ] Log in to each host from each host, to make a new `known_hosts` file on each one and ensure they all work

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

If however we forgot to put them on there, then once ssh is working, push the files in `~/bin` from one of the other linux hosts over to the newly-upgraded host.

## Keyboard Shortcuts

Define these in the Settings app:

- Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Launchers
  - Ctrl-Alt-M: Launch calculator (for **M**ath)
  - Ctrl-Alt-F: Launch web browser (**F**irefox)
  - Ctrl-Alt-S: **S**ettings
- Settings -> Keyboard -> Keyboard Shortcuts [At bottom of page] -> Custom shortcuts [At bottom of list]
  - Ctrl-Alt-K: **K**onsole - `/usr/bin/konsole`

## Konsole Sanity

Konsole -> [Hamburger] Menu -> Settings -> Configure Konsole

- 1. Create a new profile so we can update some options:
  - Profiles page -> "+ New" Button
  - General page -> General Settings tab
    - [Fill in a name:] tomh
    - [Check the box:] Default profile
    - [Verify Command:] `/bin/bash`
    - [Terminal bell mode:] Ignore Bell Events
  - Click "OK" button at bottom of page to close General page dialog
- 2. Fix mouse click-and-drag word delimiters
  - Konsole window Hamburger Menu -> Edit Current Profile ...
  - Mouse page -> Text interaction tab
    - Word characters: "_" [I.e., Underline character *only*]
    - Click "OK" button at bottom of page to close Mouse page dialog
  - Click "OK" button at bottom of page to close Configure dialog box
  - Test mouse double-click select setting
    - Close all konsole windows and tabs - to ensure we are using the new settings
    - Open a new konsole window
    - Go to any directory with more than one level, e.g., `/art/music/songs/mp3`
    - Double-click on a word in the directory name to test the click-and-drag select setting
- 3. Adjust font size
  - Konsole window Hamburger Menu -> Edit Current Profile ...
  - Appearance page -> Color scheme & font tab
    - Find the "Font:" row near the bottom of the page
    - Click Choose...
    - Change the Size to "9", or whatever works
  - Click "OK" button at the bottom of the dialog box to close it
  - Click "OK" button at the bottom of the page to close the Edit Profile dialog box


