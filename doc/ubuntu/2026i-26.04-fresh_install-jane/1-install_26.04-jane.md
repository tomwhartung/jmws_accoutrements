
# 1-install_26.04-jane.md

Time to install 26.04 on jane.

- **See the *Suggested Installation Process* appearing after the following analysis of *Jane's Disk Partitions* **

# Jane's Disk Partitions

Installing 26.04 should be straightforward and safe because jane has a lot of
**spare disk partitions.**

- These partitions are designed to make installing new versions easy

## Why These Partitions Make Intalls Easy

Here's a sorted list of the current partitions:

**Note that there are three groups of three partitions.**

- the currently used `/`, `/boot`, and `/home` partitions
- `/ubuntu-16.04*` `/`, `/boot`, and `/home` partitions
- `/mnt/spare/sda*` `/`, `/boot`, and `/home` partitions

These partitions have sizes that *corresponding somewhat* to each other in that each group has:

- a 1G partition for `/boot`
- a 23G partition for `/home/`:
- a 55G (current), a 23G (16.04), and a 173G (spare) partition for `/`

## `df` Command Output

The following code listings show all partitions followed by a list of each of the previously mentioend three groups of three.

```
 $ df | grep sdc
/dev/sdc1       923M  108M  752M  13% /ubuntu-16.04-boot
/dev/sdc2       924M  254M  623M  29% /boot
/dev/sdc6        23G   12G  9.9G  55% /ubuntu-16.04
/dev/sdc7        23G  156K   22G   1% /mnt/spare/sda7
/dev/sdc8        23G  6.0G   16G  28% /ubuntu-16.04-home
/dev/sdc9        23G   16G  5.7G  74% /home
/dev/sdc10       19G  9.0G  8.3G  53% /var/www
/dev/sdc11      923M   44K  876M   1% /mnt/spare/sda11
/dev/sdc12       92G   16G   72G  18% /usr/local/tar
/dev/sdc13       55G   19G   33G  37% /
/dev/sdc14      173G  1.1M  164G   1% /mnt/spare/sda14
 $
```

First, the currently used `/`, `/boot`, and `/home` partitions:

```
 $ df / /boot /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc13       55G   19G   33G  37% /
/dev/sdc2       924M  254M  623M  29% /boot
/dev/sdc9        23G   16G  5.7G  74% /home
 $
```

Here are the `/`, `/boot`, and `/home` partitions used by an old installation of 16.04 still hanging around:

```
 $ df | grep ubuntu-16
/dev/sdc8        23G  6.0G   16G  28% /ubuntu-16.04-home
/dev/sdc1       923M  108M  752M  13% /ubuntu-16.04-boot
/dev/sdc6        23G   12G  9.9G  55% /ubuntu-16.04
 $
```

Here are the three spare (`/mnt/spare/*`) `/`, `/boot`, and `/home` partitions:

```
 $ df | grep spare
/dev/sdc11      923M   44K  876M   1% /mnt/spare/sda11
/dev/sdc7        23G  156K   22G   1% /mnt/spare/sda7
/dev/sdc14      173G  1.1M  164G   1% /mnt/spare/sda14
 $
```


# Suggested Installation Process

Although it's tempting to overwrite the 16.04 files, *there is no reason to do so!*

**Suggested Process**

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


