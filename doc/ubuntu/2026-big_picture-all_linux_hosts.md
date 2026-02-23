
# 2026-big_picture-all_linux_hosts.md

Time to start installing Ubuntu 26.04 on all, or at least most, linux hosts.

# Purpose of Each Host

## Wired

### `jane` 2013 - 16G Memory, 500G Internal Disk, Laptop

- Main general purpose host with complete `home` directory, synced with `ava``s
- Downloading and ripping mp3s
- Uploading and organizing Sony-ZV1 video files
- Maintains a backup of all `/art` files on an external disk, INCLUDING Sony-Z and OBSV1 video files (*)
- Rare, extremely occasional social networking using firefox

### `ava` 2016 - 8G Memory, 500G Internal Disk, Desktop

- Spare general purpose host with complete `home` directory, synced with `jane``s
- Maintain and keep budget up-to-date
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 and OBS video files (*)
- Occasional social networking using chrome

### `barbara` 2016 - 2G Memory, 250G Internal Disk, Desktop

- For listening to mp3s *only*
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 and OBS video files (*)

## Wireless

### `bette` 2011 - 8G Memory, 500G Internal Disk, Laptop, **Portable**

- For portability and playing around with Tracktion *only* - at least to start
- Does **NOT** maintain a backup of **ANY** `/art` files on an external disk, **in order to facilitate portability**
- Possibly for occasional social networking using firefox

### `martha` 2023 - 16G Memory, 500G Internal Disk, Desktop

- For playing around with Tracktion and ???
- Maintains a backup of all `/art` files on an external disk, INCLUDING Sony-ZV1 and OBS video files (*)
- Possibly for occasional social networking using firefox, or possibly chrome

(*) A **big** reason for all of this is really to prepare for shifting into working with movies.
These Sony-ZV1 and OBS files are big, and I plan to create a lot of them over the next few-to-several years.
So I don't need a lot of backups, and moreover I will also be working with these files on `dorothy` the PC and `mary` the Mac.
This need to work with them  on non-Linux hosts requires keeping extra copies of them on **FAT thumb drives,**
for easily moving them to and from those hosts in addition to the Linux LAN.

# Goals - Big Picture

Upgrade all hosts to Ubuntu 26.04

- [ ] Upgrade `barbara` and `bette` to 25.10 **right away**
- [ ] Upgrade `barbara` and `bette` to 26.04 when it comes out on **2026-04-23**
- [ ] Upgrade `martha` and `ava` to 26.04 when comfortable with using 26.04 on `barbara` and `bette`
- [ ] Upgrade `jane` to 26.04 last - because it is my main Linux host that I use daily and it still has some development stuff on it...


# Overview of Installation Process - Big Picture

1. Follow the process they give on [ubuntu.com](https://ubuntu.com).
1. Customize the process for specific hosts as listed above in the section **Purpose of Each Host**


# Bare Bones Essentials Common to All Hosts

Having these is also known as acheiving *"Sanity"*.

## `~/bin` and `jmws_accoutrements`

Need to set these up early in the process.

- Details TBD, as I do the first few of them... 

## `~/.bash*` and `ssh`

Need to set these up early in the process.

- Details TBD, as I do the first few of them... 
  - Install `ssh` ... 
  - Run `ssh-keygen ...` ... 

## Required, Must-Have Apps

Need to set these up early in the process.

- `rcs`
- `ssh`
- `vim`

## Optional, Nice-to-Have Apps

- `chrome`
  - On `jane` and `ava` to start, and maybe `martha` (or others) later
  - Chrome is nice to have, but remember: **it is a pain to keep it update-to-date!**
- `libreoffice`
  - On `jane`, `ava`, and `martha` to start, maybe others later

## Keyboard Shortcuts

Define these in the Settings app:

- Ctrl-Alt-C: Chrome
- Ctrl-Alt-F: Firefox
- Ctrl-Alt-K: Konsole
- Ctrl-Alt-S: Settings

