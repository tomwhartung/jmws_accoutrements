
# 3b-barbara-install.md

Upgrading barbara by installing into existing /mnt/future* partitions.

# Installation

1. Create bootable DVD
2. Install DVD in drive and reboot
3. Choose install
3.1. Language
3.2. Normal Installation
3.3. Something Else
3.3.1. See 'Partitions' Below
3.3.2. Install Now
3.4. Timezone
3.5. User Name, password, etc.
4. Installation complete - restarting
5. Results - see 'Results' Below

# Partitions

## Partitions to Format

These are the `/mnt/future*` partitions under 16.04.

```
/dev/sda8    /
/dev/sda10   /home
/dev/sda9    /boot
```

Format these partitions as ext4.

## Partitions to Reuse

Do **not** format these partitions!

Update these to be ext4 filesystems mounted as follows:

```
/dev/sda5        13G  5.4G  6.7G  45% /ubuntu-16.04/
/dev/sda6       923M  109M  751M  13% /ubuntu-16.04/boot
/dev/sda7       9.1G  2.1G  6.5G  25% /ubuntu-16.04/home
/dev/sda11       10G  7.0G  2.5G  74% /ubuntu-16.04/var/www
/dev/sda12      923M  1.3M  859M   1% /mnt/spare/sda12
/dev/sda13      4.5G  251M  4.0G   6% /ubuntu-16.04/usr/src
/dev/sda14      3.7G  438M  3.0G  13% /ubuntu-16.04/lib/modules
/dev/sda15      2.7G  132M  2.5G   6% /ubuntu-16.04/var/cache
/dev/sda16      1.9G  230M  1.5G  14% /ubuntu-16.04/var/log
/dev/sda17      4.5G  9.4M  4.3G   1% /mnt/spare/sda17
/dev/sda18      2.7G  4.2M  2.6G   1% /mnt/spare/sda18
/dev/sda19      1.9G  2.9M  1.7G   1% /mnt/spare/sda19
/dev/sda21       19G  6.3G   12G  35% /usr/local/tar
```

# Results

**Won't let me boot into 16.04, rats!**

Able to get into Windows 10 ok though, whew!

Hold off on updating jane for now, until we get barbara right.

