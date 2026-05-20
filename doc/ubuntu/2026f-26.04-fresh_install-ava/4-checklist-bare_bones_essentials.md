
# 4-checklist-bare_bones_essentials.md

This version of `4-checklist-bare_bones_essentials.md` reflects the steps I am performing to install **Ubuntu 26.04** on `[hostname]` on **2026-05-??**.


# Bare Bones Essentials Common to All Hosts

These are the first steps to acheiving what I call *"Sanity"*.

Overview:

- 1. First Boot - booting into the install for the first time
- 1. Add the **Terminal** and **Settings** Apps to the Dock
- 1. Get the Network Running With the Static IP Address
- 1. Install Essential Packages
- 1. Update Essential Files From Previous Install
- 1. Set Essential Keyboard Shortcuts
- 1. Install Clementine and Set It and Rhythmbox up to Play My MP3s
  - Added because we are doing the install on `ava` and `barbara` before most of the others, and I like to listen to music while doing this work
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

## Add the **Terminal** and **Settings** Apps to the Dock

Here we demonstrate two ways to pin an app to the doc.

First, the **Terminal** app:

- [X] Click on the **Apps** icon in the lower left corner
- [X] Right-click on the icon for the **Terminal** app and select **Pin to Dock**
- [X] Press the **Esc** key
- [X] Right-click on the icon for the **Terminal** app *in the dock* and move it to the **Top of the Dock**

Second, the **Settings** app:

- [X] Left-click on the **Apps** icon in the lower left corner
- [X] Left-click on the icon for the **Settings** app to launch it
- [X] Right-click on the icon for the **Settings** app *in the dock* select **Pin to Dock**
- [X] Press the **Esc** key
- [X] Left-click on the icon for the **Settings** app *in the dock* and move it to the **Top of the Dock**

## Get the Network Running With the Static IP Address

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

- [X] Use the Command Line or the Software Updater to update the installed packages to their latest versions
  - [X] Using the Command Line:
    - [X] Open a terminal window and run `sudo su -` so we can run additional install commands as root
    - [X] Run `apt-get update` to identify the updated versions that apt can install
    - [X] Run `apt-get upgrade` to download and install these updated versions
  - [-] Using the Software Updater: *(TBD)*
     **TBD: This is probably what I will want to show people in the video**
    - [-] Pin the Software Updater to the dock
    - [-] Run the Software Updater to install updates made since 25.10 was released
- [X] If not already done, open a terminal window and run `sudo su -` so we can run additional install commands as root
- [X] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`
- [X] Open the **Apps** screen, run the **Konsole** app - or *pin it to the dock* and run it from there
- [X] Right-click on the icon for the **Konsole** app *in the dock* and move it to between the *Settings* and *Terminal* apps
- [-] It may be a good idea to reboot the system at this time, *however*
  - It's ok to wait and reboot after going through the steps in the next section
  - *Note* that we will *need* to reboot after updating these files, to take advantage of them being present at boot

## Update Essential Files From Previous Install

Find files from the previous install on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

**Note: Ubuntu 26.04 mounts thumb drives in `/run/media/tomh` (instead of just `/media/tomh`)!!**

- [X] Files in `/home/tomh`
  - [X] Open a terminal window
  - [X] Check in the installed version of `.bashrc`:
    - [X] Run `cd ; ci -l .bashrc` and add the *not-a-log* message *"Installed version."*
  - [X] Move or copy over all the files from `/home/tomh` on the `2023-32A` thumb drive to the `/home/tomh` directory
  - [X] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [X] `rcsdiff .bashrc`        # only CusTOMizations should show up
    - [X] This is a good time to clean up CusTOMizations that are no longer relevant
  - [X] Set background to one of the files in `~/Pictures`
    - Settings -> Appearance -> Background -> + Add Picture
- [X] Files in `/root`
  - [X] Open a terminal window and run `sudo su -` so we can **run these commands as root**
  - [X] Link the following files from `~tomh` to `/root`:
    - [X] `ln -s ~tomh/.bash_aliases .`
    - [X] `ln -s ~tomh/.bash_aliases-* .`
    - [X] `ln -s ~tomh/.vimrc .`
    - [X] `ln -s ~tomh/bin .`        # NOTE: these must be copied over before we can link to them
  - [X] Check in the installed version of `.bashrc`:
    - [X] Run `cd ; ci -l .bashrc` with the *not-a-log* message *"Installed version."*
    - [X] Add the CusTOMizations from the `2023-32A` thumb drive
- [X] Files in `/etc`
  - [X] Open a terminal window and run `sudo su -` so we can run commands as root
  - [X] Check in the installed versions: `cd /etc; ci -l fstab hosts # "Installed version."
  - [X] Add **only the CusTOMizations** from the version of `fstab` on the thumb drive to the installed version of `fstab`
    - [!] **!!! Not following this step properly made the PC unbootable !!!**
    - [!] **Instead of *adding the CusTOMizations*, I *replaced* the `/etc/fstab` file!!! OOPS!!! **
    - [!] See the subsection immediately below for information on how I fixed this!
  - [X] Add **only the CusTOMizations** from the version of `hosts` on the thumb drive to the installed version of `hosts`
