
# 2026-big_picture-all_linux_hosts.md

Time to start installing Ubuntu 26.04 on all, or at least most, linux hosts.

# Purpose of Each Host

## `jane` - 16G memory:

- Main general purpose host with complete `home` directory
- Downloading and ripping mp3s
- Uploading and organizing Sony-ZV1 video files
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 video files
- Occasional social networking using firefox

## `ava` - 8G memory:

- Spare general purpose host with backup of `jane's complete `home` directory
- Maintain and keep budget up-to-date
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 video files
- Occasional social networking using chrome

## `barbara` - 2G memory:

- For listening to mp3s *only*
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 video files

## `bette` - 8G memory:

- For playing around with Tracktion *only*
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 video files

## `martha` - 16G memory:

- For playing around with Tracktion
- Maintains a backup of all `/art` files on an external disk, including Sony-ZV1 video files


# Goals - Big Picture

Upgrade all hosts to Ubuntu 26.04

- [ ] Upgrade `barbara` and `bette` to 25.10 **right away**
- [ ] Upgrade `barbara` and `bette` to 26.04 first
- [ ] Upgrade `martha` and `ava` to 26.04 when comfortable with using 26.04 on `barbara` and `bette`
- [ ] Upgrade `jane` to 26.04 last - because I use it as my main Linux host daily and also because it still has some development stuff on it...


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
  - On `jane` and `martha` to start, maybe others later
  - Chrome is nice to have, but remember: **it is a pain to keep it update-to-date!**
- `libreoffice`
  - On `jane`, `ava`, and `martha` to start, maybe others later

## Keyboard Shortcuts

Define these in the Settings app:

- Ctrl-Alt-C: Chrome
- Ctrl-Alt-F: Firefox
- Ctrl-Alt-K: Konsole
- Ctrl-Alt-S: Settings

