
# 0-jane-ubuntu-not_gonna_take_it.md

Ran all the steps outlined in the formerly three separate files concatenated below and
decided I do not want to use ubuntu.

Here are a few of the major reasons for this decision:

- Unhappy with having only vertical workspaces.  I love workspaces, it's my favorite thing!
- Unsatisfied with the whole look-and-feel -- it's like they want my PC to be a phone!  Grr don't get me started!!
- Being unable to install amarok is the last straw.

Of course, amarok is fairly sophisticated and its publication in the latest version may just be delayed for some reason.

- https://en.wikipedia.org/wiki/Kubuntu -- they use the same repositories
- https://answers.launchpad.net/ubuntu/focal/+source/amarok
- https://askubuntu.com/questions/1140947/why-was-amarok-removed-from-19-04-repositories

Even if kubuntu does not include amarok, the look-and-feel issue is pretty huge, and I'm planning to use this
LTS release for many years.  As an aside, on barbara I am finding I enjoy using other KDE packages like k3b.

Going to give kubuntu a try.  I am fairly sure I will be able to find amarok in there once I am done.
If not, well that will suck, but hopefully it will at least have a tolerable look-and-feel.
At worst, I can reinstall the gnome ubuntu!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 1a-jane-plan-disks-basic_install.md

Upgrade jane to Ubuntu 20.04.

# Plan

Upgrade jane by installing into existing `/mnt/future*` and `/mnt/spare*` partitions.

## Upgrading to Ubuntu 20.04 LTS (Focal Fossa)

Upgrade and leave existing OS as-is.

This process should be a little bit easier than always starting from scratch:

- No need to partion disks - always the hardest part
- Will need to burn new DVD
- Will need to reinstall my favorite programs

## List of `/mnt/future*` and `/mnt/spare*` Partitions

Use these partitions first:
```
/dev/sda7        23G   44M   22G   1% /mnt/future
/dev/sda2       925M  1.2M  860M   1% /mnt/future/boot
/dev/sda9        23G   44M   22G   1% /mnt/future/home
```

Use these partitions if needed:
```
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
```

# Disks

## Starting Point

These are the partitions before the install:

```
/dev/sda1       924M  109M  752M  13% /boot
/dev/sda10       19G   12G  5.3G  70% /var/www
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda12       92G   68G   19G  79% /usr/local/tar
/dev/sda13       55G   52M   53G   1% /mnt/spare/sda13
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
/dev/sda2       925M  1.2M  860M   1% /mnt/future/boot
/dev/sda6        23G   12G  9.8G  55% /
/dev/sda7        23G   44M   22G   1% /mnt/future
/dev/sda8        23G  6.9G   15G  32% /home
/dev/sda9        23G   44M   22G   1% /mnt/future/home
```

## Goal

How to name the partitions during install:

```
/dev/sda1       924M  109M  752M  13% /ubuntu-16.04-boot
/dev/sda10       19G   12G  5.3G  70% /var/www         -- Reuse in 16.04
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda12       92G   68G   19G  79% /usr/local/tar   -- Reuse in 16.04
/dev/sda13       55G   52M   53G   1% /
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
/dev/sda2       925M  1.2M  860M   1% /boot
/dev/sda6        23G   12G  9.8G  55% /ubuntu-16.04
/dev/sda7        23G   44M   22G   1% /mnt/spare/sda7
/dev/sda8        23G  6.9G   15G  32% /ubuntu-16.04-home
/dev/sda9        23G   44M   22G   1% /home
```

# Basic Install

Choosing:

- English
- Normal installation
  - Download updates while installing Ubuntu
- Something else - RATHER THAN erase 16.04, install side-by-side with 16.04, or erase disk
  - Fill in partition information as defined above
  - Install Now
- Denver
- Install
  - Tom
  - jane
  - tomh
  - Log in automatically
- "An error occurred while restoring previously-installed applications.
   The installation will continue, but you may have to manually reinstall
   some applications after the computer reboots.
                           OK"
  - Ok

## Faiure!

Does not boot!

Try again with mostly the same, but a few different options:

- Except: choose to format sda2 [/boot] this time
  - It gives a warning about formatting it when I choose Install Now
  - Worth a shot
- Also: choose to "not use" sda10 [/var/www] yet
  - It gives a warning about formatting it when I choose Install Now, hmmm
  - Worth a shot
