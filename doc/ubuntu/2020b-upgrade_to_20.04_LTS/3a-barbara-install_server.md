
# 3a-barbara-install_server.md

Installing Ubuntu 20.04 focal fossa server on barbara.

# Disk Partitions

## Partitions Before

This is the before picture:

```
/dev/sda5        13G   33M   13G   1% /future
/dev/sda6       923M  1.2M  859M   1% /future/boot
/dev/sda7       9.1G   21M  8.6G   1% /future/home
/dev/sda8        13G  7.5G  4.7G  62% /
/dev/sda9       923M  236M  624M  28% /boot
/dev/sda10      9.2G  3.4G  5.3G  39% /home
/dev/sda11       10G  3.0G  6.5G  32% /var/www
/dev/sda12      4.5G  3.5G  730M  84% /var/lib
/dev/sda13      3.7G  7.5M  3.4G   1% /mnt/spare/sda13
/dev/sda14      2.7G  4.2M  2.6G   1% /mnt/spare/sda14
/dev/sda15      1.9G  2.8M  1.7G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.4M  4.3G   1% /mnt/spare/sda16
/dev/sda17      2.7G  4.2M  2.6G   1% /mnt/spare/sda17
/dev/sda18      1.9G  198M  1.6G  12% /var/log
/dev/sda20       19G  8.0G  9.9G  45% /usr/local/tar
```

Note: These partitions take up about (13+10) + (13+10+10) + (5+4+3+2) + (5+3+2+19) = 21 + 33 + 14 + 29 = about 100G

Also note: Windows 10 is using 116G.

**Total available space is about 232G.**

## Dump Windows?  Yes I Think So.

### Reasons to Dump Windows

Reasons to delete all the Windows partitions:

- ~~Never~~ Rarely use it except to update it
- It will lose support soon
- If I need a Windows or Mac for something, what I don't know, I can always buy a new cheap one
- Using barbara as the tar file host frees up space on others

### Reasons to NOT Dump Windows

I can't think of one single one.

## Partitions After

~~Reformat disk, delete all existing partitions, and start from scratch!~~

**Or not -  see (*) NOTE below.**

### New Partitions

Create these new partitions from the existing ntfs partitions:

/boot     2G
/       116G
/var     11G

### Mount Points for Old Partitions

```
/dev/sda5        13G   33M   13G   1% /future             -> same
/dev/sda6       923M  1.2M  859M   1% /future/boot        -> same
/dev/sda7       9.1G   21M  8.6G   1% /future/home        -> same
/dev/sda8        13G  7.5G  4.7G  62% /                   -> /ubuntu-18.04
/dev/sda9       923M  236M  624M  28% /boot               -> /ubuntu-18.04/boot
/dev/sda10      9.2G  3.4G  5.3G  39% /home               -> /ubuntu-18.04/home
/dev/sda11       10G  3.0G  6.5G  32% /var/www            -> /ubuntu-18.04/var/www
/dev/sda12      4.5G  3.5G  730M  84% /var/lib            -> /ubuntu-18.04/var/lib
/dev/sda13      3.7G  7.5M  3.4G   1% /mnt/spare/sda13    -> same
/dev/sda14      2.7G  4.2M  2.6G   1% /mnt/spare/sda14    -> same
/dev/sda15      1.9G  2.8M  1.7G   1% /mnt/spare/sda15    -> same
/dev/sda16      4.5G  9.4M  4.3G   1% /mnt/spare/sda16    -> same
/dev/sda17      2.7G  4.2M  2.6G   1% /mnt/spare/sda17    -> same
/dev/sda18      1.9G  198M  1.6G  12% /var/log            -> /ubuntu-18.04/var/log
/dev/sda20       19G  8.0G  9.9G  45% /usr/local/tar      -> /ubuntu-18.04/usr/local/tar
```

(*) NOTE: It just gives me a warm fuzzy to have my old stuff still there so I can access it.

## Partitions After

This is the after picture:

```
/dev/sda1        12G  1.1G  9.9G  10% /var
/dev/sda2       2.0G  200M  1.7G  11% /boot
/dev/sda3       114G  6.1G  102G   6% /

/dev/sda5        13G   33M   13G   1% /future
/dev/sda6       923M  1.2M  859M   1% /future/boot
/dev/sda7       9.1G   21M  8.6G   1% /future/home
/dev/sda8        13G  7.5G  4.7G  62% /ubuntu-18.04
/dev/sda9       923M  236M  624M  28% /ubuntu-18.04/boot
/dev/sda10      9.2G  3.5G  5.3G  40% /ubuntu-18.04/home
/dev/sda11       10G  3.0G  6.5G  32% /ubuntu-18.04/var/www
/dev/sda12      4.5G  3.6G  727M  84% /ubuntu-18.04/var/lib
/dev/sda13      3.7G  7.5M  3.4G   1% /mnt/spare/sda13
/dev/sda14      2.7G  4.2M  2.6G   1% /mnt/spare/sda14
/dev/sda15      1.9G  2.8M  1.7G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.4M  4.3G   1% /mnt/spare/sda16
/dev/sda17      2.7G  4.2M  2.6G   1% /mnt/spare/sda17
/dev/sda18      1.9G  192M  1.6G  12% /ubuntu-18.04/var/log
/dev/sda20       19G  8.0G  9.9G  45% /ubuntu-18.04/usr/local/tar
```

# Focal Fossa Installation

- 1. First time: used new installer and was going to reformat, but it wanted me to "Select a boot disk" but did not say how.
- 2. Second time: used old installer and it crashed
- 3. Third time: going to stick with installing into just the three windows partitions
  - It was a pain to define all those partition mount points!
  - It crashed again!
- 4. Fourth time: try new installer and sticking with installing into just the three windows partitions
  - Maybe they fixed the issue in the new installer

Fourth time is the charm!

Also, the installation left 18.04 intact and supplied an option to use it in the boot menu.
It seems to work OK, except for the network...!

# Focal Fossa Configuration

To be continued in `3b-barbara-server-sanity_please.md`.

