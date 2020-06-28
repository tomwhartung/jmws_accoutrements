
# 2a-ava.md

Upgrading ava by installing into existing `/mnt/future*` and `/mnt/spare*` partitions

# Upgrading to Kubuntu 20.04 LTS (Focal Fossa)

Install kubuntu desktop 20.04 LTS while Leaving existing OS as-is - if possible.


# Disk Partitions

## Partitions Before

```
/dev/sda10      4.5G  9.4M  4.2G   1% /mnt/future/home
/dev/sda11       20G  2.2G   16G  12% /var/www
/dev/sda12      931M  1.3M  866M   1% /mnt/spare/sda12
/dev/sda14      4.5G  357M  3.9G   9% /usr/src
/dev/sda16      4.5G  119M  4.1G   3% /var/cache
/dev/sda17      4.5G  781M  3.5G  19% /var/log
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
/dev/sda19       91G   38G   49G  44% /usr/local/tar
/dev/sda5        22G  2.5G   19G  12% /
/dev/sda6       931M  109M  758M  13% /boot
/dev/sda7       4.5G  177M  4.1G   5% /home
/dev/sda8        22G   44M   21G   1% /mnt/future
/dev/sda9       931M  1.2M  866M   1% /mnt/future/boot
```

**Also: we can use the three windows 7 partitions, a total of 240G.**

## Partitions After Harvesting Spares

Moved files in all partitions containing 16.04 files, e.g., `/var/www`, `/usr/src`, `/home`, etc.
**except the `/boot` partition, of course,** to where they belong under `/`, making as many
partitions as possible spare.

```
/dev/sda10      4.5G  9.3M  4.2G   1% /mnt/spare/sda10
/dev/sda11       20G   44M   19G   1% /mnt/spare/sda11
/dev/sda12      931M  1.2M  866M   1% /mnt/spare/sda12
/dev/sda14      4.5G  9.3M  4.2G   1% /mnt/spare/sda14
/dev/sda15      4.5G  9.3M  4.2G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.3M  4.2G   1% /mnt/spare/sda16
/dev/sda17      4.5G  9.3M  4.2G   1% /mnt/spare/sda17
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
/dev/sda19       91G   38G   49G  44% /usr/local/tar
/dev/sda5        22G  6.0G   15G  29% /
/dev/sda6       931M  109M  758M  13% /boot
/dev/sda7       4.5G  9.3M  4.2G   1% /mnt/spare/sda7
/dev/sda8        22G   44M   21G   1% /mnt/spare/sda8
/dev/sda9       931M  1.2M  866M   1% /mnt/spare/sda9
```

Hoping I can consolidate these....

## Partitions at Install Time

Was able to consolidate partitions sda8-sda19 into new unallocated space

Leaving sda7 spare for now, in memory of the old times, and for use as swap.

```
/dev/sda5        22G  6.0G   15G  29% /
/dev/sda6       931M  109M  758M  13% /boot
/dev/sda7       4.5G  9.3M  4.2G   1% /mnt/spare/sda7
```

## Partitions - Proposed

```
/dev/sda1      12.6G  0.0M 12.6G   1% /home
/dev/sda2       301M  EFI partition (*)
/dev/sda3       258G  0.0M  258G   1% /
/dev/sda4        [extended]
/dev/sda5        22G  2.5G   19G  12% /ubuntu-16.04/
/dev/sda6       931M  109M  758M  13% /ubuntu-16.04/boot
/dev/sda7        16G swap partition (**)
/dev/sda8       188G  0.0M  188G   1% /mnt/spare/sda8
```

### (*) EFI Partition or /boot?

Are they related, mutually exclusive, or maybe even the same thing?

#### References

- (1) https://askubuntu.com/questions/353683/uefi-partitioning-for-dummies#353780
- (2) https://www.diskpart.com/articles/efi-system-partition-4348.html
- (3) https://en.wikipedia.org/wiki/EFI_system_partition
- (4) https://linuxsuperuser.com/how-to-restore-or-create-efi-partition-in-ubuntu/
- (5) https://en.wikipedia.org/wiki/EFI_system_partition
- (6) https://www.ctrl.blog/entry/esp-size-guide.html

