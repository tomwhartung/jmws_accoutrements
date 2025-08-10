
# 1-REinstall_ubuntu_24.04-martha.md

RE-installing Ubuntu 24.04 from scratch on new host martha.

# Backstory: Why It's a RE-install

1. It had been a while since I have worked with ubuntu installs and I forgot that I prefer Kubuntu (KDE)
1. So I wound up installing Ubuntu 24.04 LTS and was all like WTF, oh yeah, oops!
1. So I installed Kubuntu 24.04 LTS instead
1. I am finding that with Kubuntu 24.04, the screen saver doesn't time out and sleep the way I want it to
    - This is happening on barbara, too, but I think in a different way.  Hmm.
1. So I have decided to go back to Ubuntu after all
    - Ultimately, at least for the time being, the idea is to do only music stuff on martha

These are the steps I'm taking, for possible future reference, or at least to keep me focused and provide an internal dialog as I go along


# Preparations

## Create Bootable USB Drive

Following the process at https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview (for the most part) On ava:

1. Downloaded `ubuntu-24.04.2-desktop-amd64.iso` from [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
1. Used **Startup Disk Creator** to create a bootable USB stick on my 2023-32B thumb drive
    - The docs now recommend using balenaEtcher, but I already have **Startup Disk Creator** installed on ava, so I am using that

## Saved Files Currently in /home/tomh

Find my personal files on the **`2023-32A`** drive in the **`for_martha-24.04c-ubuntu`** directory.

Most of the files we will need are in the **`martha-home_tomh-2025_07_31.tgz` backup tar file.

- Saved a copy of that on the `2023-32A` drive in `for_martha-24.04c-ubuntu/usr_local_tar`

Save the entire `/home/tomh` directory on the `2023-32A` thumb drive:

- Tried to copy `/home/tomh/`, but it was "too big" to save on the thumb drive
  - Had to delete all `~/.cache` files to get the others

## Saving Files Currently in /etc

- Copied `/etc/fstab` and `/etc/hosts` to the *`2023-32A`* thumb drive in `for_martha-24.04c-ubuntu/etc`


# Fresh Install of Ubuntu Linux 24.04 on martha

Booted martha from the USB stick and ran through the installation procedure.

## Starting With These Initial Options

Running the installation process: **Try or Install Ubuntu**

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

Started at around 7:10 PM on 2025-08-09 ...

... noticed it was finished by 7:20 PM ...

... and now the *real* fun begins!

## More Options

- [X] Not going for "Pro"
- [X] **"Yes, share system data with the Ubuntu team"** - why the fuck not??  I won't be doing much here on barbara


# First Time Failed!

Did several steps: reviewed some settings and installed a few packages, rebooted, then WTAF `sudo` Does Not Work?!?  It worked fine on barbara!!

- This page says to boot off a "Live CD":
  - [https://askubuntu.com/questions/354315/permission-denied-for-all-sudo-comands](https://askubuntu.com/questions/354315/permission-denied-for-all-sudo-comands)
- **This is not easy on this box!**
- Need to press Esc slowly but steadily to get to BIOS
- Trying this: **BIOS -> Settings -> Boot -> GO2BIOS -> Enabled**
  - "Allows you to enter BIOS setup directly by pressing the Power button for 4 sec upon bootup.
- Maybe that will help??
- In the meantime, **setting "UEFT USB Key:UEFI: USB DISK, Partition 2" 1st in the Boot Priority**
- This doesn't seem to "stick" but maybe I can boot into the "Live CD" at least once.
- **Starting over from scratch!!**

## **This time do the following before doing anything else:**

[X] **Try `sudo`!!**
[X] **Set a root password in case `sudo` breaks again!!**
[X] **Run `apt` on the command line to update the system!!**
[X] **reboot the system and check `sudo` and root access again!!**


# CusTOMizations

## Overview

Find the details for each of these steps in its corresponding section below:

1. Review Settings
1. Install Essential Packages - Settings -> Software Updates
1. Install Essential Packages - Command Line
1. Copy `fstab` and `hosts` files to `/etc`
1. Populate `/home/tomh` directory
1. Populate `/root` Directory
1. Setup `/art` Files Disk
1. Setup Startup Programs
1. Reboot and Check Progress

- ==================
1. **Finding Sanity and Fixing Issues**
  **- TBD...**
- ==================

## Install Essential Packages - Command Line

Open terminal and install as root:

```
su - root
apt-get update
apt-get upgrade -y
reboot
```

```
sudo su -
apt install rcs
apt install konsole
apt install openssh-server
apt install net-tools
apt install ifupdown
reboot
```

## Install Essential Packages - Settings -> Software Updates

I wonder if one of these screwed up the `sudo` command?

- OBS
- Konsole
- Reboot
- Test root access - *yes, I am paranoid now*

```
su -
sudo su -
```

## Review Settings

Review Settings: Menu icon -> Settings

[ ] System -> Secure Shell -> Turned on
[ ] System -> Date & Time -> Switched from 24-hour to AM/PM
[ ] System -> Software Updates -> Running this, to install all latest updates
[ ] Wi-Fi - IPv4 tab - set up static IP
   - Method: Manual
   - DNS Servers: 75.75.75.75,75.75.76.76
   - Address: 10.0.1.121 | Netmask: 255.0.0.0 | Gateway: 10.0.1.2
[ ] Privacy & Security
   - Screen Lock: turn all that shit off
[ ] Multitasking - Workspaces
[ ] Power
   - Power Mode -> Power Saver
   - Power Saving -> Screen Blank: Never
   - Power Saving -> Automatic Suspend: Off

## Copy `fstab` and `hosts` files to `/etc`

- [ ] 1. Create `RCS` dir in `/etc`
- [ ] 2. Check installed versions of `/etc/fstab` and `/etc/hosts` into RCS
- [ ] 3. Find `etc/fstab` and `etc/hosts` on the *`2023-32A`* thumb drive in `for_martha-24.04c-ubuntu/etc`
- [ ] 4. Move these files to `/etc/fstab` and `/etc/hosts`
- [ ] 5. Use `rcsdiff` command to verify that installed version doesn't contain statements not in the versions from the thumb drive
  - Fix any descrepancies as necessary


## Populate `/home/tomh` Directory

## tomh's Home Directory

- [ ] 1. Check `.bashrc` into RCS
- [ ] 2. Unpack `martha-home_tomh-2025_07_31.tgz` into a new directory named `~/Home_tomh-old/unpack-use_1st-tarHome_file`
- [ ] 3. Copy what we need from there into `/home/tomh`
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
1. Add `/usr/bin/konsole` to the list

## Reboot and Check Progress

- Ensure the disk partitions are mounted ok


- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
- DO THESE THINGS LATER
- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Finding Sanity and Fixing Issues

## More Settings: Menu icon -> Settings

- Appearance - Background
- Ubuntu Desktop
  - Desktop Icons - move to Top Left
  - Dock - Icon size: 24 looks good (for now anyway)
  - Dock - move to Bottom
  - Enhanced Tiling - turn it off (for now anyway)

- Keyboard -> Keyboard Shortcuts
  - Launchers - Calculator: Ctrl+Alt+M
  - Launchers - Web Browser: Ctrl+Alt+F
  - Launchers - Settings: Ctrl+Alt+S
  - Navigation - Switch to workspace X: Ctrl-FX

## Downloading `jmws_accoutrements` repo

1. Configure git: copy .gitconfig from another host, OR run:
   - `git config --global user.email "tomwhartung@gmail.com"`
   - `git config --global user.name "Tom Hartung"`
1. As root, create `/var/www` directory and `chown` it to `tomh:tomh`
1. Log in to github and get ssh link for `jmws_accoutrements` repo
1. As tomh, run `git clone ...` command in the `/var/www` directory

## Get `ssh` Commands to Work

Follow these steps to ensure ssh works on martha for all other hosts:

1. Need to generate new keys: `ssh-keygen`
1. Replace old pub key with new one in `authorized_hosts` on all other hosts
1. Remove `.ssh/known_hosts` file from all other hosts
1. Log in to each host from each host to make new `known_hosts` files and ensure they all work
1. As a final test, create a test file on martha in `~/tmp` and use `toTheLinuxHosts` to scp it to all the others

## Browser

Let's try using **both** Firefox and Chrome on martha, for now.

- See the instructions for installing Chrome below, for when we decide to start using it.

## `xscreensaver` Issue

Boo, `xscreensaver` does not run with wayland!

### For Possible Future Reference

If they ever fix that issue, we can do these steps to use it:

apt install 'xscreensaver*'
apt install '*fortune*'
1. Add `/usr/bin/xscreensaver` to the list
- Ensure xscreensaver and konsole are running on startup


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-



# Fix Issues


# Find Sanity, as Best We Can

## Install Chrome
- Install google-chrome-stable
  - Reference:
    - https://ubuntuhandbook.org/index.php/2024/04/install-google-chrome-ubuntu-24-04-lts/
  - Apparently it's best to do this manually now?
    - See quote below (from the link above) about the automatic method being *"deprecated"*

> *Download & install the .deb package via the steps above automatically setup the Google Chrome repository for your system. However it’s outdated and **deprecated** due to security and policy change!*

  - Download file and run `apt install <*.deb file name>` as root
    - The following Note/Warning appeared at the end of the `apt` command output
    - A search yielded this solution:
      - https://askubuntu.com/questions/908800/what-does-this-apt-error-message-download-is-performed-unsandboxed-as-root
      - So I ran the two commands immediately below the Note/Warning, that were recommended by that page, as root

> N: Download is performed unsandboxed as root as file '/root/Downloads/google-chrome-stable_current_amd64.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)

```
chown -Rv _apt:root /var/cache/apt/archives/partial/
chmod -Rv 700 /var/cache/apt/archives/partial/
```

## Install Waveform Etc.

- [ ] Install Tracktion download manager
  - Got the Note/Warning quoted below
    - Frankly I don't think running it unsandboxed is a big deal
  - Note that it is similar to the one above, but this one concerns the *Downloads* directory
    - Oh rats, I see now that the one above was also for the *Downloads* directory
    - Try running the slightly different commands immediately below the Note/Warning, because `~root/Downloads` seems like the logical place to be installing downloaded `.deb` files
    - Note that I changed the `700` to `770` in the second command, so that `root` can continue to copy files into their `Downloads` directory!
- [ ] Install all of the Tracktion software I have purchased

> N: Download is performed unsandboxed as root as file '/root/Downloads/tracktion_download_manager_v1.5.3.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)

```
chown -Rv _apt:root /root/Downloads
chmod -Rv 770 /root/Downloads
```


## Fine Tuning Shortcuts etc.

- Adjust System settings as necessary
- Adjust Konsole settings as necessary


# Finish Up

- Consider uninstalling firefox because one browser is enough on this host

