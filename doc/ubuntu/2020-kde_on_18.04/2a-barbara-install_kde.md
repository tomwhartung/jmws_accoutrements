
# 2a-barbara-install_kde.md

I like using KDE on jane.

This file is about installing KDE side-by-side with gnome on barbara, which is already running Ubuntu 18.04.

# References

See `1a-bette-install_kde.md` in this directory.

# Analysis

Definitely seeing a bit of variety in the results but also quite a bit of similarity.
I am happy with what I have now on bette but want to try out KDE on it because I am digging what I now have on jane with 20.04.

## Making Room

Doing this on bette took up 2G space.  We do not have that on barbara.

Before moving the contents of `/var/lib`, which is using about 3.1G of space, into the formerly spare partition `/dev/sda12` ,
which is currently mounted on `/mnt/spare/sda13` , because I fucked up.

```
/dev/sda8        13G  9.6G  2.6G  79% /
/dev/sda12      4.5G  9.4M  4.3G   1% /mnt/spare/sda13
```

After moving the contents `/var/lib` into the formerly spare partition `/dev/sda12` ,

```
/dev/sda8        13G  6.2G  6.0G  51% /
/dev/sda12      4.5G  3.5G  756M  83% /var/lib
```

The `/var/lib` partition is tight, but ok, so let us proceed.
Hopefully `/var/lib` won't fill up and ruin everything!

## Which Package to Install?

Based on the Analysis in `1a-bette-install_kde.md` in this directory, we will install `kubuntu-desktop` .

# Proposed Process Plan

Here is what I will try.  May need to adjust this as necessary.

## Install `tasksel`

Assuming `tasksel` is short for "task selection."
I definitely want to be able to choose between KDE and Gnome, so I can return to the old familar UI anytime I want.

