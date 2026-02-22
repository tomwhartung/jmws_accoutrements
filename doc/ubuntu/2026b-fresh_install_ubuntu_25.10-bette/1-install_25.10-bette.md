
# 1-install_25.10-bette.md

Time to install 25.10 on bette.

# Why?

- I want to use `barbara` for listening to mp3s
- I want to use `bette` upstairs for playing with Tracktion

# Goals - Big Picture

- Use `barbara` for listening to mp3s instead of `bette`
- Use `bette` for playing music via Tracktion upstairs

# Overview of Installation Process - Big Picture

1. Follow the process they give on [ubuntu.com](https://ubuntu.com).
1. Customize `barbara` for listening to mp3s, using the `/art/*` external disk currently used on `bette`


# IMPORTANT


## Save Important Files and Info About `bette`

- [ ] Save important files in `/etc` and `/home/tomh` to the `2023-32A` thumb drive in subdirectories of `for_25.10_on_bette`
- [ ] Save network configuration for static on `bette` to the `2023-32A` thumb drive


## Wait a Few Days!

**BEFORE OVERWRITING `BETTE`, be sure to spend a few days ensuring `barbara` can play mp3s the way we want it to!**


# A Note Concerning Bette's Disk Partitions

Currently `bette` has a lot of spare disk partitions.

- **We no longer need these, so we will create a new partition table with just one partition!!**


# Installation Process - Specific Steps

## Create a Bootable USB Drive

1. [X] Download the Ubuntu 25.10 bootable USB drive image from [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
2. [X] Follow the steps on this page to use the *Disks* program to create the bootable USB drive
   - [documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop](https://documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop)

## Install Ubuntu 25.10 on `bette`

- [ ] Use the USB drive to boot `bette`
- [ ] Run the install


## Acheive Sanity Using Ubuntu 25.10 on `bette`

- [ ] Find old files on the `2023-32A` thumb drive in `for_25.10_on_bette`
  - `/etc`
  - `/home/tomh`
- [ ] Get network going
  - Steps TBD
- [ ] Get ssh working
  - Steps TBD


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Possible template for use next year:

# Preparations

- [ ] Update `tarHome` to backup most relevant files for adding to new install
- [ ] Run `tarHome` on jane to be sure we have the latest
- [ ] Review the procedure here:
  - https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/index.html

Extra steps taken, because they seem to make sense to me:

- [ ] Closed chrome windows and tabs that I no longer "need"
- [ ] Rebooted and exited Chrome, leaving only a couple of Konsole windows open

Doing the install:

[ ] TBD


