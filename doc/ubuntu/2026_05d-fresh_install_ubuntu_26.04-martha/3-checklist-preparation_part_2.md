
# 3-checklist-preparation_part_2.md

This version of `3-checklist-preparation_part_2.md` reflects the steps I performed to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Preparation

Before the install we need to save some important files and information off on thumb drives and
the like for use after the install.

We need to do this for all hosts, but specifics may vary.

## Save Network Info and Important Files

Copy the steps in this checklist to a file specific to the host currently being upgraded.

Then, when doing the install, note any particularities in the file for that host, for possible future reference.

- [ ] Save network configuration for static connection
- [ ] Save important files in `/etc`, `/root` and `/home/tomh` to the `2023-32A` thumb drive
  - [ ] `/etc/fstab` and `/etc/hosts`
  - [ ] For `/root`:
    - [ ] Save a list of already-existing links to files and directories in `~tomh`
    - [ ] Identify any files that have customizations, e.g., `.bashrc`, and save those customizations
  - [ ] For files in `/home/tomh`, much will depend on how we will be using the host
    - [ ] `.bash_aliases*`, `.bashrc`, `.ssh/`, `.gitconfig`, `.vimrc`, `d.e`, `Pictures/`, `r*`, etc.

