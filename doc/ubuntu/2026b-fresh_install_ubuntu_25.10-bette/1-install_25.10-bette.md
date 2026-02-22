
# 1-install_26.04-bette.md

Time to install 26.04 on bette.

See `../2026a-fresh_install_of_26.04-jane/1-install_26.04-jane.md`.

In particular, see the:

- ** *Suggested Installation Process* appearing after the analysis of *Jane's Disk Partitions* **

# Bette's Disk Partitions

Installing 26.04 should be straightforward and safe because bette has a lot of
**spare disk partitions.**

- These partitions were designed to make installing new versions easy
- See `../2026a-fresh_install_of_26.04-jane/1-install_26.04-jane.md` to understand why

## `df` Command Output on Bette

The following code listings show all partitions followed by a look at partitions that:

- Were previously used by version 14.04
- Are currently being used by version 18.04, **which is no longer supported!**
- Are currently `spare`
- Are specifically designated for `future` use

```
$ dfh | grep sda | sort
/dev/sda1        12G   10G  1.5G  88% /home
/dev/sda10      921M   12K  858M   1% /mnt/spare/sda10
/dev/sda11       19G   24K   18G   1% /mnt/future/home
/dev/sda12      921M  122M  736M  15% /ubuntu-14.04/boot_partition
/dev/sda13      4.5G  8.0K  4.2G   1% /mnt/spare/sda13
/dev/sda14      9.1G  5.1G  3.6G  59% /ubuntu-14.04/var/www
/dev/sda15       19G   14G  3.6G  80% /ubuntu-14.04
/dev/sda16       46G   15G   29G  34% /ubuntu-14.04/home
/dev/sda17      216G   28K  205G   1% /mnt/future
/dev/sda2        92M   14K   85M   1% /mnt/spare/sda2
/dev/sda3       217G   43G  163G  21% /
/dev/sda5        23G   13G  9.4G  57% /usr/local/tar
/dev/sda7       4.5G  887M  3.4G  21% /mnt/spare/sda7
/dev/sda8       4.5G  594M  3.7G  14% /mnt/spare/sda8
/dev/sda9       4.5G   12K  4.2G   1% /mnt/spare/sda9
$
$ dfh | grep sda | grep -v 14.04 | grep -v spare | grep -v future
/dev/sda3       217G   43G  163G  21% /
/dev/sda1        12G   10G  1.5G  88% /home
/dev/sda5        23G   13G  9.4G  57% /usr/local/tar
$
$ dfh | grep 14.04
/dev/sda15       19G   14G  3.6G  80% /ubuntu-14.04
/dev/sda14      9.1G  5.1G  3.6G  59% /ubuntu-14.04/var/www
/dev/sda12      921M  122M  736M  15% /ubuntu-14.04/boot_partition
/dev/sda16       46G   15G   29G  34% /ubuntu-14.04/home
$
$ dfh | grep spare | sort
/dev/sda10      921M   12K  858M   1% /mnt/spare/sda10
/dev/sda13      4.5G  8.0K  4.2G   1% /mnt/spare/sda13
/dev/sda2        92M   14K   85M   1% /mnt/spare/sda2
/dev/sda7       4.5G  887M  3.4G  21% /mnt/spare/sda7
/dev/sda8       4.5G  594M  3.7G  14% /mnt/spare/sda8
/dev/sda9       4.5G   12K  4.2G   1% /mnt/spare/sda9
$
$ dfh | grep future
/dev/sda17      216G   28K  205G   1% /mnt/future
/dev/sda11       19G   24K   18G   1% /mnt/future/home
$
```

**Note that there are *plenty* of partitions in which to install a new version, while allowing for *saving the old one!!* **


# Suggested Installation Process

Although it's tempting to overwrite the 16.04 files, *there is no reason to do so!*

**Suggested Process**

TODO: Consider what we will want to use bette for:

- Continue using it strictly for listening to music?
- Use barbara for listening to music, and use bette for something else?
  - Poor barbara has only a few Gig of memory, it gets overwhelmed doing even mild browsing
  - bette has 8 Gig of memory, and might be better used for something else?
  - bette currently uses only a few Gig of to play music, and has a lot left over
    - Maybe use bette for browsing as well as playing music?

Something to think about this year!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

**COPIED THE FOLLOWING DETAILS FROM:**

- `../2026a-fresh_install_of_26.04-jane/1-install_26.04-jane.md`.

**CHANGE THESE DETAILS AFTER ANALYZING BETTE'S PARTITIONS NEXT YEAR**

- 1. Use the 1G in `/dev/sdc11` as the `/boot` directory for 26.04
- 1. Use the 23G in `/dev/sdc7 ` as the `/home` directory for 26.04
- 1. Carve up the 173G in `/dev/sdc14` into these new partitions:
  - 41G for `/` for 26.04

  - 1G for `/mnt/spare/boot_for_next_time_1`
  - 24G for `/mnt/spare/home_for_next_time_1`
  - 41G for `/mnt/spare/slash_for_next_time`

  - 1G for `/mnt/spare/boot_for_next_time_2`
  - 24G for `/mnt/spare/home_for_next_time_2`
  - 41G for `/mnt/spare/slash_for_next_time`

  - [X] Check: (41*3) + ((1+24)*2) = 123 + 50 = 173


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Possible template for use next year:

# Preparations

- [ ] Update `tarHome` to backup most relevant files for adding to new install
- [ ] Run `tarHome` on jane to be sure we have the latest
- [ ] Review the procedure here:
  - https://documentation.ubuntu.com/server/how-to/software/upgrade-your-release/index.html

Extra steps taken, because they seem to make sense to me:

- [ ] Closed chrome windows and tabs that I no longer "need"
- [ ] Rebooted and exited Chrome, leaving only a couple of Konsole windows open

Doing the install:

[ ] TBD


