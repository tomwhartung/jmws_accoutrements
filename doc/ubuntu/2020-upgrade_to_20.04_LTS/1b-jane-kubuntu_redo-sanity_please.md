
# 1b-jane-sanity_please.md

Upgrading jane to 20.04.

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

