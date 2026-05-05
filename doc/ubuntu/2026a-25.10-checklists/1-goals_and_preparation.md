
# 2026_02a-checklists_for_25.10/1-goals_and_preparation.md

Time to start thinking about installing Ubuntu 26.04 on all linux hosts.

**Unfortunately, it won't be out until next year.**

So in the meantime, we will install 25.10 on `barbara` and `bette`.

# Goals - Big Picture

In the short term we want to upgrade `barbara` and `bette` to Ubuntu 25.10

- [X] Upgrade `barbara` to 25.10 **right away**
- [X] Upgrade `bette` to 25.10 **right away**

This way we will be more prepared when it comes time to upgrade all hosts to Ubuntu 26.04


# Overview of Installation Process - Big Picture

1. Follow the process they give on [ubuntu.com](https://ubuntu.com).
1. Customize the process for specific hosts as listed above in the section **Purpose of Each Host**


# Preparation

## Part 1 - Create a Bootable USB Drive

These steps need to be done *only **once** for **all** hosts*.

1. [X] Download the bootable USB drive image from [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
2. [X] Follow the steps on this page to use the *Disks* program to create the bootable USB drive on the `2023-32B` thumb drive
   - [documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop](https://documentation.ubuntu.com/desktop/en/latest/tutorial/install-ubuntu-desktop)

## Part 2 - Save Network Info and Important Files - Host-Specific Steps

These steps may depend, to a varying extent, on the specific host - in which case make notes to that effect in the file for that host.

- [ ] Save network configuration for static connection
- [ ] Save important files in `/etc`, `/root` and `/home/tomh` to the `2023-32A` thumb drive
  - [ ] `/etc/fstab` and `/etc/hosts`
  - [ ] For `/root`:
    - [ ] Save a list of already-existing links to files and directories in `~tomh`
    - [ ] Identify any files that have customizations, e.g., `.bashrc`, and save those customizations
  - [ ] For `/home/tomh`, much will depend on how we will be using the host
    - [ ] `.bash_aliases*`, `.bashrc`, `.ssh/`, `.gitconfig`, `.vimrc`, `d.e`, `Pictures/`, `r*`, etc.

