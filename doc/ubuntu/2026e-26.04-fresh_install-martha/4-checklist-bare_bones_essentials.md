
# 4-checklist-bare_bones_essentials.md

This version of `4-checklist-bare_bones_essentials.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Bare Bones Essentials Common to All Hosts

These are the first steps to acheiving what is known as *"Sanity"*.

## Set Essential Keyboard Shortcuts

In reality I use these all the time and quickly go crazy without them.

- [ ] Settings -> Keyboard -> [Scroll to bottom] Keyboard Shortcuts -> View and Customize Shorcuts
  - Navigation
    - [ ] Alt+[Left Arrow] - Switch to workspace on the left
    - [ ] Alt+[Right Arrow] - Switch to workspace on the right
    - [ ] Alt+F1 - Switch to Workspace 1
    - [ ] Alt+F2 - Switch to Workspace 2
    - [ ] Alt+F3 - Switch to Workspace 3
    - [ ] Alt+F4 - Switch to Workspace 4
    - [ ] Ctl+Alt+[Left Arrow] - Move window one workspace to the left
    - [ ] Ctl+Alt+[Right Arrow] - Move window one workspace to the right

## Install Essential Packages

- [ ] Use the Command Line or the Software Updater to update the installed packages to their latest versions
  - [ ] Using the Command Line:
    - [ ] Open a terminal window and run `sudo su -` so we can run additional install commands as root
    - [ ] Run `apt-get update` to identify the updated versions that apt can install
    - [ ] Run `apt-get upgrade` to download and install these updated versions
  - [ ] Using the Software Updater: *(TBD)*
     **TBD: This is probably what I will want to show people in the video**
    - [ ] Pin the Software Updater to the dock
    - [ ] Run the Software Updater to install updates made since 25.10 was released
- [ ] If not already done, open a terminal window and run `sudo su -` so we can run additional install commands as root
- [ ] Run `apt-get install rcs vim net-tools openssh-server ifupdown git konsole`

## Update Essential Files From Previous Install

Find old files on the `2023-32A` thumb drive in the `for_...` directory and use them to update the new install.

- [ ] Files in `/home/tomh`
  - [ ] Open a terminal window
  - [ ] Check in the installed version of `.bashrc`:
    - [ ] Run `cd ; ci -l .bashrc` and add the *not-a-log* message *"Installed version."*
  - [ ] Copy over all the files from `/home/tomh` on the `2023-32A` thumb drive
  - [ ] Run `rcsdiff` to ensure that overwriting `.bashrc` did not wipe out any needed updates to the file:
    - [ ] `rcsdiff .bashrc`       # only CusTOMizations should show up
  - [ ] Set background to one of the files in `~/Pictures`
    - Settings -> Appearance -> Background -> + Add Picture
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
- [ ] Files in `/etc`
  - [ ] Open a terminal window and run `sudo su -` so we can run commands as root
  - [ ] Check in the installed versions: `cd /etc; ci -l fstab hosts # "Installed version."
  - [ ] Add CusTOMizations from versions on the `2023-32A` thumb drive

## Essential Networking - `ssh`

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

