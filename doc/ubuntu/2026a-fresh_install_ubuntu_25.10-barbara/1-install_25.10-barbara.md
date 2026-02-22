
# 1-install_25.10-barbara.md

Time to install 25.10 on barbara.

# Why?

- Poor `barbara` has very little memory (2G, maybe 3?) and now even crashes a lot even when I have just 6-7-8 tabs open in Firefox
- All I do with `bette` these days is listen to mp3s
- I listen to mp3s every morning on `rita`, a Mac Mini from 2008 (32-bit) that has only 2G memory
- I want to use bette upstairs for playing with Tracktion

# Goals - Big Picture

- Use `barbara` for listening to mp3s instead of `bette`
- Use `bette` for playing music via Tracktion upstairs

# Installation Process

Follow the process they give on [ubuntu.com](https://ubuntu.com).

## Create bootable USB drive

[X] 1. Download the Ubuntu 25.10 bootable USB drive image from [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
[X] 2. Follow the steps on this page to use the *Disks* program to create the bootable USB drive
   - [documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop](https://documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop)

## Install Ubuntu 25.10 on `barbara`

[ ] - Use the USB drive to boot `barbara`
[ ] - Run the install

--- OR MAYBE??? ---

- [ ] Use the USB drive to boot `barbara`
- [ ] Run the install


## Acheive Sanity Using Ubuntu 25.10 on `barbara`

- Find old files on the `2023-32A` thumb drive in `for_25.10_on_barbara`
  - `/etc`
  - `/home/tomh`
- Get network going
  - Steps TBD
- Get ssh working
  - Steps TBD


## Listen to Music on `barbara`

- Use the external drives formerly used on `bette`
  - Set them up for automounting
- Start by using Rhythmbox
  - Link `/art/music/songs/mp3` to `~/Music/Rhythmbox`
- Install (if needed?) and use the `Clementine` mp3 player
  - Link `/art/music/songs/mp3` to `~/Music/Clementine`
- Install and use the `Strawberry` mp3 player
  - Link `/art/music/songs/mp3` to `~/Music/Strawberry`
  - I tried a few different players using 24.10 on `barbara`, and liked this one the best
- Research and possibly install and use another mp3 player


## Is That All There Is?

- Try to keep things minimal because:
  - 26.04 will be out on 2026-04-23
  - 25.10 will expire on 2026-07-09

