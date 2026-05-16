
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
- 1. Essential Networking - `ssh`

## First Boot

Booting into 26.04 the first time we are prompted to make the following decisions:

- [ ] Location Services - Turn on
  - "*You can change this later in the Settings app*"
- [ ] Help Improve Ubuntu
  - [ ] Share system data with the Ubuntu team - Turn on
  - [ ] Share error reports with the Ubuntu team - Turn on
- [ ] Choose how Ubuntu looks
  - Style - Default
  - Accent Color - Defaults to Orange
- [ ] Finish

## Add the **Terminal** and **Settings** Apps to the Dock

Here we demonstrate two ways to pin an app to the doc.

First, the **Terminal** app:

- [ ] Click on the **Apps** icon in the lower left corner
- [ ] Right-click on the icon for the **Terminal** app and select **Pin to Dock**
- [ ] Press the **Esc** key
- [ ] Right-click on the icon for the **Terminal** app *in the dock* and move it to the **Top of the Dock**

Second, the **Settings** app:

- [ ] Left-click on the **Apps** icon in the lower left corner
- [ ] Left-click on the icon for the **Settings** app to launch it
- [ ] Right-click on the icon for the **Settings** app *in the dock* select **Pin to Dock**
- [ ] Press the **Esc** key
- [ ] Left-click on the icon for the **Settings** app *in the dock* and move it to the **Top of the Dock**

## Get the Network Running With the Static IP Address

- [ ] Open a **Terminal** window and try running:
  - `ping google.com`
  - If it works, great!  But don't be surprised if it doesn't.
  - We are going to need to set a **static IP address**, so might as well do it now.
- [ ] Open the **Settings** app and use the values saved in `2-checklist-preparation_part_2.md` to set up *static IP*
  - [ ] Settings -> Network -> Wired section -> [Gear Icon]
    - [ ] Details tab: Connect automatically
    - [ ] Identity tab
       - Name: "Static wired quantum fiber via asus"
       - MTU: Automatic
    - [ ] IPv4 tab:
      - [ ] IPv4 Method section: Manual
      - [ ] Addresses section: Address: 10.0.1.117; Netmask: 255.255.255.0; Gateway: 10.0.1.2
      - [ ] DNS section: 192.168.0.1,205.171.2.25
    - [ ] Security tab:
      - Authentication: MD5
- [ ] Go back to the **Terminal** window opened previously and try running the `ping` command again:
  - `ping google.com`
  - **If it doesn't work, review the settings entered and figure out why!  This is super-important, so good luck!!**

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
- [ ] Open the **Apps** screen, run the **Konsole** app - or *pin it to the dock* and run it from there
- [ ] Right-click on the icon for the **Konsole** app *in the dock* and move it to between the *Settings* and *Terminal* apps
- [ ] It may be a good idea to reboot the system at this time, *however*
  - It's ok to wait and reboot after going through the steps in the next section
  - *Note* that we will *need* to reboot after updating these files, to take advantage of them being present at boot

## Update Essential Files From Previous Install

Find old files on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

- [ ] Files in `/home/tomh`
  - [ ] Open a terminal window
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` and add the *not-a-log* message *"Installed version."*
  - [ ] Copy over all the files from `/home/tomh` on the `2023-32A` thumb drive
  - [ ] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [ ] `rcsdiff .bashrc`       # only CusTOMizations should show up
    - [ ] This is a good time to clean up CusTOMizations that are no longer relevant
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
  - [ ] Add **only the CusTOMizations** from the version of `fstab` on the thumb drive to the installed version of `fstab`
  - [ ] Add **only the CusTOMizations** from the version of `hosts` on the thumb drive to the installed version of `hosts`
- [ ] *Definitely* reboot the system at this time
  - If the PC doesn't boot, it's probably an issue with `/etc/fstab`, so fix that right away

## Set Essential Keyboard Shortcuts

In reality I use these all the time and quickly go crazy without them.

- [ ] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts -> View and Customize Shorcuts
  - Navigation
    - [ ] Ctl+Alt+[Left Arrow] - Move window one workspace to the left
    - [ ] Ctl+Alt+[Right Arrow] - Move window one workspace to the right
    - [ ] Alt+F1 - Switch to Workspace 1
    - [ ] Alt+F2 - Switch to Workspace 2
    - [ ] Alt+F3 - Switch to Workspace 3
    - [ ] Alt+F4 - Switch to Workspace 4
    - [ ] Alt+[Left Arrow] - Switch to workspace on the left
    - [ ] Alt+[Right Arrow] - Switch to workspace on the right

## Essential Networking - `ssh`

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

