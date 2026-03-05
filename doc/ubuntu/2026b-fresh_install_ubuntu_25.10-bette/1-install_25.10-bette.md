
# 1-install_25.10-bette.md

Time to install 25.10 on bette.

# Why?

- I want to use `barbara` for listening to mp3s
- This will allow me to use `bette` upstairs for playing music with Tracktion and working on movies

# Goals - Big Picture

- Use `barbara` for listening to mp3s instead of `bette`
- Use `bette` for playing music via Tracktion upstairs

# Overview of Installation Process - Big Picture

1. Follow the process they give on [ubuntu.com](https://ubuntu.com).
1. Customize `barbara` for listening to mp3s, using the `/art/*` external disk currently used on `bette`

# A Note Concerning Bette's Disk Partitions

Currently `bette` has a lot of spare disk partitions.

- **We no longer need these, so we will create a new partition table with just one partition!!**


# Preparation

Since we are planning to use `bette` only for playing music, and maybe making videos, at this time we should only need a bare minimum of files there to start.

## Part 1: Create a Bootable USB Drive

[X] Create a Bootable USB Drive - see *2026-big_picture-all_linux_hosts.md*

## Part 2: Save Important Files and Info About `barbara`

- [X] Save network configuration for static on `barbara` - **see below**
- [X] Save important files in `/etc` and `/home/tomh` to the `2023-32A` thumb drive in subdirectories of `for_25.10_on_barbara`


# Installation Process - Specific Steps

## Install Ubuntu 25.10 on `bette`

- [X] Use the USB drive to boot `bette`
  - Accessing BIOS - to get it to boot from the USB drive - might be tricky
  - Sony VAIO laptop Model PCG-71913L, 2011-09; product name VPCEH2LGX; Factory ID CS20 (from bottom of pc)
  - Found and downloaded User Guide from:
    [https://helpguide.sony.net/ammig/VPCEG2_EH2_EJ2_EL2_EK_series/EN/contents/01/01/01/01.html](helpguide.sony.net/ammig/VPCEG2_EH2_EJ2_EL2_EK_series/EN/...)
  - Saved a copy of User Guide in this directory
  - From p. 134 of 368: **press F11 key repeatedly to boot from the USB drive**
  - W00t w00t we're rollin'!
- [X] Run the install
  - Copied and pasted the following checklist from *`2026-big_picture-all_linux_hosts.md`*:
- [X] Use the USB drive to boot the PC
  - [X] May need to mess with the BIOS to get it to boot from the USB drive
    - **True Dat: Needed to RTFM and press F11 repeatedly to boot from USB thumb drive**
- [X] Running the install *on 2026-02-27 at 8:55 PM*
  - [X] Answer easy no-brainer questions
  - [X] Start with **Extended Selection**
  - [X] Yes **Install recommended proprietary software**
  - [X] **Erase disk and install Ubuntu**
     - Dual-boot installs were cool back in the day, but I do not see myself wanting to do those any longer
  - [X] **No encryption**
  - [X] **Create your account**:
    - [X] My name, computer's name, my user id, password;
    - [X] ** *Uncheck* Require my password to log in**
  - [X] Install **started at 9:10 PM** and **finished at 9:26 PM**

## Achieve Sanity Using Ubuntu 25.10 on `bette`

### Find old files on the `2023-32A` thumb drive in `for_25.10_on_bette`
  - `/etc`
  - `/home/tomh`
  - [ ] For details, see *Update Essential Files From Previous Install* in the file `../2026-big_picture-all_linux_hosts.md`
- [ ] Set background image: `~/Pictures/joan_miro_wall_01.jpg`

### Get Network Going

Following are the settings from the previous (Kubuntu) install; the format of Ubuntu's settings may differ slightly

- Connection name: "Wireless Quantum Fiber via tomsasus"
  - General configuration tab:
    - [X] Automatically connect to this network when it is available
		- Wi-Fi tab:
    - SSID: tomsasus
    - Mode: Infrastructure
    - Restrict to device: wlp7s0 (74:E5:0B:36:4E:90)
    - MTU: Automatic
  - Wi-Fi Security tab:
    - WPA/WPA2 Personal
  - IPv4 tab:
    - Method: Manual
    - DNS: 192.168.0.1, 205.171.2.25
    - IP: 10.0.1.112
    - Netmask: 255.255.255.0
    - Gateway: 10.0.1.2
    - Default Route: 10.0.1.2
  - IPv6 tab:
    - Method: Automatic - i.e., Disable

- [ ] Get ssh working
  - Refer to `2026-big_picture-all_linux_hosts.md`

### Steps Common to Upgrades on Multiple Linux Hosts

For details see the following sections in `../2026-big_picture-all_linux_hosts.md`:

- [ ] Install Essential Packages
- [ ] Networking - `ssh`
- [ ] Github; Clone the `jmws_accoutrements` Repo
- [ ] Set Essential Keyboard Shortcuts


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

Isn't that enough??  I kind of hope so!!!

- [ ] **Try to keep things minimal because:**
  - **26.04 will be out on 2026-04-23**
  - **25.10 will expire on 2026-07-09**

