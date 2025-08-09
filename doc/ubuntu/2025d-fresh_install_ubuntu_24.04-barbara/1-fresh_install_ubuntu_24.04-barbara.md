
# 1-fresh_install_ubuntu_24.04-barbara.md

Installing Ubuntu 24.04 from scratch on barbara.

# Backstory

1. I installed Kubuntu 24.04 LTS on barbara
1. I am finding that with Kubuntu 24.04, the screen saver or (probably) something else (but what?) forces me to enter my password
1. barbara has very minimal memory, because I bought it to be a headless web server, with no windowing
   - Now I want to use it for minimal light surfing
   - And **maybe** use it in the near future for listening to music - *if* it has enough memory to do so - so may want to try that
1. Hence I have decided to install just plain Ubuntu


# Preparations

## Preparing the bootable thumb drive

Following the process at https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview (for the most part) On ava:

1. Downloaded `ubuntu-24.04.2-desktop-amd64.iso` from [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
1. Used **Startup Disk Creator** to create a bootable USB stick on my 2023-32B thumb drive
    - The docs now recommend using balenaEtcher, but I already have **Startup Disk Creator** installed on ava, so I am using that

## Saving Files Currently in /home/tomh

Find my personal files on the **`2023-32A`** drive in the **`for_barbara-24.04b-ubuntu`** directory.

Most of the files we will need are in the **`barbara-home_tomh-2025_06_03.tgz` backup tar file.

- Saved a copy of that on the `2023-32A` drive in `for_barbara-24.04b-ubuntu/usr_local_tar`

Save the entire `/home/tomh` directory on the `2023-32A` thumb drive:

- Tried to copy `/home/tomh/`, but it was "too big" to save on the thumb drive
  - There was room left - according to the `df` command - so I suspect it had to do with there being so many small files
  - On linux sometimes it runs out of inode space; on FAT, well, I'm not sure, but it's probably a similar deal
- Deleted all `~/.cache` files then created a`.tgz` file and saved *that* on the thumb drive in `for_barbara-24.04b-ubuntu/home/tomh`

## Saving Files Currently in /etc

- Copied `/etc/fstab` and `/etc/hosts` to the *`2023-32A`* thumb drive in `for_barbara-24.04b-ubuntu/etc`


# Fresh Install of Ubuntu Linux 24.04 on barbara

## Starting With These Initial Options

Boot off the *2023-32B* USB thumb drive and run the installation process: **Try or Install Ubuntu**

Use the Extended Version that includes "offline-friendly selection of office tools, utilities, and web browser."

## Other Options Selected During the Process:

- [X] *"Install third-party software for graphics and Wi-Fi Hardware"* - check!
  - *"Including but not limited to NVIDIA drivers and similar"*
- [X] *"Download and install support for additional media formats* - check!
  - *"Including but not limited to MP3, MP4, MOV and similar"*

- [X] *"Erase disk and install Ubuntu"*
  - *"Start from scratch or your selected disk"*
  - Advanced features: None - options include LVM and encryption, and some *"Experimental"* options

- [X] NOTE: changing password!  This ex-server is now behind multiple firewalls!!
- [X] **Unchecked** the *"Require my password to log in"* box!

## Basic Install

Started at around 9:20 PM on 2025-08-05 ...

... noticed it was finished by 10:20 PM ...

... and now the *real* fun begins!

## More Options

- [X] Not going for "Pro"
- [X] **"Yes, share system data with the Ubuntu team"** - why the fuck not??  I won't be doing much here on barbara


# CusTOMizations

## Overview

Find the details for each of these steps in its corresponding section below:

1. Review Settings
1. Install Essential Packages
1. Copy `fstab`	and `hosts` files to `/etc`
1. Populate `/home/tomh` directory
1. Populate `/root` Directory
1. Setup `/art` Files Disk
1. Setup Startup Programs
1. Reboot and Check Progress

- ==================
1. **Finding Sanity and Fixing Issues**
  **- TBD...**
- ==================

## Review Settings

Review Settings: Menu icon -> Settings

See what's there and change them when it makes sense:

- System -> Secure Shell -> Turned on
- System -> Date & Time -> Switched from 24-hour to AM/PM
- System -> Software Updates -> Running this, to install all latest updates
- Network - set up static IP
  - IPv4 tab
    - Method: Manual
    - DNS Servers: 75.75.75.75,75.75.76.76
    - Address: 10.0.1.116 | Netmask: 255.0.0.0 | Gateway: 10.0.1.2
- Privacy & Security - turn all that shit off
- Multitasking - Workspaces
- Appearance - Background
- Ubuntu Desktop
  - Desktop Icons - move to Top Left
  - Dock - Icon size: 24 looks good (for now anyway)
  - Dock - move to Bottom
  - Enhanced Tiling - turn it off (for now anyway)
- Power
  - Power Saving -> Screen Blank: Never
  - Power Saving -> Automatic Suspend: Off

## Install Essential Packages

Open terminal and install as root:

```
apt-get update
apt-get upgrade -y
apt install rcs
apt install net-tools
apt install openssh-server
apt install ifupdown
apt install 'xscreensaver*'
apt install '*fortune*'
apt install konsole
```

## Copy `fstab`	and `hosts` files to `/etc`

- [X] 1. Create `RCS` dir in `/etc`
- [X] 2. Check installed versions of `/etc/fstab` and `/etc/hosts` into RCS
- [X] 3. Find `etc/fstab` and `etc/hosts` on the *`2023-32A`* thumb drive in `for_barbara-24.04b-ubuntu/etc`
- [X] 4. Move these files to `/etc/fstab` and `/etc/hosts`
- [X] 5. Use `rcsdiff` command to verify that installed version doesn't contain statements not in the versions from the thumb drive
  - Fix any descrepancies as necessary

## Populate `/home/tomh` Directory

## tomh's Home Directory

- [X] 1. Check `.bashrc` into RCS
- [X] 2. Unpack `barbara-home_tomh-2025_06_03.tgz` into a new directory named `~/Home_tomh-old/unpack-use_1st-tarHome_file`
- [X] 3. Copy what we need from there into `/home/tomh`
  - `.bashrc`, `.bash_aliases`, `.bash_aliases-*`, `.ssh`, `.vimrc`, `r*`, `bin`, `technical`, etc.

If necessary, get more files from the `home` directory copied to the thumb drive.

## Root User's Home Directory

## Populate `/root` Directory
Set up `/root`:

- Copy `.bashrc` from the thumb drive to `/root`
- Reconstruct links to files in `~tomh`, such as `.bash_aliases`, etc.

Make the directory look like `/root` on `jane`.

## Setup `/art` Files Disk

1. Ensure `/etc/fstab` file is updated with external disk info
1. Plugin /art files disk

## Setup Startup Programs

1. Click on **Show Apps** icon in lower right corner
1. Click on **Startup Applications** icon in the list that appears
1. Add `/usr/bin/xscreensaver` to the list
1. Add `/usr/bin/konsole` to the list

## Reboot and Check Progress

- Ensure the disk partitions are mounted ok
- Ensure xscreensaver and konsole are running on startup


# Finding Sanity and Fixing Issues

## More Settings: Menu icon -> Settings

- Keyboard -> Keyboard Shortcuts
  - Launchers - Calculator: Ctrl+Alt+M
  - Launchers - Web Browser: Ctrl+Alt+F
  - Launchers - Settings: Ctrl+Alt+S
  - Navigation - Switch to workspace X: Ctrl-FX

## Downloading `jmws_accoutrements` repo

1. As root, create `/var/www` directory and `chown` it to `tomh:tomh`
1. Log in to github and get ssh link for `jmws_accoutrements` repo
1. As tomh, run `git clone ...` command in the `/var/www` directory

## Get `ssh` Commands to Work

Follow these steps to ensure ssh works on barbara for all other hosts:

1. Need to generate new keys: `ssh-keygen`
1. Replace old pub key with new one in `authorized_hosts` on all other hosts
1. Remove `.ssh/known_hosts` file from all other hosts
1. Log in to each host from each host to make new `known_hosts` files and ensure they all work
1. As a final test, create a test file on barbara in `~/tmp` and use `toTheLinuxHosts` to scp it to all the others

## Browser

Let's try using Firefox **only** on barbara, for now.

- Leaving instructions for installing Chrome below, in case we decide to use it.

## Unresolved `xscreensaver` Issue

- The `xscreensaver` app doesn't run with Wayland
- Ubuntu 24.04 runs Wayland
- `xscreensaver` says to switch to x11
- I'd rather stick with Wayland
- Disabling `xscreensaver` for now...
- Instead, try just blanking after XX minutes:
  - Settings -> Power -> Power Saving -> Screen Blank


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Fine-tuning Konsole -> Settings:

- Configure Konsole:
  - Profiles
    - New: tomh-exp
      - Set as Default
      - Edit:
        - Mouse -> Text Interaction -> Word characters: '_' only
- Configure Keyboard Shortcuts:
  - Move tab to the Left: Shift-Ctrl-Left arrow
  - Move tab to the Reft: Shift-Ctrl-Reft arrow
  - WTF Shift-Ctrl-T and Shift-Ctrl-N don't work?!?
    - Set up Ctrl-Alt-T and Ctrl-Alt-N in both Konsole settings and System Settings->Shortcuts


## Finish up finding sanity in the new version, as best we can.

- Must set Konsole Keyboard Shortcuts in **Both** System Settings and Konsole Keyboard Shortcuts
  - My old shortcuts (Shift+Ctrl+T and Shift+Ctrl+N) do not seem to work in 24.04!  Rats!!
  - System Settings -> Workspace
    - Set New Tab Shortcut to Alt+Shift+T
    - Set New Window Shortcut to Alt+Shift+N
  - Konsole -> Settings -> Configure Keyboard Shortcuts
    - Set New Tab Shortcut to Alt+Shift+T
    - Set New Window Shortcut to Alt+Shift+N

**These are KDE/Kubuntu Settings, which may or may not be availiable in Gnome/Ubuntu.**

Adapt these steps as necessary and appropriate, when there's time.

## Important Settings

System Settings:

- KDE Wallet: when it pops up and asks, click the top button to use the old style

- Workspace Options:
  - Workspace Behavior -> Screen Edges
    - Uncheck top three
    - Switch desktop on edge: Only When Moving Windows
  - Workspace Behavior -> Screen Locking
    - Uncheck top two checkboxes
  - Workspace Behavior -> Virtual Desktops
  - Shortcuts -> Custom Shortcuts
    - Launch Chrome, Konsole, Settings
  - Startup and Shutdown -> Autostart
    - Add konsole and xscreensaver

- Hardware Options:
  - Energy Settings - not yet sure what's ideal here...
    - Uncheck top two check boxes


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Issue(s) to Maybe Fix Later

## Browser

On barbara we want to use Chrome **only**.

- Install google-chrome-stable
  - Use Firefox to download file and run `apt install` as root user

## When Comfortable Using Chrome **Only**

- Uninstall Firefox

## WTF Is up With Switching Workspaces With Shift-Ctrl-Arrow_keys??

- When (if?) get Ctrl-Alt-Arrow keys shortcut to switch desktops working:
  - Use this as a work-around:
    - System Settings -> Workspace -> Workspace Behavior -> Screen Edges
      - Switch desktop on edge: Only When Moving Windows **OR** Always Enabled
  - Figure out which one is preferred and make other hosts match

