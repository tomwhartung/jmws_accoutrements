
# 3a-install_24.04-barbara.md

Installing 24.04 from scratch on barbara


# Preparations

See `1-prepare_for_fresh_install.md` in this directory.

## Saving Files Currently in /home/tomh

Most of the files we will need are in `barbara-home_tomh-2025_06_03.tgz`

Save the entire `/home/tomh` directory on the **2023-32A** thumb drive:

- Created a`.tgz` file but it was too big to save on the thumb drive
- Had to delete all `~/tmp` and `~/.cache` files to get this to work
  - For details, see `3b-home_tomh-barbara-disk_usage.md` in this directory

## Saving Files Currently in /etc

- Add `/etc/fstab` and `/etc/hosts` to the *2023-32A* thumb drive


# Run the install

Boot off the *2023-32B* USB drive USB and run the installation process.

## Install Options

Use the version that includes vim and git.
This is the version I installed on martha and it saved a few steps.

- I think this is the **"Normal"** version
- I don't think we will need *Element*, *VMs*, or *Krita*

Other options selected:

- *Customize:* Installing the **"Normal"** version on barbara
- *Partitions:* Choosing Erase Disk
- *Users:* Be sure to check the *"Log in automatically"* box!


# Installing Essential Packages

Install as root:

```
apt-get update
apt-get upgrade -y
apt install rcs
apt install net-tools
apt install openssh-server
apt install ifupdown
apt install 'xscreensaver*'
apt install '*fortune*'
```


# Home Directories

## tomh's Home Directory

- Check `.bashrc` into RCS
- Unpack `barbara-home_tomh-2025_06_03.tgz` in a temp directory (`~/unpack`)
- Copy what we need from there into `/home/tomh`
  - `.bashrc`, `.bash_aliases`, `.bash_aliases-*`, `.ssh`, `.vimrc`, etc.

If necessary, get more files from the `home` directory copied to the thumb drive.

## Root User's Home Directory

Set up `/root`:

- Copy `.bashrc` from the thumb drive to `/root`
- Reconstruct links to files in `~tomh`, such as `.bash_aliases`, etc.

Make the directory look like `/root` on `jane`.


# Finding Sanity Part I

## Browser

On barbara we want to use Chrome **only**.

- Install google-chrome-stable
  - Use Firefox to download file and run `apt install` as root user

## Important Settings

System Settings:

- KDE Wallet: when it pops up and asks, click the top button to use the old style

- Workspace Options:
  - Workspace Behavior -> Screen Edges
    - Uncheck top three
    - Switch desktop on edge: Only When Moving Windows
  - Workspace Behavior -> Screen Locking
    - Uncheck top two checkboxes
  - Workspace Behavior -> Virtual Desktops
  - Shortcuts -> Custom Shortcuts
    - Launch Chrome, Konsole, Settings
  - Startup and Shutdown -> Autostart
    - Add konsole and xscreensaver

- Hardware Options:
  - Energy Settings - not yet sure what's ideal here...
    - Uncheck top two check boxes

Konsole -> Settings:

- Configure Konsole:
  - Profiles
    - New: tomh-exp
      - Set as Default
      - Edit:
        - Mouse -> Text Interaction -> Word characters: '_' only
- Configure Keyboard Shortcuts:
  - Move tab to the Left: Shift-Ctrl-Left arrow
  - Move tab to the Reft: Shift-Ctrl-Reft arrow
  - WTF Shift-Ctrl-T and Shift-Ctrl-N don't work?!?
    - Set up Ctrl-Alt-T and Ctrl-Alt-N in both Konsole settings and System Settings->Shortcuts

## Get Network to Work: Static IP, hosts file, ssh, git etc.

- Network
  - Static IP: 10.0.0.116
- Copy `/etc/hosts` from the thumb drive
  - Check it in to rcs before making more changes
- Configure git
  - Copy .gitconfig from another host, OR run:
    - `git config --global user.email "tomwhartung@gmail.com"`
    - `git config --global user.name "Tom Hartung"`
- Ensure ssh works
  - Need to generate new keys: `ssh-keygen`
  - Replace old pub key with new one in `authorized_hosts` on all other hosts
  - Remove `.ssh/known_hosts` file from all other hosts
  - Log in to each host from each host to make new `known_hosts` files and ensure they all work
- Need to pull `jmws_accountrements` code for some ssh scripts to work
  - Use a browser to log into github, get ssh command argument, and run `git clone`


# Fix Issues

See below.


# Find Sanity Part II

Finish up finding sanity in the new version, as best we can.

## When install is nearly complete

- Uninstall Firefox

## WTF Is up With Switching Workspaces With Shift-Ctrl-Arrow_keys??

- When (if?) get Ctrl-Alt-Arrow keys shortcut to switch desktops working:
  - System Settings -> Workspace -> Workspace Behavior:
    - Workspace Behavior -> Screen Edges
      - Switch desktop on edge: Only When Moving Windows