Seven of the eight references -- i.e., all but [#8] -- that recommend `kubuntu-desktop` also recommend installing `tasksel` first.

```
apt install tasksel
```

[x] so far so good

## Install `kubuntu-desktop`

Use `tasksel` to install `kubuntu-desktop`

```
tasksel install kubuntu-desktop
```

This is where it goes into GUI mode.  The references contain plenty of screenshots of this.

**This step appears to have FAILED!**

Not sure, but it looks bad.

**NOTE THAT WE ARE GOING TO INSTALL 20.04 SERVER HERE ANYWAY!!**

So, ultimately, it's no biggie and not worth sweating over.

Output of running the `tasksel` command, a few times:

```
root@barbara: ~
$ tasksel install kubuntu-desktop
E: Unable to correct problems, you have held broken packages.
root@barbara: ~
$ tasksel install kubuntu-desktop
xserver-xorg					install
root@barbara: ~
$ tasksel install kubuntu-desktop
xserver-xorg					install
root@barbara: ~
$ tasksel install kubuntu-desktop
xserver-xorg					install
root@barbara: ~
$
```

Not sure what it is trying to tell me!

Disk space looks ok:

```
$ dfh . lib
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda8        13G  7.0G  5.3G  58% /
/dev/sda12      4.5G  3.5G  744M  83% /var/lib
```

Searching for the error message `E: Unable to correct problems, you have held broken packages.`
led to trying a few things, that did not seem to help.

I examined the following urls that I found by searching duckduckgo for
"tasksel install kubuntu-desktop E: Unable to correct problems, you have held broken packages."

- https://askubuntu.com/questions/223237/unable-to-correct-problems-you-have-held-broken-packages#223267
- https://askubuntu.com/questions/164587/how-can-you-unhold-remove-a-hold-on-a-package
- https://www.linux.org/threads/kde-plasma-instead-of-compiz.26078/
- https://appuals.com/fix-unable-correct-problems-held-broken-packages/
- https://www.linuxquestions.org/questions/linux-desktop-74/unable-to-correct-problems-you-have-held-broken-packages-4175510237/
- http://forums.debian.net/viewtopic.php?t=125122

The things I tried, and the output:

```
root@barbara: ~
$ dpkg --get-selections | grep hold
root@barbara: ~
$ apt-get update
Ign:1 http://dl.google.com/linux/chrome/deb stable InRelease
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Hit:3 http://dl.google.com/linux/chrome/deb stable Release
Hit:4 http://us.archive.ubuntu.com/ubuntu bionic InRelease
Hit:5 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic InRelease
Get:7 http://us.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
Get:8 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [40.7 kB]
Get:9 http://us.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
Get:10 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [42.0 kB]
Get:11 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]
Get:12 http://us.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [303 kB]
Get:13 http://us.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [273 kB]
Get:14 http://us.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B]
Get:15 http://us.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [7,972 B]
Fetched 923 kB in 7s (128 kB/s)
Reading package lists... Done
root@barbara: ~
$ apt-get upgrade -y
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@barbara: ~
$ apt-get autoremove
Reading package lists... Done
Building dependency tree
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@barbara: ~
$ apt list tasksel
Listing... Done
tasksel/bionic,bionic,now 3.34ubuntu11 all [installed]
root@barbara: ~
$ apt list sddm
Listing... Done
sddm/bionic,now 0.17.0-1ubuntu7 amd64 [installed]
root@barbara: ~
$ apt list xserver-xorg
Listing... Done
xserver-xorg/bionic-updates,now 1:7.7+19ubuntu7.1 amd64 [installed]
N: There is 1 additional version. Please use the '-a' switch to see it
root@barbara: ~
$ apt list xserver-xorg -a
Listing... Done
xserver-xorg/bionic-updates,now 1:7.7+19ubuntu7.1 amd64 [installed]
xserver-xorg/bionic 1:7.7+19ubuntu7 amd64

root@barbara: ~
$ dpkg –configure -a
dpkg: error: need an action option

Type dpkg --help for help about installing and deinstalling packages [*];
Use 'apt' or 'aptitude' for user-friendly package management;
Type dpkg -Dhelp for a list of dpkg debug flag values;
Type dpkg --force-help for a list of forcing options;
Type dpkg-deb --help for help about manipulating *.deb files;

Options marked [*] produce a lot of output - pipe it through 'less' or 'more' !
root@barbara: ~
$ dpkg -configure -a
dpkg: error: unknown option -o

Type dpkg --help for help about installing and deinstalling packages [*];
Use 'apt' or 'aptitude' for user-friendly package management;
Type dpkg -Dhelp for a list of dpkg debug flag values;
Type dpkg --force-help for a list of forcing options;
Type dpkg-deb --help for help about manipulating *.deb files;

Options marked [*] produce a lot of output - pipe it through 'less' or 'more' !
root@barbara: ~
$ dpkg --configure -a
root@barbara: ~
$ apt-get install -f
Reading package lists... Done
Building dependency tree
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@barbara: ~
$ apt-get update
Ign:1 http://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 http://dl.google.com/linux/chrome/deb stable Release
Hit:3 http://security.ubuntu.com/ubuntu bionic-security InRelease
Hit:4 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic InRelease
Hit:5 http://us.archive.ubuntu.com/ubuntu bionic InRelease
Hit:7 http://us.archive.ubuntu.com/ubuntu bionic-updates InRelease
Hit:8 http://us.archive.ubuntu.com/ubuntu bionic-backports InRelease
Reading package lists... Done
root@barbara: ~
$ apt-get upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@barbara: ~
$ which synaptic
/usr/sbin/synaptic
root@barbara: ~
$ apt-get autoclean
Reading package lists... Done
Building dependency tree
Reading state information... Done
Del google-chrome-stable 81.0.4044.113-1 [67.1 MB]
Del google-chrome-stable 81.0.4044.122-1 [66.7 MB]
Del google-chrome-stable 81.0.4044.92-1 [66.7 MB]
root@barbara: ~
$ apt-get clear cache
E: Invalid operation clear
root@barbara: ~
$ apt-cache policy
Package files:
 100 /var/lib/dpkg/status
     release a=now
 500 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic/main i386 Packages
     release v=18.04,o=LP-PPA-ubuntuhandbook1-audacity,a=bionic,n=bionic,l=Audacity Audio Editor and Recorder,c=main,b=i386
     origin ppa.launchpad.net
 500 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic/main amd64 Packages
     release v=18.04,o=LP-PPA-ubuntuhandbook1-audacity,a=bionic,n=bionic,l=Audacity Audio Editor and Recorder,c=main,b=amd64
     origin ppa.launchpad.net
 500 http://dl.google.com/linux/chrome/deb stable/main amd64 Packages
     release v=1.0,o=Google LLC,a=stable,n=stable,l=Google,c=main,b=amd64
     origin dl.google.com
 500 http://security.ubuntu.com/ubuntu bionic-security/multiverse i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=multiverse,b=i386
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=multiverse,b=amd64
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/universe i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=universe,b=i386
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=universe,b=amd64
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/restricted i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=restricted,b=i386
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=restricted,b=amd64
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/main i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=main,b=i386
     origin security.ubuntu.com
 500 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-security,n=bionic,l=Ubuntu,c=main,b=amd64
     origin security.ubuntu.com
 100 http://us.archive.ubuntu.com/ubuntu bionic-backports/universe i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-backports,n=bionic,l=Ubuntu,c=universe,b=i386
     origin us.archive.ubuntu.com
 100 http://us.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-backports,n=bionic,l=Ubuntu,c=universe,b=amd64
     origin us.archive.ubuntu.com
 100 http://us.archive.ubuntu.com/ubuntu bionic-backports/main i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-backports,n=bionic,l=Ubuntu,c=main,b=i386
     origin us.archive.ubuntu.com
 100 http://us.archive.ubuntu.com/ubuntu bionic-backports/main amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-backports,n=bionic,l=Ubuntu,c=main,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/multiverse i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=multiverse,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=multiverse,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=universe,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=universe,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/restricted i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=restricted,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=restricted,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=main,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic-updates,n=bionic,l=Ubuntu,c=main,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/multiverse i386 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=multiverse,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=multiverse,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/universe i386 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=universe,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=universe,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/restricted i386 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=restricted,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/restricted amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=restricted,b=amd64
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/main i386 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=main,b=i386
     origin us.archive.ubuntu.com
 500 http://us.archive.ubuntu.com/ubuntu bionic/main amd64 Packages
     release v=18.04,o=Ubuntu,a=bionic,n=bionic,l=Ubuntu,c=main,b=amd64
     origin us.archive.ubuntu.com
Pinned packages:
```

The mix of amd64 and i386 in the output looks suspicious!!  But I am not sure what it means....

I also tried to find broken packages in synaptic:

- Custom Filters [Button near the bottom] -> Broken [Option above the buttons]

Nothing shows up.

**STOPPING HERE, HOPEFULLY I HAVE NOT MESSED THINGS UP TOO BADLY!!**

**NOT RUNNING THE `sddm` STEP FOR NOW!!**

**WILL HOLD OFF ON REBOOTING FOR NOW...!!!**

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## If Necessary, Run the `sddm` Step

The references are a bit ambiguous about this step.

- Some of the references do not mention it
- The ones that do, claim it should run automatically
- Some claim to install sddm manually, if it is not already installed
  - It is already installed:

```
# apt list sddm
Listing... Done
sddm/bionic,now 0.17.0-1ubuntu7 amd64 [installed]
```

Reinstalling it simply confirms that `sddm is already the newest version (0.17.0-1ubuntu7).`

Some of those that do -- #1, etc. -- mention it also mention this workaround.
The idea is to set sddm to run as the default choice, rather than gdm3 -- I also have lightdm, which was selected.

```
dpkg-reconfigure sddm
```

Ok, it seems to have run ok.  Now I need to log out or reboot -- or both.

