
# 1-install_25.10-barbara.md

Time to install 25.10 on barbara.

# Why?

- Poor `barbara` has very little memory (2G, but shows 3-4) and now even crashes a lot even when I have just 6-7-8 tabs open in Firefox
- All I do with `bette` these days is listen to mp3s
- I listen to mp3s every morning on `rita`, a Mac Mini from 2008 (32-bit) that has only 2G memory, and it works fine
- I want to use `bette` upstairs for playing music with Tracktion, etc.

# Goals - Big Picture

- Use `barbara` for listening to mp3s instead of `bette`
- Use `bette` for playing music using Tracktion and making movies upstairs

# Overview of Installation Process - Big Picture

1. Follow the process they give on [ubuntu.com](https://ubuntu.com).
1. Customize `barbara` for listening to mp3s, using the `/art/*` external disk currently used on `bette`

# Installation Process - Specific Steps

For details, see the process given in
[*2026-big_picture-all_linux_hosts.md*](https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/2026-big_picture-all_linux_hosts.md).

## Preparation

### Part 1: Create a Bootable USB Drive

[X] Create a Bootable USB Drive - see *2026-big_picture-all_linux_hosts.md*

## Part 2: Save Important Files and Info About `barbara`

- [X] Save network configuration for static on `barbara` - **see below**
- [X] Save important files in `/etc` and `/home/tomh` to the `2023-32A` thumb drive in subdirectories of `for_25.10_on_barbara`

## Install Ubuntu 25.10 on `barbara`

- [X] Following the process given in *2026-big_picture-all_linux_hosts.md* under *Installing Ubuntu 25.10*
- [X] Starting to run the install wizard *on 2026-02-27 at 5:50 PM*
- [X] Install **started at 5:58 PM** and **finished before 6:13 PM**

## Achieve Sanity Using Ubuntu 25.10 on `barbara`

### Network - Connection

- [X] Get network going - Wired, Manual Config
  - [X] Settings -> Network -> Wired -> [Click on the Plus sign to add a connection
    - Identity
      - Name: "Wired Quantum Fiber"; MTU: automatic
      - Connect Automatically
    - IPv4:
      - IP: 10.0.1.116
      - Netmask: 255.0.0.0
      - Gateway: 10.0.1.2
      - Default Route: 10.0.1.2
      - DNS: 192.168.0.1, 205.171.2.25
    - IPv6: Disable

### Steps Common to Upgrades on Multiple Linux Hosts

Copied the steps in these sections to identically-named sections in `../2026-big_picture-all_linux_hosts.md` -
because we will be running these multiple times in the near future - but left the original checklists here for posterity:

- [ ] Update Essential Files From Previous Install
- [ ] Install Essential Packages
- [ ] Set Essential Keyboard Shortcuts
- [ ] Networking - `ssh`
- [ ] Github; Clone the `jmws_accoutrements` Repo

### Update Essential Files From Previous Install

Find old files on the `2023-32A` thumb drive in `for_25.10_on_barbara` and use them to update the new install.

- [X] Files in `/etc`
  - [X] Open a terminal window and run `sudo su -` so we can run commands as root
  - [X] Check in the installed versions: `cd /etc; ci -l fstab hosts # "Installed version."
  - [X] Add CusTOMizations from versions on the `2023-32A` thumb drive
- [X] Files in `/home/tomh`
  - [X] Open a terminal window
  - [X] Check in the installed version of `.bashrc`: `cd /etc; ci -l .bashrc # "Installed version."
  - [X] Copy over all the files from `/home/tomh` on the `2023-32A` thumb drive
  - [X] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [X] `rcsdiff .bashrc` - only Customizations should show up
- [X] Files in `/root`
  - [X] Open a terminal window and run `sudo su -` so we can run commands as root
  - [X] Link the following files in `~tomh` to `/root`:
    - [X] `ln -s ~tomh/.bash_aliases .`
    - [X] `ln -s ~tomh/.bash_aliases-barbara .`
    - [X] `ln -s ~tomh/.vimrc .`
    - [X] `ln -s ~tomh/bin .`
  - [X] Check in the installed version of `.bashrc`: `cd /etc; ci -l .bashrc # "Installed version."

### Install Essential Packages

- [X] Pin the Software Updater to the dock
- [X] Run the Software Updater to install updates made since 25.10 was released
- [X] Open a terminal window and run `sudo su -` so we can run additional install commands as root
- [X] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`

### Set Essential Keyboard Shortcuts

- [X] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts
  - [X] Ctrl+F1 - Switch to Workspace 1
  - [X] Ctrl+F2 - Switch to Workspace 2
  - [X] Ctrl+F3 - Switch to Workspace 3
  - [X] Ctrl+F4 - Switch to Workspace 4

### Networking - `ssh`

- [X] Get ssh working
  - [X] Copy old `~/.ssh` directory into the new `/home/tomh` directory
    - In particular, we need the old `authorized_keys` file
    - Having the `pubs` subdirectory can help, if we have a problem someday
  - [X] Run `ssh-keygen` to generate new keys
  - [X] Copy `~/.ssh/id_ed25519.pub` to `~/.ssh/id_ed25519.pub-barbara`
  - [X] Update `~/.ssh/authorized_keys` on all linux hosts, replacing old public key for barbara with the new one
    - *Else you will be asked for a password*
  - [X] Remove `.ssh/known_hosts` file from all other hosts
    - *Else you will get a nasty error message*
  - [X] Log in to each host from each host, to make a new `known_hosts` file on each one and ensure they all work

### Github; Clone the `jmws_accoutrements` Repo

- [X] Update ssh key for `barbara` on github.com
  - [X] Access User Menu [photo in upper right corner] -> Settings -> Access -> SSH and GPG keys
    - [X] Delete the old ssh key for `barbara`
    - [X] Add the new ssh key, that was created above, as `barbara-ubuntu-25.10`
- [X] Make a subdirectory in `/var` named `/var/www` and change the owner of it to `tomh`:
  - [X] As the `root` user run: `cd /var; mkdir www; chown tomh:tomh www`
- [X] Clone the `jmws_accoutrements` repo:
  - [X] As the `tomh` user run: `cd /var/www; git clone [ssh url from github for the repository]`
    - We probably want to run `git clone git@github.com:tomwhartung/jmws_accoutrements.git`, but check github to be sure

## Steps Unique to Upgrading `barbara`

### Listen to Music on `barbara`

- [X] Start by using Rhythmbox
  - [X] Link `/art/music/songs/mp3` to `~/Music/Rhythmbox`
  - [X] Open the Hamburger Menu -> Preferences -> Music page and set the Library Location to `~/Music/Rhythmbox`
    - **NOTE:** Do this **before** adding anything (e.g., subdirs, links, subdirs with links) to `~/Music`
  - [X] Give it a listen!
- [X] Try Clementine
  - [X] Link `/art/music/songs/mp3` to `~/Music/Clementine`
  - [X] Install and pin the `Clementine` mp3 player to the task bar
  - [X] Open the Tools -> Preferences -> Music Library page and add `~/Music/Clementine` to the library
  - [X] Run Tools -> Do a full library rescan
  - [X] Give it a listen!
- [X] Try Strawberry
  - [X] Link `/art/music/songs/mp3` to `~/Music/Strawberry`
  - [X] Install and pin the `Strawberry` mp3 player to the task bar
  - [X] Install and pin the `Strawberry` mp3 player to the task bar
  - [X] Give it a listen!
- [X] Ensure we can use freegalmusic.com in Firefox, and bookmark the site
- [?] If desired, maybe research and possibly install and use another mp3 player
  - Actually, I think we are good, at least for now



### Once We Are Comfortable With Listening to Music on `barbara`

- [ ] Use the external drives formerly used on `bette`
  - Update `/etc/fstab` to Set them up for automounting
- [ ] Swap out the `FATALLART` external drive - *it is now a spare!*
  - Update `/etc/fstab` so it is no longer automounted


## Steps I Did Not Anticipate

Following are a few additional steps I found I needed to do after the install:

- [X] Had to update `tarHome`
  - In the long run, we may really need this script:
    - For `ava` and `jane` - because those will [presumably] be the only hosts on which we have "full" `/home/tomh` directories
    - -> Will have to see how this goes

# Steps to Do Later?

## Keyboard Shortcuts

Because each host will have slightly different roles and slightly different software installed on them,
**these are kinda TBD right now,** but I will probably want to do something similar eventually:

Previously I have been defining these in the Settings app:

- Ctrl-Alt-C: Chrome
- Ctrl-Alt-F: Firefox
- Ctrl-Alt-K: Konsole
- Ctrl-Alt-S: Settings

We may want to change the commands on this list, and - depending on which commands make the list -
use different key combinations for them.


# Is That All There Is?

Isn't that enough??  I kind of hope so!  Because I really need to be more on the ball about keeping these hosts up-to-date!!

- [ ] **Try to keep things minimal because:**
  - **26.04 will be out on 2026-04-23**
  - **25.10 will expire on 2026-07-09**

