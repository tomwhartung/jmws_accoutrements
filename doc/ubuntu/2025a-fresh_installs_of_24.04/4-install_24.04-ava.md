
# 4-install_24.04-ava.md

Installing 24.04 from scratch on ava.


# Preparations

See `1-prepare_for_fresh_install.md` in this directory.


# Saving Files in /home/tomh

Most if not all of the files needed in the new install will be in the `tarHome` tar file:

- `ava-home_tomh-2025_06_03.tgz`

Put this on the thumb drive.

## Saving Files Currently in /home/tomh

Most of the files we will need are in `ava-home_tomh-2025_06_03.tgz`

Try saving the entire `/home/tomh` directory on the *2023-32A* thumb drive:

- Delete all `~/tmp` and `~/.cache` files before trying this

## Saving Files Currently in /etc

- Add `/etc/fstab` and `/etc/hosts` to the *2023-32A* thumb drive


# Run the install

Boot off the *2023-32B* USB drive USB and run the installation process.

Use the version that includes vim, rcs, and git.

# Home Directories

## tomh's Home Directory

Populate the `/home/tomh` directory with selected files and directories from the `tarHome` file:

- `ava-home_tomh-2025_06_03`
  - Unpack in a temp directory and copy what we need from there
    - `.bashrc`, `.bash_aliases`, `.bash_aliases-*`,  `.vimrc`, etc.

If necessary, get more files from the `home` directory copied to the thumb drive.

## Root User's Home Directory

Set up `/root` by copying files (`.bashrc`, etc) from jane to `/root` as necessary and reconstructing links to files in `~tomh`,
such as `.bash_aliases`, etc.

Make the directory look like `/root` on `jane`.


# Get Network to Work: Static IP, hosts file, ssh etc.

- Network
  - Static IP: 10.0.0.117
- Copy `/etc/hosts` from the thumb drive
  - Check it in to rcs before making more changes
- Install the following packages using `apt install`:
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
- Ensure ssh works


# Fix Issues

- On martha, I had to remove and re-install firefox because it gave me a snap error


# Find Sanity, as Best We Can

- Install google-chrome-stable
  - Apparently we must do this manually now?
  - Download file and run `apt install`

- Adjust System settings as necessary
- Adjust Konsole settings as necessary

