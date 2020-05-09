
# 1b-bette-kde_refinements.md

These are some refinements needed after switching to KDE.

# External Disk

Make directories appropriate for mounting the disk contents, and update fstab to mount them automatically when the system boots.

Reference:

- https://askubuntu.com/questions/125257/how-do-i-add-an-additional-hard-drive

```
mkdir -p /mnt/disks/art
mkdir -p /mnt/disks/FATART
cd /etc
rd fstab     # Ensure latest version has been checked in
vi fstab
```

Update fstab to mount:

- /dev/sdb1/art to /mnt/disks/art
- /dev/sdb2/FATART to /mnt/disks/FATART

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

