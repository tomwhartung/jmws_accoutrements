
# 2a-barbara-install_kde.md

I like using KDE on jane.

This file is about installing KDE side-by-side with gnome on barbara, which is already running Ubuntu 18.04.

# References

See `1a-bette-install_kde.md` in this directory.

# Analysis

Definitely seeing a bit of variety in the results but also quite a bit of similarity.
I am happy with what I have now on bette but want to try out KDE on it because I am digging what I now have on jane with 20.04.

## Making Room

Doing this on bette took up 2G space.  We do not have that on barbara

```
/dev/sda8        13G  9.6G  2.6G  79% /
/dev/sda12      4.5G  9.4M  4.3G   1% /mnt/spare/sda13
```

Moving the contents `/var/lib`, which is using about 3.1G of space, into the formerly spare partition `/dev/sda12` ,
which is currently mounted on `/mnt/spare/sda13` , because I fucked up.


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

[x] This step appears to have completed ok.

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

