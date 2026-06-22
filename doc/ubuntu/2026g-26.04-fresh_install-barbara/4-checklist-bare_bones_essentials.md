
# 4-checklist-bare_bones_essentials.md

This version of `4-checklist-bare_bones_essentials.md` reflects the steps I am performing to install **Ubuntu 26.04** on `barbara` on **2026-05-30**.


# Recap: PROBLEMS With Installing 26.04

Because HP has **retired** this PC **we were unable to install Ubuntu 26.04 from scratch!**

- *Bummer!*
- However, we were able to upgrade the OS using the `do-release-upgrade` command

For details about all this, see these files in this directory:

- `3a-checklist-installation.md`
- `3b-checklist-installation-PROBLEMS.md`
- `3c-do_release_upgrade-output.txt`

Because we did ran `do-release-upgrade` instead of installing Ubuntu 26.04 from scratch, **running many of the steps in this checklist is unnecessary.**

- *However,* this did result in **one rather serious issue!**

For details, see the section *Yikes!  The App Center Doesn't Work!!* below


# Bare Bones Essentials Common to All Hosts

These are the first steps to acheiving what I call *"Sanity"*.

Overview:

- 1. First Boot - booting into the install for the first time
- 1. Add the **Terminal** and **Settings** Apps to the Dock
- 1. Get the Network Running With the Static IP Address
- 1. Install Essential Packages
- 1. Update Essential Files From Previous Install
- 1. Set Essential Keyboard Shortcuts
- 1. Essential Networking - `ssh`

## First Boot

Booting into 26.04 the first time we are prompted to make the following decisions:

- [X] Location Services - Turn on
  - "*You can change this later in the Settings app*"
- [X] Help Improve Ubuntu
  - [X] Share system data with the Ubuntu team - Turn on
  - [X] Share error reports with the Ubuntu team - Turn on
- [X] Choose how Ubuntu looks
  - Style - Default
  - Accent Color - Defaults to Orange
- [X] Finish

## Opened the **Strawberry** App

And now it's doing a rescan of the entire collection.

The columns were out of order, so I had to fix that.

Got it to play a song, so at least it still works!

## Verified `barbara` Is Running 26.04