#### Deliberations

I was ready to install but it complained about not having an EFI partition, saying the computer may not boot.

I believe it thinks I need an EFI partition because I had windows 7 on there, but am overwriting it with the new OS.
This is because it is formatted as FAT, which is not something a linux system needs, but I may be mistaken, see reference (4).

On the other hand, after reading the references, it may be it just needs a /boot partition.
I typically create a small, 1G partition for /boot, but bette does not have one.  Why have one if I don't need it?
The /boot partitions on jane and barbara are 1G and 2G respectively, and use only about 200M.

#### Decision 1

Using the 300M sda2 partition for this purpose is no real sacrifice, even if it is just to keep a bogus warning message from showing up.
That is probably what Windows used this tiny partition for, anyway.

Reference (6) suggests that 300M is plenty of room for it, no matter what the OS.
In the table, the entry for ubuntu claims it needs only 4.9 MB but the default partition size is 513 MB.
Surely 300M is big enough, I hope.

##### Oops!  Try Again!!

After setting /dev/sda2 as an EFI the installer seemed to be happy, and progressed tot he next step, then a popup appeared saying
"The attempt to mount a file system with type vfat in partition #2 at /boot/efi failed."
Looks like I need to try again.

#### Decision 2

After looking into the swap issue, and deciding it can't hurt -- see below.

And after looking at the partition scheme the installer suggests, I have decided to use that.

**See the section entitled "Partitions - Suggested and Accepted" below."

### (**) Do I Need a Swap Partition?

#### References

- (1) https://www.tecmint.com/install-ubuntu-20-04-desktop/
- (2) https://linuxconfig.org/how-to-install-ubuntu-20-04-focal-fossa-desktop
- (3) https://askubuntu.com/questions/398258/do-i-need-a-swap-partition
- (4) https://askubuntu.com/questions/49109/i-have-16gb-ram-do-i-need-32gb-swap

#### Deliberations

At first I thought, no.
Then I thought, why not use the 5G sda7?

After checking the references below, which mostly say yes, I am re-thinking the issue.
The references agree that at worst it cannot hurt, provided you have plenty of space, which I do in fact have.
And at best it can save your system from crashing should a process want more memory than there is currently available.
They also agree that I should make it twice as big as your memory.

#### Decision

Delete the spare sda7 partition, create 16G swap partition out of unallocated space, and use the remainder to create a spare sda8 partition.

## Partitions - Suggested and Accepted

The installer suggests a partition scheme similar to what I have in mind.
Since it is suggesting this scheme, presumably it will work without the errors I have been encountering.

### Suggested Partitions

The default option, "Guided - resize SCSI1 (0,0,0), partition #3 (sda) and use freed space" is similar to what's under the section
entitled "Partitions - Proposed" above.

They suggest doing the following:

- Format `sda1` as ext4
- Somehow split `sda3` into two partitions
  - Formatting `sda3` as 132.4G of ext4
  - Installing "Kubuntu (auto)" in 125.4G of ext4
  - Interestingly, there's a slider between these two partitions, allowing me to shrink one and grow the other
- Leaving Ubuntu 16.04 alone
- Also presumably leaving the Ubuntu 16.04 /boot 1G partition alone
- Formating `sda7` as 16G of swap
- Presumably leaving the remaining unallocated space alone

### Accepted Partitions

This actually makes a lot of sense.

However, why not use the slider between the `sda3` and "Kubuntu (auto)" partitions to make the "Kubuntu (auto)" partition larger?

**Using the slider to:**

- Make the `sda3` smaller, about 60G
- Make the "Kubuntu (auto)" partition larger, about 200G, which is about the size of the free space we still have

**Make it so.**  Done, captain!

Clicking on "Install Now."

## Partitions After

```
```