- [X] *Definitely* reboot the system at this time
  - If the PC doesn't boot, it's probably an issue with `/etc/fstab`, so fix that right away

### YIKES!  IT DOESN'T BOOT BACK UP!!

**The reboot failed, and it put me in emergency mode!**

- I suspect it is a problem in `/etc/fstab`, because that is one of the things I changed
- Sure enough, running some searches, this popped up as a possible problem
- Unfortunately, the filesystem is read-only, making it impossible to try to fix `/etc/fstab`
- Searching for how to fix the read-only aspect specifically, I found this post:
  - https://stackoverflow.com/questions/383595/repairing-fstab-read-only
- After a few tries, and based on one of the answers there, I was able to fix the read-only filesystem with this command, yay:
  - `mount -n -o remount -t ext4 /dev/sda2 /`
- **It's a good thing I checked the installed version of `/etc/fstab` into RCS!!**
- Then I ran `cd /etc` and ran `mv fstab fstab-possibly_bad`
- Then I ran `co -l fstab` to restore the installed version

**This enabled me to boot back into the install!  WHEW!!**

- [X] Then I added just the CusTOMizations to `/etc/fstab`, plugged in my external USB drives, and rebooted

We now return you to our original programming!!

## Set Essential Keyboard Shortcuts

In reality I use these all the time and quickly go crazy without them.

- [X] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts -> View and Customize Shorcuts
  - Navigation
    - [X] Ctl+Alt+[Left Arrow] - Move window one workspace to the left
    - [X] Ctl+Alt+[Right Arrow] - Move window one workspace to the right
    - [X] Alt+F1 - Switch to Workspace 1
    - [X] Alt+F2 - Switch to Workspace 2
    - [X] Alt+F3 - Switch to Workspace 3
    - [X] Alt+F4 - Switch to Workspace 4
    - [X] Alt+[Left Arrow] - Switch to workspace on the left
    - [X] Alt+[Right Arrow] - Switch to workspace on the right

## Install Our Favorite Music Apps and Set Them up to Play My MP3s

For the detailed checklist of steps to run to complete this goal, refer to the file `7-checklist-standard_apps.md` in this directory.

## Essential Networking - `ssh`

- [X] Get ssh working
  - [X] Copy old `~/.ssh` directory into the new `/home/tomh` directory
    - In particular, we need the old `authorized_keys` file
    - Having the `pubs` subdirectory can help, if we have a problem someday
  - [X] Run `ssh-keygen` to generate new keys
    - When prompted for a file name or passphrase, just press Enter to accept the default values
  - [X] Ensure the permissions on the private key `~/.ssh/id_ed25519` are 0600
    - `ls -l ~/.ssh/id_ed25519`       # should be -rw------- NOT -rw-r--r--
    - `chmod 600 ~/.ssh/id_ed25519`
    - `ls -l ~/.ssh/id_ed25519`
    - These somehow got changed to 644 on `martha`, which caused an ugly error, until I actually read the message and fixed the perms; weird!
  - [X] Copy `~/.ssh/id_ed25519.pub` to `~/.ssh/id_ed25519.pub-ava`
  - [X] Copy the file `~/.ssh/id_ed25519.pub-[hostname]` to a thumb drive so we can copy it to all other linux hosts
  - [X] Move (`mv ...`) the file `~/.ssh/id_ed25519.pub-ava` to the `pubs/` subdirectory for possible future reference
  - [X] Update `~/.ssh/authorized_keys` on all linux hosts, replacing old public key for [hostname] with the new one
    - *Else you will be asked for a password*
  - [X] Remove `.ssh/known_hosts` file from all other hosts
    - *Else you will get a nasty error message*
  - [X] Log in to each host from each host, to make a new `known_hosts` file on each one and ensure they all work

