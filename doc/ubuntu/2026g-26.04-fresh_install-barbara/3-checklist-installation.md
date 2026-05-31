
# 3-checklist-installation.md

This version of `3-checklist-installation.md` reflects the steps I am performing to install **Ubuntu 26.04** on `barbara` on **2026-05-17**.


# Installing Ubuntu 26.04

Much of this is quite straightforward, answering several easy no-brainer questions that do not require further comment.

## Running the Install

Following is a list of steps, for future reference, even when it's simple, but has been a while since the last time I did this:

- [X] Shutdown the PC
- [X] Disconnect all external USB storage drives

## **Problems** Running the Install

After repeatedly trying to install 26.04, I finally figured out that **HP has retired this PC!!**

- For details, see `3-checklist-installation-PROBLEMS.md` in this directory

You have to do some drilling down, but by starting on this page I learned that **HP has retired this PC!!**

- https://support.hp.com/us-en/retired-products

This information will help find the current status - i.e., **retired** - of this specific PC:

- Product Name: DC6000
- SKU Number: BZ270US#ABA
- Processor Type: Intel(R) Core(TM)2 Duo CPU E8400 @ 3.00GHz
- System BIOS 786G2 v01.14
- Chassis Serial Number: MXL1220HN4
- Asset Tracking Number: MXL1220HN4
- ME Firmware Virsion 5.2.10.1023
- Management Mode: AMT

## Plan B: Upgrade the Release

Rather than re-installing - which I really wanted to do - I can just use the command line to upgrade the release.

- I did this on `jane` and it caused some issues, so I'd *rather* install 26.04 from scratch
- At this point, however, I really have no choice, because freakin' HP has **retired** my freakin' PC!!

### References

These pages describe how to use the command line on 25.10 to upgrade to 26.04:

- (1) This looks like the preferred, official process:
  - https://discourse.ubuntu.com/t/best-practice-for-a-successful-release-upgrade-to-26-04/80868
  - The only tricky thing looks to be when one has special programs that do not come with plain old vanilla Ubuntu (*)
  - I just installed 25.10 recently, so should not have any issues with any of that
- (2) This is a slightly different process, that for example explains how to check for apps that have been *held back*
  - https://linuxize.com/post/how-to-upgrade-to-ubuntu-26-04/
- (3) This process is one that suggests using `-d` if issues arise, which is something the previous URL cautions against doing:
  - https://www.linuxlookup.com/howto/upgrade_ubuntu_25_10_ubuntu_26_04_lts

(*) From reference (1):

> "The #1 cause of broken upgrades is deb packages from non-Ubuntu sources. It’s 100% preventable."

I do not have anything from a non-Ubuntu source, so we should be good to go.

Also from reference (1):

> "3. Make a 26.04 LiveUSB installer"

I do have that, but it "*hiccups*" on the old BIOS installed on the system, so the whole *retirement* thing *might* be an issue....

In general, I will be combining commands from all three of these pages, and focusing on the core commands that all three references have in common.

### Details

All of these commands must be run as the `root` user.

#### Ensure Everything is Up-To-Date

First check for packages that have been held back.  This command comes from reference (2):

```
apt-mark showhold
```

This output nothing, so we are good to go.

Next do the regular update.  These commands come from all three references:

```
apt update
apt upgrade
```

Everything is up-to-date, no surprises there, so let's continue.

#### Upgrade the Release

Reference (2) recommends running these two commands:

- `apt full-upgrade` - to "*resolve any remaining dependency changes*":
- `apt --purge autoremove` - to "*automatically installed dependencies that are no longer needed*":

```
apt full-upgrade
apt --purge autoremove
```

Again, everything is up-to-date, and there was nothing to remove, so let's continue.

All three references say to run this command:

```
do-release-upgrade
```

- [X] The first time, it said I hadn't rebooted since installing software that required a reboot (oops), so I rebooted
- [X] After the reboot, it did some figurin' and output the following summary:

```
Do you want to start the upgrade?


13 packages are going to be removed. 135 new packages are going to be
installed. 1877 packages are going to be upgraded.

You have to download a total of 2,290 M. This download will take
about 12 minutes with your connection.

Installing the upgrade can take several hours. Once the download has
finished, the process cannot be canceled.

Continue [yN]  Details [d]
```

- [X] I entered 'd' and captured the details in the file `3-do_release_upgrade-output.txt`



## Continuing With the Original Checklist

Following are the original checklist's items, for possible future reference ... but it's now looking more and more like I will not do this after all....

- [ ] Running the install on **2026-05-??** at **??:?? PM**
  - [ ] Answer these easy no-brainer questions
    - *Choose your language* - English
    - *Accessibility in Ubuntu* - None
    - *Select your keyboard layout* - English (US)
    - *Connect to the internet* - Use wired connection
    - *What do you want to do with Ubuntu?* - Install Ubuntu
    - *How would you like to install Ubuntu?* - Ineractive Installation
    - *What apps would you like to install to start with?* - Extended selection
    - *Install recommended proprietary software?*
      - [X] Install third-party software for graphics and Wi-Fi hardware
      - [ ] Download and install support for additional media formats - *this option is unavailable and greyed-out*
    - *How do you want to install Ubuntu?* - Erase disk and install Ubuntu
    - *Encryption and file system* - No encryption
    - *Create your account*
      - Your name: Tom H
      - Your computer's name: barbara
      - Your username: tomh
      - Password: tomh
      - Confirm password: tomh
      - [ ] Require my passowrd to log in - **Uncheck**
      - [ ] Use Active Directory - Leave unchecked
    - *Select your timezone* - Denver
    - *Review your choices*
      - Erase disk and install Ubuntu, etc.
  - [ ] Clicking the **Install** button at **[note the time here]**
  - [ ] Install finished at **[note the time here]**
  - [ ] Clicking the **Restart now** button
  - [ ] Please remove the installation medium, then press ENTER:

