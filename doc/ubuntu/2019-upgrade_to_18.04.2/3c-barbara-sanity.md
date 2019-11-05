
# 3c-barbara-sanity.md

Achieving sanity as quickly as possible on barbara by installing essential programs

# Essentials

Immediate Goals:

- Restore home directory
- Get barbara on the network
- Install standard packages
- Get look and feel to be consistent with others
- Start using barbara to rip CDs to mp3

# Details

## Restore home directory

Copy of old home directory is in `/ubuntu-16.04/home` .

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

Reboot


## Get barbara on the network

- Restore old copy of `/etc/hosts` .
- Set static IP address


## Install standard packages

[ ] Install unity-tweak-tool
    apt-get install unity-tweak-tool
[ ] Install rcs, synaptic, vim, openssh-server
[ ] Install subversion, git, git-svn, (??git-stuff, git-magic??)
[ ] Install fortune-mod, fortunes, other fortune* packages as desired
[ ] Install xscreensaver, xscreensaver-data-extra
[ ] Install xscreensaver-gl-extra
[ ] Lock xscreensaver and unity-tweak-tool to launcher
[ ] Remove gnome-screensaver
    apt-get update
    apt list gnome-screensaver
    apt-get remove gnome-screensaver
[ ] Add xscreensaver to startup programs
    gnome-session-properties
[ ] Update System Settings -> Brightness & Lock
[ ] Update System Settings -> Power
[ ] Update Terminal Preferences
[ ] Check man page for other steps needed to get it working at startup
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


