
# 1a-jane-plan-disks-basic_install.md

Upgrade jane to 20.04.

# Plan

Upgrade jane by installing into existing `/mnt/future*` and `/mnt/spare*` partitions.

## Upgrading to Ubuntu 20.04 LTS (Focal Fossa)

Upgrade and leave existing OS as-is.

This process should be a little bit easier than always starting from scratch:

- No need to partion disks - always the hardest part
- Will need to burn new DVD
- Will need to reinstall my favorite programs

## List of `/mnt/future*` and `/mnt/spare*` Partitions

Use these partitions first:
```
/dev/sda7        23G   44M   22G   1% /mnt/future
/dev/sda2       925M  1.2M  860M   1% /mnt/future/boot
/dev/sda9        23G   44M   22G   1% /mnt/future/home
```

Use these partitions if needed:
```
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
```

# Disks

## Starting Point

These are the partitions before the install:

```
/dev/sda1       924M  109M  752M  13% /boot
/dev/sda10       19G   12G  5.3G  70% /var/www
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda12       92G   68G   19G  79% /usr/local/tar
/dev/sda13       55G   52M   53G   1% /mnt/spare/sda13
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
/dev/sda2       925M  1.2M  860M   1% /mnt/future/boot
/dev/sda6        23G   12G  9.8G  55% /
/dev/sda7        23G   44M   22G   1% /mnt/future
/dev/sda8        23G  6.9G   15G  32% /home
/dev/sda9        23G   44M   22G   1% /mnt/future/home
```

## Goal

How to name the partitions during install:

```
/dev/sda1       924M  109M  752M  13% /ubuntu-16.04-boot
/dev/sda10       19G   12G  5.3G  70% /var/www         -- Reuse in 16.04
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda12       92G   68G   19G  79% /usr/local/tar   -- Reuse in 16.04
/dev/sda13       55G   52M   53G   1% /
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
/dev/sda2       925M  1.2M  860M   1% /boot
/dev/sda6        23G   12G  9.8G  55% /ubuntu-16.04
/dev/sda7        23G   44M   22G   1% /mnt/spare/sda7
/dev/sda8        23G  6.9G   15G  32% /ubuntu-16.04-home
/dev/sda9        23G   44M   22G   1% /home
```

# Basic Install

Choosing:

- English
- Normal installation
  - Download updates while installing Ubuntu
- Something else - RATHER THAN erase 16.04, install side-by-side with 16.04, or erase disk
  - Fill in partition information as defined above
  - Install Now
- Denver
- Install
  - Tom
  - jane
  - tomh
  - Log in automatically
- "An error occurred while restoring previously-installed applications.
   The installation will continue, but you may have to manually reinstall
   some applications after the computer reboots.
                           OK"
  - Ok

## Faiure!

Does not boot!

Try again with mostly the same, but a few different options:

- Except: choose to format sda2 [/boot] this time
  - It gives a warning about formatting it when I choose Install Now
  - Worth a shot
- Also: choose to "not use" sda10 [/var/www] yet
  - It gives a warning about formatting it when I choose Install Now, hmmm
  - Worth a shot
- Also: choose to format sda13 [/] and sda14 [/mnt/spare/sda14] this time
  - It hung on sda13 after checking the sda13 filesystem when trying to boot
  - Also worth a shot

## Success!!

One of the changes made this time fixed the issue.  Yay!

