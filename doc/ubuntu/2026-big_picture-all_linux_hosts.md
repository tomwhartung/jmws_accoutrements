
# 2026-big_picture-all_linux_hosts.md

Time to start installing Ubuntu 26.04 on all, or at least most, linux hosts.

# About Each Linux Host

## Wired Hosts

### `jane` 2013 - 16G Memory, 500G Internal Disk, Laptop

Named for [Jane Russell](https://en.wikipedia.org/wiki/Jane_Russell).

|When|External Disks|Size|Used|Percent|Remaining|
|----|--------------|:--:|:--:|------:|:-------:|
|Before:|`/mnt/disks/art`|1400G|647G|51%|637G|
|Before:|`/mnt/disks/FATART`|489G|193G|40%|296G|
||||
|After:|**SAME**|||

- Main general purpose host with complete `home` directory, synced with `ava``s
- Downloading and ripping mp3s
- Uploading and organizing Sony-ZV1 video files
- Maintains a backup of all `/art` files on an external disk, INCLUDING Sony-Z and OBSV1 video files (*)
- Rare, extremely occasional social networking using firefox

### `ava` 2016 - 8G Memory, 500G Internal Disk, Desktop

Named for [Ava Gardner](https://en.wikipedia.org/wiki/Ava_Gardner).

|When|External Disks|Size|Used|Percent|Remaining|
|----|--------------|:--:|:--:|------:|:-------:|
|Before:|`/mnt/disks/art`|1400G|510G|40%|795G|
|Before:|`/mnt/disks/FATART`|466G|193G|42%|273G|
|Before:|`/mnt/disks/retro-16*`|15G|5.6G|42%|7.9G|
||||
|After:|**SAME**|||

- Spare general purpose host with complete `home` directory, synced with `jane``s
- Maintain and keep budget up-to-date
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 and OBS video files (*)
- Occasional social networking using chrome

### `barbara` 2016 - 2G Memory, 250G Internal Disk, Desktop

Named for [Bette Davis]().

|When|External Disks|Size|Used|Percent|Remaining|
|----|--------------|:--:|:--:|------:|:-------:|
|Before:|`/mnt/disks/FATALLART`|932G|698G|75%|243G|
|||||
|After:|**disks from `bette`**|
|After:|`/mnt/disks/art`|1400G|507G|39%|798G|
|After:|`/mnt/disks/FATART`|466G|194G|42%|273G|

- For listening to mp3s *only*
- Maintains a backup of all `/art` files on an external disk, EXCEPT Sony-ZV1 and OBS video files (*)

## Wireless Hosts

### `bette` 2011 - 8G Memory, 500G Internal Disk, Laptop, **Portable**

Named for [Bette Davis](https://en.wikipedia.org/wiki/Bette_Davis).

|When|External Disks|Size|Used|Percent|Remaining|
|----|--------------|:--:|:--:|------:|:-------:|
|Before:|`/mnt/disks/art`|1400G|507G|39%|798G|
|Before:|`/mnt/disks/FATART`|466G|194G|42%|273G|
|||||
|After:|**moved to `barbara`**|**NONE**||||

- For portability and playing around with Tracktion *only* - at least to start
- Does **NOT** maintain a backup of **ANY** `/art` files on an external disk, **in order to facilitate portability**
- Possibly for occasional social networking using firefox

### `martha` 2023 - 16G Memory, 500G Internal Disk, Desktop

Named for [Martha Vickers](https://en.wikipedia.org/wiki/Martha_Vickers).

|When|External Disks|Size|Used|Percent|Remaining|
|----|--------------|:--:|:--:|------:|:-------:|
|Before:|`/mnt/disks/art`|1400G|410G|32%|895G|
|Before:|`/mnt/disks/FATART`|466G|193G|42%|273G|
|Before:|`/mnt/disks/FAT-SONGS`|466G|296G|64%|170G|
|||||
|After:|**SAME**|||

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


# Preparation

Some of the specifics for this step may depend on the host.

- [ ] Save network configuration for static hosts
- [ ] Save important files in `/etc`, `/root` and `/home/tomh` to the `2023-32A` thumb drive
  - [ ] `/etc/fstab` and `/etc/hosts`
  - [ ] For `/root`:
    - [ ] Save a list of already-existing links to files and directories in `~tomh`
    - [ ] Identify any files that have customizations, e.g., `.bashrc`
  - [ ] For `/home/tomh`, much will depend on how we will be using the host
    - [ ] `.bash_aliases*`, `.bashrc`, `.ssh/`, `.gitconfig`, `.vimrc`, `d.e`, `Pictures/`, `r*`, etc.


# Bare Bones Essentials Common to All Hosts

Having these is also known as acheiving *"Sanity"*.

### Update Essential Files From Previous Install

Find old files on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

- [ ] Files in `/etc`
  - [ ] Open a terminal window and run `sudo su -` so we can run commands as root
  - [ ] Check in the installed versions: `cd /etc; ci -l fstab hosts # "Installed version."
  - [ ] Add CusTOMizations from versions on the `2023-32A` thumb drive
- [ ] Files in `/home/tomh`
  - [ ] Open a terminal window
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` and add the *not-a-log* message *"Installed version."*
  - [ ] Copy over all the files from `/home/tomh` on the `2023-32A` thumb drive
  - [ ] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [ ] `rcsdiff .bashrc`       # only CusTOMizations should show up
- [ ] Files in `/root`
  - [ ] Open a terminal window and run `sudo su -` so we can **run these commands as root**
  - [ ] Link the following files from `~tomh` to `/root`:
    - [ ] `ln -s ~tomh/.bash_aliases .`
    - [ ] `ln -s ~tomh/.bash_aliases-* .`
    - [ ] `ln -s ~tomh/.vimrc .`
    - [ ] `ln -s ~tomh/bin .`        # NOTE: these must be copied over before we can link to them
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` with the *not-a-log* message *"Installed version."*
    - [ ] Add the CusTOMizations from the `2023-32A` thumb drive

### Install Essential Packages

- [ ] Pin the Software Updater to the dock
- [ ] Run the Software Updater to install updates made since 25.10 was released
- [ ] Open a terminal window and run `sudo su -` so we can run additional install commands as root
- [ ] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`

### Set Essential Keyboard Shortcuts

- [ ] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts
  - [ ] Ctrl+F1 - Switch to Workspace 1
  - [ ] Ctrl+F2 - Switch to Workspace 2
  - [ ] Ctrl+F3 - Switch to Workspace 3
  - [ ] Ctrl+F4 - Switch to Workspace 4

### Networking - `ssh`

- [ ] Get ssh working
  - [ ] Copy old `~/.ssh` directory into the new `/home/tomh` directory
    - In particular, we need the old `authorized_keys` file
    - Having the `pubs` subdirectory can help, if we have a problem someday
  - [ ] Run `ssh-keygen` to generate new keys
  - [ ] Copy `~/.ssh/id_ed25519.pub` to `~/.ssh/id_ed25519.pub-[hostname]`
  - [ ] Update `~/.ssh/authorized_keys` on all linux hosts, replacing old public key for [hostname] with the new one
    - *Else you will be asked for a password*
  - [ ] Remove `.ssh/known_hosts` file from all other hosts
    - *Else you will get a nasty error message*
  - [ ] Log in to each host from each host, to make a new `known_hosts` file on each one and ensure they all work

### Github; Clone the `jmws_accoutrements` Repo

- [ ] Update ssh key for *[hostname]* on github.com
  - [ ] Access User Menu [photo in upper right corner] -> Settings -> Access -> SSH and GPG keys
    - [ ] Delete the old ssh key for *[hostname]*
    - [ ] Add the new ssh key, that was created above, as `*[hostname]*-ubuntu-25.10`
- [ ] Make a subdirectory in `/var` named `/var/www` and change the owner of it to `tomh`:
  - [ ] As the `root` user run: `cd /var; mkdir www; chown tomh:tomh www`
- [ ] Clone the `jmws_accoutrements` repo:
  - [ ] As the `tomh` user run: `cd /var/www; git clone [ssh url from github for the repository]`
    - We probably want to run `git clone git@github.com:tomwhartung/jmws_accoutrements.git`, but check github to be sure

### Populate `~/bin`

Once ssh is working, push the files in `~/bin` from one of the other linux hosts over to the newly-upgraded host:


## Optional, Nice-to-Have Apps

- `chrome`
  - On `jane` and `ava` to start, and maybe `martha` (or others) later
  - Chrome is nice to have, but remember: **it is a pain to keep it update-to-date!**

## Keyboard Shortcuts

This is kinda TBD right now...:

Define these in the Settings app:

- Ctrl-Alt-C: Chrome
- Ctrl-Alt-F: Firefox
- Ctrl-Alt-K: Konsole
- Ctrl-Alt-S: Settings

