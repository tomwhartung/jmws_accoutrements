
# 2-checklist-preparation_part_2.md

This version of `2-checklist-preparation_part_2.md` reflects the steps I am performing to install **Ubuntu 26.04** on `martha` on **2026-05-??**.


# Preparation

Before the install we need to save some important files and information off on thumb drives and
the like for use after the install.

We need to do this for all hosts, but specifics may vary.

## Save Network Info and Important Files

Copy the steps in this checklist to a file specific to the host currently being upgraded.

Then, when doing the install, note any particularities in the file for that host, for possible future reference.

Save network configuration for static connection:

- [X] **Ubuntu, wi-fi**
  - [X] Settings -> WiFi -> Visible Networks -> tomsasus -> [Gear Icon]
    - [X] Details tab: Connect automatically; Make available to other users
    - [X] Identity tab: SSID: tomsasus
    - [X] IPv4 tab:
      - [X] IPv4 Method section: Manual
      - [X] Addresses section: Address: 10.0.1.121; Netmask: 255.255.255.0; Gateway: 10.0.1.2
      - [X] DNS section: 192.168.0.1,205.171.2.25
    - [X] Security tab:
      - [X] Security: wPA & WPA2 Personal
      - [X] Password:
- [X] **Ubuntu, wired**
  - [X] N/A

Save important files in `/etc` and `/root` to appropriately-named directories on the `2023-32A` thumb drive:

- [X] Files in `/etc`:
  - [X] Copy `/etc/fstab` and `/etc/hosts` to the thumb drive
- [X] Files in `/root`:
  - [X] Create `LINKS.txt` - use `ls -al` and `cat` to save a list of already-existing links to files and directories in `~tomh`
  - [X] Identify any files that have customizations, e.g., `.bashrc`, and save those customizations
    - [X] **Note:** we rarely do this so don't be surprised if there are no files that need to be saved in this step!

Save important files in `/home/tomh` to an appropriately-named directory on the `2023-32A` thumb drive:

- Hosts `barbara`, `bette`, and `martha` should have very few files in `~tomh`
  - At best we want only the files needed to make ssh work
  - Try to keep all the files we are working with on thumb drives, to make upgrading much easier
- Only `ava` and `jane` have a lot of files in `/home/tomh`
  - These are mostly files accumulated over the years that are no longer needed, but still nice to have

- [X] Files in `/home/tomh`
  - [X] All linux hosts - `barbara`, `bette`, and `martha` *should* have *only* these files and directories
    - [X] Copy directories `bin/`, `.ssh/`, and `Pictures/` to the thumb drive
    - [X] Copy files `.bash_aliases*`, `.bashrc`, `.gitconfig`, `.vimrc`, `d.e`, `r*`, etc. to the thumb drive
    - [X] Create `LINKS.txt` - use `ls -al` and `cat` to save a list of already-existing links  in `~tomh` to files and directories on external disks
  - [X] We keep these anachronistic directories in `/home/tomh` on `ava` and `jane` *only* - pretty much for just sentimental reasons
    - [N/A] Copy directories `marketing/`, `personal/`, `technical/`, and `work/` to the thumb drive

- [X] **On `martha`** we are experimenting with using links to keep the very few files we want here in these directories on a **thumb drive**

