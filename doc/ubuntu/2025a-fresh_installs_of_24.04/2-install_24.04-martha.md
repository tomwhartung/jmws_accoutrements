
# 2-install_24.04-martha.md

Installing 24.04 from scratch on new host martha.


# Preparations

See `1-prepare_for_fresh_installs.md` in this directory.

# New Linux Host: martha

Figure out how to get the computer to boot off the thumb drive:

1. Windows 10: Settings -> Recovery -> reboot from here
2. Press F2 continuously

This turned out to be a little tricky.


# Run the install

Boot off the *2023-32B* USB drive and run the installation process.

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

## Install Chrome
- Install google-chrome-stable
  - Reference:
    - https://ubuntuhandbook.org/index.php/2024/04/install-google-chrome-ubuntu-24-04-lts/
  - Apparently it's best to do this manually now?
    - See quote below (from the link above) about the automatic method being *"deprecated"*

> *Download & install the .deb package via the steps above automatically setup the Google Chrome repository for your system. However it’s outdated and **deprecated** due to security and policy change!*

  - Download file and run `apt install <*.deb file name>` as root
    - The following Note/Warning appeared at the end of the `apt` command output
    - A search yielded this solution:
      - https://askubuntu.com/questions/908800/what-does-this-apt-error-message-download-is-performed-unsandboxed-as-root
      - So I ran the two commands immediately below the Note/Warning, that were recommended by that page, as root

> N: Download is performed unsandboxed as root as file '/root/Downloads/google-chrome-stable_current_amd64.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)

```
chown -Rv _apt:root /var/cache/apt/archives/partial/
chmod -Rv 700 /var/cache/apt/archives/partial/
```

## Fine Tuning Shortcuts etc.

- Adjust System settings as necessary
- Adjust Konsole settings as necessary


# Finish Up

- Uninstall firefox because one browser is enough on this host

