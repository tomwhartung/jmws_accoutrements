
# 2-install_24.04-martha.md

Installing 24.04 from scratch on new host martha.


# Preparations

See `1-prepare_for_fresh_install.md` in this directory.

# New Linux Host: martha

Figure out how to get the computer to boot off the thumb drive:

1. Windows 10: Settings -> Recovery -> reboot from here
2. Press F2 continuously

This turned out to be a little tricky.


# Run the install

Boot of the USB and run the installation process.

Use the version that includes vim, rcs, and git.

# Home Directories

## tomh's Home Directory

Populate the `/home/tomh` directory with selected files and directories from the `tarHome` file created for jane:

- `jane-home_tomh-2025_05_29.tgz`

## Root User's Home Directory

Set up `/root` by copying files (`.bashrc`, etc) from jane to `/root` as necessary and reconstructing links to files in `~tomh`,
such as `.bash_aliases`, etc.

Make the directory look like `/root` on `jane`.


# Get Network to Work: Static IP, hosts file, ssh etc.

- Network
  - Static IP: 10.0.0.121
- Fix `/etc/hosts`
  - Use a copy of the one on jane
  - Check in to rcs before making more changes
- Install using `apt install`:
  - net-tools, openssh, openssh-server, ifupdown
- Configure git
  - Copy .gitconfig from another host, OR run:
    - `git config --global user.email "tomwhartung@gmail.com"`
    - `git config --global user.name "Tom Hartung"`
- Install using Discover OR run:
  - `apt-get update`
  - `apt-get upgrade -y`
  - 'apt install xscreensaver*'
  - 'apt install *fortune*'
- Install `/home/tomh` from jane's most recent tar file
  - Unpack in a temp directory and copy what we need from there
    - `.bashrc`, `.bash_aliases`, `.bash_aliases-*`,  `.vimrc`, etc.
- Get ssh to work
  - Run `ssh-keygen`
  - Add `~/.ssh/*` files copied from jane


# Fix Issues

- Remove and re-install firefox because of snap error


# Find Sanity, as Best We Can

- Install google-chrome-stable
  - Apparently we must do this manually now?
  - Download file and run `apt install`

- Adjust System settings as necessary
- Adjust Konsole settings as necessary

