
# 1-sanity.md

Get a sane desktop on barbara.

# Essentials

For details, see:

- `../2020b-upgrade_to_20.04_LTS/4b-ava-kubuntu-sanity_please.md`.
- `../2020b-upgrade_to_20.04_LTS/4c-ava-kubuntu-refinements.md`.

Overview of process:

- Install:
  - net-tools, vim, rcs, git
- Network
  - Manual static IP: 10.0.1.116
- Configure git
  - `git config --global user.email "tomwhartung@gmail.com"`
  - `git config --global user.name "Tom Hartung"`
- Fix `/etc/hosts`
  - Check in to rcs before making more changes
  - On barbara
  - On all the others
- Install:
  - openssh-server, ifupdown
- List first then install:
  - 'xscreensaver*'
  - '*fortune*'
- Install `/home/tomh` from ava's most recent tar file
  - Update with `~/.ssh/*` files copied from barbara's server days
- Install google-chrome-stable
  - http://ubuntuhandbook.org/index.php/2020/04/google-chrome-ubuntu-20-04-official-repository/
- System settings
  - Adjust as necessary
- Konsole settings
  - Adjust as necessary

