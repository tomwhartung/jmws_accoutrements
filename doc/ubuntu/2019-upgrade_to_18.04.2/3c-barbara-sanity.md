
# 3c-barbara-sanity.md

Achieving sanity as quickly as possible on barbara by installing essential programs

# Essentials

Immediate Goals:

- [x] Restore home directories
- [x] Get barbara on the network
- [ ] Install standard packages
- [ ] Get look and feel to be consistent with others
- [ ] Start using barbara to rip CDs to mp3

# Details

## Restore home directories

Note: must do tomh first because the root user links to some of tomh's files.

### Restoring `~tomh`

Copy of old home directory is in `/ubuntu-16.04/home` .

Commands run as tomh:

```
cd /home
sudo mkdir tomh-installed
sudo chown tomh:tomh tomh-installed
cp -rp tomh/* tomh-installed
cp -rp tomh/.[a-zA-Z]* tomh-installed
cd tomh
cp -rp /ubuntu-16.04/home/tomh/* .
cp -rp /ubuntu-16.04/home/tomh/.[a-zA-Z]* .
```

### Updating `~root`

Copy of old home directory is in `/ubuntu-16.04/home` .

- **Check to ensure we are not overwriting something needed for the new version**
- This is unlikely but it's best to be safe

Commands run as root:
```
l /ubuntu-16.04/root/
ls -al /ubuntu-16.04/root/
cat .bashrc
diff .bashrc /ubuntu-16.04/root/.bashrc
cp /ubuntu-16.04/root/.bashrc .
ls -al /ubuntu-16.04/root/
cat /ubuntu-16.04/root/postgres_commands.txt
cp /ubuntu-16.04/root/postgres_commands.txt .
apt install rcs
mkdir RCS
ci -l .bashrc  # Installed version
ln -s ~tomh/.bash_aliases .
ln -s ~tomh/.bash_aliases-barbara .
ln -s ~tomh/bin .
ln -s ~tomh/.vimrc  .
```

Reboot to be safe - check that nothing got messed up somehow.


## Get barbara on the network

### Restore old copy of `/etc/hosts*` files.


Commands run as root:
```
Leave hosts.allow and hosts.deny alone

```
root@barbara: ~
$ l /etc/hosts*
-rw-r--r-- 1 root root 222 Aug  4 23:01 /etc/hosts
-rw-r--r-- 1 root root 411 Feb  9  2019 /etc/hosts.allow
-rw-r--r-- 1 root root 711 Feb  9  2019 /etc/hosts.deny
root@barbara: ~
$ cd /etc
root@barbara: /etc
$ diff /ubuntu-16.04/etc/hosts.allow  hosts.allow
1d0
< sendmail: all
root@barbara: /etc
$ diff /ubuntu-16.04/etc/hosts.deny  hosts.deny
root@barbara: /etc
$
```

### Set static IP address


Reboot and test network.

## Install standard packages

### unity-tweak-tool

- [x] Install unity-tweak-tool

```
sudo apt-get install unity-tweak-tool
unity-tweak-tool
```

Got an error when trying to run it:
- The following schema missing is com.canonical.notify-osd
  - "In order to work properly, Unity Tweak Took recommends you install the necessary packages"

Solution found:
- https://askubuntu.com/questions/965583/unity-tweak-tool-schema-missing-com-canonical-desktop-interface/965602

```
apt-get install notify-osd
apt-get install overlay-scrollbar
```

### Version Control

- [ ] Install rcs, synaptic, vim, openssh-server
- [ ] Install subversion, git, git-svn, (??git-stuff, git-magic??)
- [ ] Install fortune-mod, fortunes, other fortune* packages as desired

### Screensaver

- [ ] Install xscreensaver, xscreensaver-data-extra
- [ ] Install xscreensaver-gl-extra
- [ ] Lock xscreensaver and unity-tweak-tool to launcher
- [ ] Remove gnome-screensaver

```
apt-get update
apt list gnome-screensaver
apt-get remove gnome-screensaver
```

- [ ] Add xscreensaver to startup programs
  - It did this automatically

### Getting More Normal - Settings

- [ ] Update System Settings -> Brightness & Lock
- [ ] Update System Settings -> Power
- [ ] Update Terminal Preferences
- [ ] Check man page for other steps needed to get it working at startup
    man xscreensaver

## Get look and feel to be consistent with others

### Multiple desktops

Gone!  WTF!?!

References:
- Why they are gone - drag and drop windows to use them dynamically - what bs
  - https://websiteforstudents.com/what-are-workspaces-and-how-to-use-them-on-ubuntu-18-04-beta/
- How to get them back:
  - https://askubuntu.com/questions/1081251/multiple-workspaces-on-ubuntu-18-04-1-lts-and-later-with-gnome-shell

Commands:
```
sudo apt-get update
sudo apt install gnome-tweaks
gnome-tweaks   ## Once it is running, right-click on the icon and Add it as a Favorite
```

### More Standard Apps

```
gnome-calculator   ## Once it is running, right-click on the icon and Add it as a Favorite
```

Ubuntu Software icon in dock -> Search -> Libreoffice Calc -> Launch
- Once it is running, right-click on the icon and Add it as a Favorite




## Start using barbara to rip CDs to mp3

### Easy Tag

Ubuntu Software icon in dock -> Search -> Easy Tag -> Launch
- Once it is running, right-click on the icon and Add it as a Favorite

### Ripping CDs

#### Trying Rhythmbox

- Ok to rip to .ogg by default
-


