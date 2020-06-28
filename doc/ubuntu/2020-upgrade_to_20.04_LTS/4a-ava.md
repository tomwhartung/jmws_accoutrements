
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

### Feedback

Now there is a popup warning it will:

- Format "partition #9 of SCSI1 (0, 0, 0) (sda) as ESP"
   - Note that this is just another name for EFI, which caused me to rethink all this
- Format ""partition #10 of SCSI1 (0, 0, 0) (sda) as ext4"

It says nothing about the size of these partitions, and I am curious about that, so rats.
But this is what it wants to do!

Clicking on "Continue."

## Fatal Error!

Now we have a new popup!

- Title: "Unable to install GRUB in /dev/sda"
- Body: "Executing `grub-install /dev/sda' failed.  This is a fatal error"

Rut-roh!!

Now we have a new popup!

- Title: "Installation failed - KDialog ?"
- Body: "The installer encountered an unrecoverable error.  A desktop session will not be run so that you may investigate the problem or try installing again."

Idea: try again, this time don't use the slider.

## Trying Again

Now we have a new popup!

- Title: "ubi-partman crashed"
- Body: "ubi-partman crashed with exit code 10.  Further information may be found in /var/log/syslog.  Do you want to try running this step again before continuing?  If you do not, your installation may fail entirely or may be broken"
- Buttons: Retry, Ignore, Close

The `syslog` is no help.

This post for 18.04 has a suggestion:

- https://askubuntu.com/questions/1032905/ubi-partman-failed-with-exit-code-10-ubuntu-18-04

Interestingly, it has to do with having an EFI partition.

Picking Retry causes the same dialog to appear.

Picking Close.

## Trying the Suggestion from Askubuntu.com

Trying the fixes from this post:

- https://askubuntu.com/questions/1032905/ubi-partman-failed-with-exit-code-10-ubuntu-18-04

There are two, but they are very similar.
It's worth a shot!

### Attempting to Fix It

- [x] Installing GParted, hope this works
- [x] Changed sda2 to FAT32, because I thought that is what the post wanted me to do.
      - Right clicking on it does not show any options to edit the partition, rats
- [x] Right clicking on sda9, which is already 512M of FAT32, allows me to manage flags
      - The boot and esp flags are already set
      - Clearing both of these flags
- [x] Looking at sda2 again, I can right click on it and change things
      - Setting the boot and esp flags
      - Setting the label to "EFI" as the post suggests

Thinking maybe this crapped out because it tried to use sda9 as the EFI partition, when sda9 is not a **primary partition.**

Thinking maybe that sda2 is a **primary partition** so it ~~will~~ might (don't want to get overconfident and jinx it!) succeed this time.

Things I notice in gparted:

- /dev/sda3 is a primary partition, 55.75G of ext4
- /dev/sda7 is a secondary partition, 14.9G of 'linux-swap' space
- /dev/sda10 is a secondary partition, 183.9G of ext4, mounted on /target

Exiting gparted and running through the installation again.

### Start From "Scratch"

Getting the same error: "ubi-partman crashed with exit code 10...."

The syslog says that it cannot unmount /target because it is busy, and trying to unmount it in gparted causes the same error.

**Time to reboot and try again.**  Sometimes a crashed process can make the OS think it's using a partition, when it really isn't, is what I'm thinking.

### Start "Fresh"

Partition manager shows the disks as they did above, with out sda10 being mounted on /target .

Install -> Disk Setup step shows it is very confused....

- It sees "Ubuntu 16.04" and "Ubuntu 20.04" in the Before picture
- It sees "Ubuntu 20.04" and "Kubuntu (auto)" in the After picture
- The slider trades space between the "Ubuntu 20.04" and "Kubuntu (auto)" partitions, weird

Picking the "Guided - use entire disk" option.

- Single partition using 500.1 GB for Kubuntu

Clicking on "Install Now."

Interestingly, the popup says:

- partition #1 of SCSI1 (0, 0, 0) (sda) as ESP
- partition #2 of SCSI1 (0, 0, 0) (sda) as ext4

Interesting because I think it is the ESP bit that got me into all this trouble in the first place.
Live and learn.

## Partitions After Install

```
/dev/sda1       511M  7.8M  504M   2% /boot/efi
/dev/sda2       457G  8.1G  416G   2% /
```

