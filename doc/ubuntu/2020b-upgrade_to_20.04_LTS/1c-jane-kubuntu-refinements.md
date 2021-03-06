
# 1c-jane-refinements.md

Refining 20.04 install on jane.

# Necessary Refinements

Now that I can do stuff without cursing, it's time to get serious.

## Ssh to and From Hosts on the LAN

Remove `~/.ssh/known_hosts` from `jane`, `barbara`, and `bette`.

```
apt list openssh-server
apt install -y openssh-server
apt install net-tools          ## so I can run ifconfig
apt install ifupdown           ## so I can run ifup and ifdown
```

Reboot and ssh into `ava`, `barbara`, and `bette`, and from each of those into the others and `jane` as well.

## Xscreensaver

Find and install all relevant packages:

```
apt search '.*xscreensaver.*'
apt list 'xscreensaver*'
apt install xscreensaver xscreensaver-data-extra xscreensaver-data xscreensaver-gl xscreensaver-gl-extra
```

Add a short script named `xscreensaver.sh` to run it when the system boots to the directory `~/.config/autostart-scripts` .

Following is an example:

```
 $ cat  .config/autostart-scripts/xscreensaver.sh
#!/bin/bash
#
## xscreensaver-demo &
xscreensaver &
```

Reference:

- https://askubuntu.com/questions/487920/how-to-control-programs-run-at-startup

Install the fortune program:

```
apt list '*fortune*'
apt show fortunes
apt install fortune-mod fortunes fortunes-min fortunes-bofh-excuses fortunes-mario
apt install fortunes-ga fortunes-debian-hints fortunes-off fortunes-spam fortunes-ubuntu-server
apt install fortune-anarchism    ## Note: "fortune" is singular in this one
```

Reboot and ensure the screensaver runs automatically.

## External Disk

Install gparted, make directories appropriate for mounting the disk contents, and update fstab to mount them automatically when the system boots.
Reference:

- https://askubuntu.com/questions/125257/how-do-i-add-an-additional-hard-drive

```
apt install gparted
fdisk -l
cd /
mkdir -p /mnt/disks/art
mkdir -p /mnt/disks/FATART
cd /etc
rd fstab
vi fstab
```

Update fstab to mount:

- /dev/sdb/art to /mnt/disks/art
- /dev/sdb/FATART to /mnt/disks/FATART

Add a link to the root directory and fix the links under /art to the FAT filesystem as follows:

```
cd /
l
ln -s /mnt/disks/art/art .
l art
gogd            ## should take you to /art/music/songs/mp3/Grateful_Dead
cd /art/music/
l
rm analog_projects
ln -s /mnt/disks/FATART/art_music_analog_projects analog_projects
goamaa          ## should take you to /art/music/analog_projects/Audacity
cd /art/videos/
l purchased/
cd  purchased/
rm Movies
ln -s /mnt/disks/FATART/art_videos_purchased/Movies  Movies
rm TV_Shows
ln -s /mnt/disks/FATART/art_videos_purchased/TV_Shows .
```

Reboot and ensure the partitions are properly mounted and the `gogd` and `goamaa` aliases still work properly after a reboot.

## Workspace Background

Change the workspace background image:

- Right click an empty area of the desktop
- Select the Desktop Settings option
- Add a new wallpaper image by clicking the Get New Wallpapers... button.

