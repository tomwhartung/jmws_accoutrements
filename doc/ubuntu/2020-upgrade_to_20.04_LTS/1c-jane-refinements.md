
# 1c-jane-refinements.md

Refining 20.04 install on jane.

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

## Installing Some Extras

This page suggests, among other things, installing some restricted extra software:

- https://itsfoss.com/things-to-do-after-installing-ubuntu-20-04/

Note: when get a window blocking progress, press tab to select OK, Yes, Agree, or whatever and press Enter.

```
sudo apt install ubuntu-restricted-extras   ## 2. Install media codec
```

Claims it cannot download tts-mscorefonts (or similar) and will try again later.  Whatever!



