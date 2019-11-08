
# 3c-barbara-sanity.md

Achieving sanity as quickly as possible on barbara by installing essential programs

# Essentials

Immediate Goals:

- [x] Restore home directories
- [x] Multiple desktops
- [x] Get barbara on the network
- [x] Install standard packages
- [x] Get look and feel to be consistent with others

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


## Multiple desktops

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

Installing `unity-tweak-tool` as described in a later step gives more control.


## Get barbara on the network

Restore `/etc/hosts*` files and set the settings.

### Restore old copies of `/etc/hosts*` files.

#### Leave hosts.allow and hosts.deny alone

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

#### Keep link to `hosts-www_is_ava` file.

Commands run as root:
```
cd /etc
l host*
l /ubuntu-16.04/etc/host*
l /ubuntu-16.04/etc/hosts*
rcsdiff hosts
rcsdiff hosts.*
ci -l hosts.*
ci -l hosts
l /ubuntu-16.04/etc/hosts*
l /ubuntu-16.04/etc/hosts-www_is_*
l hosts*
   95  l /ubuntu-16.04/etc/hosts-www_is_*
cp /ubuntu-16.04/etc/hosts-www_is_* .
l hosts*
diff hosts hosts-www_is_ava
rd hosts
rm hosts; ln -s hosts-www_is_ava hosts
l
l hosts*
rd hosts
ci -l hosts-www_is_*
rd hosts*
```

End result of all that, much of which was admittedly overly cautious, but that is how I roll:
```
l hosts*
lrwxrwxrwx 1 root root   16 Nov  6 16:05 hosts -> hosts-www_is_ava
-rw-r--r-- 1 root root 2715 Nov  6 16:04 hosts-www_is_ava
-rw-r--r-- 1 root root 3343 Nov  6 16:04 hosts-www_is_barbara
-rw-r--r-- 1 root root  411 Feb  9  2019 hosts.allow
-rw-r--r-- 1 root root  711 Feb  9  2019 hosts.deny

```

### Set static IP address

Settings -> Network -> Wired -> IPv4 tab

- Manual
- Addresses
  - Address: 192.168.1.116
  - Netmask: 255.255.255.0
  - Gateway: 192.168.1.1
- DNS
  - 192.168.30.2, 192.168.31.2

Commands run as root:
```
apt install net-tools
ifconfig
```

Reboot and test network.


## Install standard packages

### unity-tweak-tool

- [x] Install unity-tweak-tool

```
sudo apt-get update
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

### Networking and Version Control

- [x] Install vim, openssh-server
- [x] Install rcs, synaptic, vim, openssh-server
- [x] Install subversion, git, git-svn, (??git-stuff, git-magic??)

```
apt-get update
apt install vim
apt install synaptic openssh-server
apt install subversion git
```

### SSH

**Must remove all `~/.ssh/known_hosts` files to prevent scary errors.**

There is no doubt a more elegant way to do this but just removing them all is simple and effective.

### Screensaver

- [x] Install fortune-mod, fortunes, other fortune* packages as desired
- [x] Install xscreensaver, xscreensaver-data-extra
- [x] Install xscreensaver-gl-extra
- [x] Lock xscreensaver and unity-tweak-tool to launcher
- [x] Remove gnome-screensaver
- [x] Check man page for other steps needed to get it working at startup

```
apt-get update
apt install -y fortune-mod fortunes
apt install -y xscreensaver xscreensaver-data-extra xscreensaver-gl-extra
apt list gnome-screensaver
apt-get remove gnome-screensaver
man xscreensaver     ## if needed
xscreensaver-demo    ## to get settings dialog
```

- [x] Add xscreensaver to startup programs
  - It did this automatically

### Getting More Normal - Settings

- [x] Update System Settings -> Power
- [x] Update Terminal Preferences
  - Apparently included when updating home directory


## Get look and feel to be consistent with others

Background is very important.  Botticelli looks good!

### Essential directories

Commands run as root:
```
cd /var
mkdir www
chown tomh:tomh www
```

Now it is ok to add github repos, such as this one, `jmws_accoutrement` .

### More Standard Apps for the Dock

```
gnome-calculator   ## Once it is running, right-click on the icon and Add it as a Favorite
```

Ubuntu Software icon in dock -> Search -> Libreoffice Calc -> Launch
- Once it is running, right-click on the icon and Add it as a Favorite

