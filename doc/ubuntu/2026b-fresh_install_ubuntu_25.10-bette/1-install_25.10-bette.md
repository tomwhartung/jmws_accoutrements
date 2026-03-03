
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



# IMPORTANT TODOs BEFORE WHIPING OUT BETTE'S DISK


## Review Files in `/home/tomh`, Saving Important Files, and Network Config Info About `bette`

- [ ] Review files in `/home/tomh`, and copy any that are not already in `/home/tomh` on `jane` over to there
- [ ] Save important files in `/etc` and `/home/tomh` to the `2023-32A` thumb drive in subdirectories of `for_25.10_on_bette`
- [ ] Save network configuration for static on `bette` to the `2023-32A` thumb drive


## Wait a Few Days!

**BEFORE OVERWRITING `BETTE`, be sure to spend a few days ensuring `barbara` can play mp3s the way we want it to!**


# A Note Concerning Bette's Disk Partitions

Currently `bette` has a lot of spare disk partitions.

- **We no longer need these, so we will create a new partition table with just one partition!!**


# Preparation

## Create a Bootable USB Drive

1. [X] Download the Ubuntu 25.10 bootable USB drive image from [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
2. [X] Follow the steps on this page to use the *Disks* program to create the bootable USB drive
   - [documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop](https://documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop)

## Save Important and Customized Files to the USB Drive

Use the `2023-32A` thumb drive for saving anything important we will need on the new install.

- **For details, see the section *Preparation* in the file `../2026-big_picture-all_linux_hosts.md`
- Since we are planning to use `bette` only for playing music, and maybe making videos, at this time we should only need a bare minimum of files there to start.


# Installation Process - Specific Steps

## Install Ubuntu 25.10 on `bette`

- [ ] Use the USB drive to boot `bette`
- [ ] Run the install


## Acheive Sanity Using Ubuntu 25.10 on `bette`

- [ ] Find old files on the `2023-32A` thumb drive in `for_25.10_on_bette`
  - `/etc`
  - `/home/tomh`
- [ ] Get network going
  - Wireless, Manual Config - IPv4:
    - Identity - Name: "Wireless Quantum Fiber"; MTU: automatic
    - SSID: tomsasus
    - Mode: Infrastructure
    - Wi-Fi Security: WPA/WPA2 Personal
    - IP: 10.0.1.112
    - Netmask: 255.255.255.0
    - Gateway: 10.0.1.2
    - Default Route: 10.0.1.2
    - DNS: 192.168.0.1, 205.171.2.25
  - IPv6: Disable

- [ ] Get ssh working
  - Refer to `2026-big_picture-all_linux_hosts.md`


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Possible ideas for things that will need to be done this time:

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