These commands come from
[https://linuxize.com/post/how-to-upgrade-to-ubuntu-26-04/](https://linuxize.com/post/how-to-upgrade-to-ubuntu-26-04/).

```
tomh@barbara: ~
 $ uname -r
7.0.0-22-generic
tomh@barbara: ~
 $ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 26.04 LTS
Release:        26.04
Codename:       resolute
tomh@barbara: ~
 $
```

## Yikes!  The App Center Doesn't Work!!

Trying to run the App Center causes it to start up, then fail.  Rats!!

- This is more-than-likely due of course to the BIOS issue caused by HP "retiring" this PC

As long as we can play music on this PC, I guess we are ok.

## Add the **Terminal** and **Settings** Apps to the Dock

- [X] **All of this looks good after the upgrade!**

Here we demonstrate two ways to pin an app to the doc.

First, the **Terminal** app:

- [N/A] Click on the **Apps** icon in the lower left corner
- [N/A] Right-click on the icon for the **Terminal** app and select **Pin to Dock**
- [N/A] Press the **Esc** key
- [N/A] Right-click on the icon for the **Terminal** app *in the dock* and move it to the **Top of the Dock**

Second, the **Settings** app:

- [N/A] Left-click on the **Apps** icon in the lower left corner
- [N/A] Left-click on the icon for the **Settings** app to launch it
- [N/A] Right-click on the icon for the **Settings** app *in the dock* select **Pin to Dock**
- [N/A] Press the **Esc** key
- [N/A] Left-click on the icon for the **Settings** app *in the dock* and move it to the **Top of the Dock**

## Get the Network Running With the Static IP Address

- [X] **All of this looks good after the upgrade!**

- [X] Open a **Terminal** window and try running:
  - `ping google.com`
  - If it works, great!  But don't be surprised if it doesn't.
  - We are going to need to set a **static IP address**, so might as well do it now.
- [X] Open the **Settings** app and use the values saved in `2-checklist-preparation_part_2.md` to set up *static IP*
  - [X] Settings -> Network -> Wired section -> [Gear Icon]
    - [X] Details tab: Connect automatically
    - [X] Identity tab
       - Name: "Static wired quantum fiber via asus"
       - MTU: Automatic
    - [X] IPv4 tab:
      - [X] IPv4 Method section: Manual
      - [X] Addresses section: Address: 10.0.1.117; Netmask: 255.255.255.0; Gateway: 10.0.1.2
      - [X] DNS section: 192.168.0.1,205.171.2.25
    - [X] Security tab:
      - Authentication: MD5
- [X] Go back to the **Terminal** window opened previously and try running the `ping` command again:
  - `ping google.com`
  - **If it doesn't work, review the settings entered and figure out why!  This is super-important, so good luck!!**

## Install Essential Packages

- [X] **All of this looks good after the upgrade!**

- [X] Use the Command Line or the Software Updater to update the installed packages to their latest versions
  - [X] Using the Command Line:
    - [X] Open a terminal window and run `sudo su -` so we can run additional install commands as root
    - [X] Run `apt-get update` to identify the updated versions that apt can install
    - [X] Run `apt-get upgrade -y` to download and install these updated versions
  - [N/A] Using the Software Updater: *(TBD)*
     **TBD: This is probably what I will want to show people in the video**
    - [N/A] Pin the Software Updater to the dock
    - [N/A] Run the Software Updater to install updates made since 25.10 was released
- [N/A] If not already done, open a terminal window and run `sudo su -` so we can run additional install commands as root
- [N/A] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`
- [N/A] Open the **Apps** screen, run the **Konsole** app - or *pin it to the dock* and run it from there
- [N/A] Right-click on the icon for the **Konsole** app *in the dock* and move it to between the *Settings* and *Terminal* apps
- [N/A] It may be a good idea to reboot the system at this time, *however*
  - It's ok to wait and reboot after going through the steps in the next section
  - *Note* that we will *need* to reboot after updating these files, to take advantage of them being present at boot

## Update Essential Files From Previous Install

- [X] **All of this looks good after the upgrade!**

Find old files on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

- [N/A] Files in `/home/tomh`
  - [N/A] Open a konsole window
  - [N/A] Check the installed version of `.bashrc` into RCS:
    - [N/A] Run the following commands:
      - `cd`
      - `mkdir RCS`
      - `ci -l .bashrc`     # add the *not-a-log* message *"Installed version."*
  - [N/A] Move (or copy) the `.bashrc` and `.bash_aliases*` files from `/home/tomh` on the thumb drive to `/home/tomh`
  - [N/A] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [N/A] `rcsdiff .bashrc`       # only CusTOMizations should show up
    - [N/A] This is a good time to clean up any CusTOMizations that are no longer relevant and hence obsolete
  - [N/A] Move (or copy) the rest of the files from `/home/tomh` on the thumb drive to `/home/tomh`
    - `.vimrc .gitconfig`
    - `d.e r*`
    - `.ssh/` - Use `mv` or `cp -r`
  - [N/A] Set background to one of the files in `~/Pictures`
    - Settings -> Appearance -> Background -> + Add Picture
- [N/A] Files in `/root`
  - [N/A] Open a konsole window and run `sudo su -` so we can **run these commands as root**
  - [N/A] Check in the installed version of `.bashrc`:
    - [N/A] Run the following commands:
      - `cd`
      - `mkdir RCS`
      - `ci -l .bashrc`     # add the *not-a-log* message *"Installed version."*
    - [N/A] Move (or copy) the `.bashrc` file from `/root` on the thumb drive to add the CusTOMizations
  - [N/A] Link the following files from `~tomh` to `/root`:
    - [N/A] `ln -s ~tomh/.bash_aliases .`
    - [N/A] `ln -s ~tomh/.bash_aliases-* .`
    - [N/A] `ln -s ~tomh/.vimrc .`
    - [N/A] `ln -s ~tomh/bin .`        # NOTE: these must be copied over before we can link to them
- [N/A] Files in `/etc`
  - [N/A] Open a konsole window and run `sudo su -` so we can run commands as root
  - [N/A] Check the installed versions of `/etc/fstab` and `/etc/hosts` into RCS
    - [N/A] Run the following commands:
      - `cd /etc`
      - `mkdir RCS`
      - `ci -l fstab hosts`  # "Installed version."
  - [N/A] Add **only the CusTOMizations** from the version of `fstab` on the thumb drive to the installed version of `fstab`
  - [N/A] Add **only the CusTOMizations** from the version of `hosts` on the thumb drive to the installed version of `hosts`
  - [N/A] **Be sure to plug in any external disks referenced in the CusTOMizations added to `fstab`**
- [N/A] *Definitely* reboot the system at this time
  - If the PC doesn't boot, it's probably because the disks referenced in the CusTOMizations added to `/etc/fstab` are not plugged in

## Set Essential Keyboard Shortcuts

- [X] ** *Almost* all of this looks good after the upgrade!**
- [X] See below for the ones I had to redo

In reality I use these all the time and quickly go crazy without them.

- [N/A] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts -> View and Customize Shorcuts
  - Navigation
    - [N/A] Ctl+Alt+[Left Arrow] - Move window one workspace to the left
    - [N/A] Ctl+Alt+[Right Arrow] - Move window one workspace to the right
    - [N/A] Alt+F1 - Switch to Workspace 1
    - [N/A] Alt+F2 - Switch to Workspace 2
    - [N/A] Alt+F3 - Switch to Workspace 3
    - [N/A] Alt+F4 - Switch to Workspace 4
    - [N/A] Alt+[Left Arrow] - Switch to workspace on the left
    - [N/A] Alt+[Right Arrow] - Switch to workspace on the right

## Essential Networking - `ssh`

- [X] **All of this looks good after the upgrade!**

- [X] Get ssh working
  - [N/A] Copy old `~/.ssh` directory into the new `/home/tomh` directory
    - In particular, we need the old `authorized_keys` file
    - Having the `pubs` subdirectory can help, if we have a problem someday
  - [X] Run `ssh-keygen` to generate new keys
    - When prompted for a file name or passphrase, just press Enter to accept the default values
  - [X] Ensure the permissions on the private key `~/.ssh/id_ed25519` are 0600
    - `ls -l ~/.ssh/id_ed25519`       # should be -rw------- NOT -rw-r--r--
    - `chmod 600 ~/.ssh/id_ed25519`
    - `ls -l ~/.ssh/id_ed25519`
    - These somehow got changed to 644 on `martha`, which caused an ugly error, until I actually read the message and fixed the perms; weird!
  - [X] Copy `~/.ssh/id_ed25519.pub` to `~/.ssh/id_ed25519.pub-[hostname]`
  - [X] Copy the file `~/.ssh/id_ed25519.pub-[hostname]` to a thumb drive so we can copy it to all other linux hosts
  - [X] Move (`mv ...`) the file `~/.ssh/id_ed25519.pub-[hostname]` to the `pubs/` subdirectory for possible future reference
  - [X] Update `~/.ssh/authorized_keys` on all linux hosts, replacing old public key for [hostname] with the new one
    - *Else you will be asked for a password*
  - [X] Remove `.ssh/known_hosts` file from all other hosts
    - *Else you will get a nasty error message*
  - [X] Log in to each host from each host, to make a new `known_hosts` file on each one and ensure they all work

