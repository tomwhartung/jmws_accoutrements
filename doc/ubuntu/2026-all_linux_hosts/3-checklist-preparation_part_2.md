
# 2026-all_linux_hosts/3-checklist-preparation_part_2.md

Before the install we need to save some important files and information off on thumb drives and
the like for use after the install.

# Preparation

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
  - [ ] For `/home/tomh`, much will depend on how we will be using the host
    - [ ] `.bash_aliases*`, `.bashrc`, `.ssh/`, `.gitconfig`, `.vimrc`, `d.e`, `Pictures/`, `r*`, etc.