- Also: choose to format sda13 [/] and sda14 [/mnt/spare/sda14] this time
  - It hung on sda13 after checking the sda13 filesystem when trying to boot
  - Also worth a shot

## Success!!

One of the changes made this time fixed the issue.  Yay!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 1b-jane-sanity_please.md

Upgrading jane to Ubuntu 20.04.

# Acheiving Sanity

## Home Directory

- 1. Tar up old home directory left in ubuntu-16.04-home
- 2. Move installed /home/tomh to /home/tomh-installed
- 3. Unpack tar file into /home/tomh
- 4. Yikes!  All files and directories in the root /home/tomh directory now appear as icons on the screen!!  See below for fix.

## Root User's Home Directory

Reconstruct links, e.g., .bash_aliases, present in /ubuntu-16.04/root to /root as appropriate.

Copy files and directories, e.g., .vim and RCS, from /ubuntu-16.04/root to /root as appropriate

## Fix /var/www

Use blkid to properly add /dev/sda10 to /etc/fstab

Well rats: the install wiped out everything in /dev/sda10.  Good thing it's all in github!

**Will restore all this in a separate step later.**

## Fix Icons

Number 13 on this page says to use the Extensions application, and that it is already installed.

- https://itsfoss.com/things-to-do-after-installing-ubuntu-20-04/

I could not find it in my apps, so I installed, ran, and used it to hide the freakin icons.  Whew!

## Install Vim, Git, RCS, and Chrome

Try using the Ubuntu Software app.

- Note: the Search icon is way up in the upper-left corner of the screen!
- RCS and chrome are not found, but chromium and opera are there, so use the app to install them.

### Vim, Git, and RCS: Use the Command Line.

```
apt list vim
apt install vim
apt list git
apt install git
apt list rcs
apt install rcs
cd /etc
mkdir RCS
ci -l fstab hosts
```

### Chrome

Download from google then install:

```
dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -f
```

Run on command line then lock to launcher, err, "save as a favorite."

### Chromium and Opera

Use Ubuntu software app to install.

Run on command line then lock to launcher, err, "save as a favorite."

Ahh, that is much better!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 1c-jane-refinements.md

Refining Ubuntu 20.04 install on jane.

# Necessary Refinements

Now that I can do stuff without cursing, it's time to get serious.

## Ssh to and From Hosts on the LAN

Remove `~/.ssh/known_hosts` from `jane`, `barbara`, and `bette`.

```
apt list openssh-server
apt install -y openssh-server
```

Ssh into `ava`, `barbara`, and `bette`, and from each of those into the others and `jane` as well.

## Setting Number of Workspaces

Install gnome-tweaks:

```
sudo apt install gnome-tweaks
```

Run it on the command line, Add to Favorites, and use it to:

- Set number of workspaces
- Window Titlebars: Move close button on window title to the left side
- Access Startup Applications
- Tweak top bar

Found here:

- https://askubuntu.com/questions/1081251/multiple-workspaces-on-ubuntu-18-04-1-lts-and-later-with-gnome-shell

## Xscreensaver

Find and install all relevant packages:

```
apt search '.*xscreensaver.*'
apt list 'xscreensaver*'
apt install xscreensaver xscreensaver-data-extra xscreensaver-data xscreensaver-gl xscreensaver-gl-extra
```

Run it on the command line and Add to Favorites.

## Installing Some Suggested Extras

This page suggests, among other things, installing some restricted extra software:

- https://itsfoss.com/things-to-do-after-installing-ubuntu-20-04/

Note: when get a window blocking progress, press tab to select OK, Yes, Agree, or whatever and press Enter.

```
sudo apt install ubuntu-restricted-extras   ## 2. Install media codec
```

Claims it cannot download tts-mscorefonts (or similar) and will try again later.  Whatever!

## Turning off Sticky Edges

Sticky edges are totally annoying.  Fortunately we can turn them off.

```
gsettings set org.gnome.mutter edge-tiling false            ## Worked ok for xeyes
gsettings set org.gnome.shell.overrides edge-tiling false   ## Maybe overkill but I hate it when its sticky
```

Found these commands here:

- https://askubuntu.com/questions/1029168/18-04-how-to-disable-the-window-resizing-when-accidentally-touching-one-of-the

