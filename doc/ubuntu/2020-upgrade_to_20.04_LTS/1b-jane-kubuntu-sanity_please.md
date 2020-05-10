
# 1b-jane-sanity_please.md

Upgrading jane to 20.04.

# Acheiving Sanity

## Home Directory

Restore home directory, one file and directory at a time, for safety.

## Root User's Home Directory

Reconstruct links, e.g., .bash_aliases, present in /ubuntu-16.04/root to /root as appropriate.

Copy files and directories, e.g., .vim and RCS, from /ubuntu-16.04/root to /root as appropriate

## Install Vim, Git, RCS, and Chrome

Vim, Git, and RCS: use the command line.

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

Configure git:

```
git config --global user.email "tomwhartung@gmail.com"
git config --global user.name "Tom Hartung"
```

## Install Chrome

Download from google then install:

```
dpkg -i google-chrome-stable_current_amd64.deb    ## got an error first time
apt install libappindicator3-1
dpkg -i google-chrome-stable_current_amd64.deb    ## worked ok the second time
apt-get install -f
```

Find in menu then Add to Favorites.

## Install Chromium and Opera

Use Ubuntu software app -- i.e., **Discover** -- to install.

Find in menu then Add to Favorites.

Ahh, that is much better!

