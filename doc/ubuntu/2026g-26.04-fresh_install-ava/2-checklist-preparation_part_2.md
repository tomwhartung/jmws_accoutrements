
# 2-checklist-preparation_part_2.md

This version of `2-checklist-preparation_part_2.md` reflects the steps I am performing to install **Ubuntu 26.04** on `ava` on **2026-05-06**.


# Preparation

Before the install we need to save some important files and information off on thumb drives and
the like for use after the install.

We need to do this for all hosts, but specifics may vary.


## Save Network Info and Important Files

Copy the steps in this checklist to a file specific to the host currently being upgraded.

Then, when doing the install, note any particularities in the file for that host, for possible future reference.

Save network configuration for static connection:

- [-] **Ubuntu, wi-fi**
  - N/A
- [X] **Ubuntu, wired**
  - [X] Settings -> Wired section -> [Gear Icon]
    - [X] Details tab: Connect automatically
    - [X] Identity tab
       - Name: "Static wired quantum fiber via asus"
       - MTU: Automatic
    - [X] IPv4 tab:
      - [X] IPv4 Method section: Manual
      - [X] Addresses section: Address: 10.0.1.117; Netmask: 255.255.255.0; Gateway: 10.0.1.2
      - [X] DNS section: 192.168.0.1,205.171.2.25
    - [X] Security tab:
      - Authentication: MD5

Save important information about the current filesystems' partitions to the `2023-32A` thumb drive:

```
cd /mnt/disks
mkdir 2023-32A/for_26.04-3-ava
cd 2023-32A/for_26.04-3-ava
l /art > LINKS-art.txt
df | grep '/dev/sd' | sort > df-grep-sort.txt
mkdir -p etc home/tomh root
```

Save important files in `/etc` and `/root` to the `2023-32A` thumb drive:

- [X] Files in `/etc`:
  - [X] Copy `/etc/fstab` and `/etc/hosts` to the thumb drive
- [X] Files and links in `/root`:
  - [X] Copy `~root/.bashrc` to the root directory on the thumb drive
  - [X] Create `LINKS.txt` - use `ls -al` and `cat` to save a list of already-existing links to files and directories in `~tomh`
  - [X] Identify any files other `.bashrc` than that have customizations, and save those customizations
    - [X] **Note:** we rarely do this so don't be surprised if there are no files that need to be saved in this step!

Save important files in `/home/tomh` to the `2023-32A` thumb drive.

- Hosts `barbara`, `bette`, and `martha` should have very few files in `~tomh`
  - At best we want only the files needed to make ssh work
  - Try to keep all the files we are working with on thumb drives, to make upgrading much easier
- Only `ava` and `jane` have a lot of files in `/home/tomh`
  - These are mostly files accumulated over the years that are no longer needed, but still nice to have

- [ ] Files in `/home/tomh`
  - [ ] All linux hosts should have these files and directories
    - [-] Furthermore, `barbara`, `bette`, and `martha` *should* have *only* these files and directories:
      - [ ] Copy directories `bin/`, `.ssh/`, and `Pictures/` to the thumb drive
      - [ ] Copy files `.bash_aliases*`, `.bashrc`, `.gitconfig`, `.vimrc`, `d.e`, `r*`, etc. to the thumb drive
      - [ ] Create `LINKS.txt` - use `ls -al` and `cat` to save a list of already-existing links  in `~tomh` to files and directories on external disks
  - [X] **Optional:** Clean out and copy the `~/Downloads/` directory to the thumb drive
  - [X] On hosts `ava` and `jane` *only* - we keep these anachronistic directories in `/home/tomh`, pretty much just for sentimental reasons
    - [X] Copy directories `~/jobsearch/`, `~/marketing/`, `~/personal/`, `~/technical/`, and `~/work/` to the thumb drive
      - [X] **PRO TIP:** Preserve permissions by creating a `tar` file containing these directories:
        - `cd ; tar cvzf home_subdirs-2026_05_06.tgz marketing/ personal/ technical/ work/`
      + [!] **PARANOID MUCH???** - yeah let's overcome our paranoia and get moving on here by doing both the `cp -r` and the `tar` file!
       + [!] **HEY!!! - Once I start the install and overwrite the disk, there's no goiong back!!**

