
# 1b-jane-sanity_please.md

Upgrading jane to 20.04.

# Acheiving Sanity

## Home Directory

- 1. Tar up old home directory left in ubuntu-16.04-home
- 2. Move installed /home/tomh to /home/tomh-installed
- 3. Unpack tar file into /home/tomh
- 4. Yikes!  All files and directories in the root /home/tomh directory now appear as icons on the screen!!  See below for fix

## Fix /var/www

Use blkid to properly add /dev/sda10 to /etc/fstab

## Fix Icons

Installed Extensions application, ran and used it to hide the freakin icons.

