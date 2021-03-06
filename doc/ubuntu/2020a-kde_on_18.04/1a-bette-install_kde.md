
# 1a-bette-install_kde.md

I like using KDE on jane.

This file is about installing KDE side-by-side with gnome on bette, which is already running Ubuntu 18.04.

# References

These are listed in the order in which they came up when searching duckduckgo for "how to install kde on ubuntu 18.04" .

1. tasksel & kubuntu-desktop & sddm
  - https://vitux.com/how-to-install-the-kde-plasma-desktop-on-ubuntu-18-04-lts/
  - https://linuxconfig.org/how-to-install-kde-plasma-desktop-on-ubuntu-18-04-bionic-beaver-linux

2. kde-full | kde-standard | kde-plasma-desktop & sddm
  - https://itsfoss.com/install-kde-on-ubuntu/

3. kde-plasma-desktop & sddm
  - https://www.configserverfirewall.com/ubuntu-linux/ubuntu-install-kde/

4. ~~tasksel & kde-desktop and tasksel & kubuntu-desktop and software-properties-common~~
  - https://kifarunix.com/install-kde-plasma-on-debian-10-9-ubuntu-18-04/
  - Eliminating this reference from further consideration
    - Their process is a little confusing, because at the end it calls for optionally running add-apt-repository ppa:kubuntu-ppa/backports
    - Why??  This is unclear.
    - Moreover, I want to avoid using add-apt-repository ppa:kubuntu-ppa/backports if at all possible, so it is suspicious

5. tasksel & kubuntu-desktop
  - https://www.fossmint.com/install-kde-plasma-on-ubuntu/ -- contains two slightly different processes

6. just plasma-desktop
  - https://www.fossmint.com/install-kde-plasma-on-ubuntu/ -- contains two slightly different processes
  - "This method neither edits your bootup configuration nor does it install any unnecessary dependencies."

7. tasksel & kubuntu-desktop OR plasma-desktop
  - https://itsubuntu.com/install-latest-kde-plasma-ubuntu-18-04/

8. kubuntu-desktop & sddm
  - https://www.osradar.com/how-to-install-kde-plasma-on-ubuntu-18-04/
  - Includes commands to use to delete it

9. ~~plasma-desktop OR kde-plasma-desktop & sddm~~
  - https://askubuntu.com/questions/999244/how-to-install-kde-plasma-without-installing-full-kubuntu-desktop
  - Eliminating this reference from further consideration
    - The person installed "Kubuntu Desktop" on 17.10 and claims it made his PC run slow, so he uninstalled it
    - They want the plasma look without all the other stuff
    - I have plenty of disk space and am fine with installing the full kubuntu desktop

10. ~~add-apt-repository ppa:kubuntu-ppa/backports & plasma-desktop OR kde-full OR kde-standard~~
  - https://www.how2shout.com/how-to/how-install-kde-plasma-5-17-de-on-ubuntu-18-04-or-19-10.html
  - Eliminating this reference from further consideration
    - I want to avoid using add-apt-repository ppa:kubuntu-ppa/backports if at all possible
    - The author is either careless or does not know English very well

11. tasksel & kubuntu-desktop & sddm
  - https://linuxtips.us/install-kde-plasma-ubuntu-18-04/

12. tasksel & kubuntu-desktop & sddm
  - https://wpcademy.com/how-to-install-kde-plasma-on-ubuntu-18-04-lts/

# Analysis

Definitely seeing a bit of variety in the results but also quite a bit of similarity.
I am happy with what I have now on bette but want to try out KDE on it because I am digging what I now have on jane with 20.04.

## Plenty of Space!

There is plenty of space in `/`:

```
/dev/sda3       217G   35G  171G  17% /   ## "plenty of space" is an understatement!
```

Not sure why I set things up this way, hmmm.  Must have gotten tired of slicing and dicing the disk.

So I want to "play it safe," which means not cutting any corners, which in turn means installing `tasksel` for sure.

## Which Package to Install?

Should I install `kde-desktop` or `kde-plasma-desktop` or `kde-full` or `plasma-desktop` or ???

### Outliers:

The `kde-standard` package appears only as an optional suggestion, as opposed to the main suggestion, in #2 and [#10].

At first I thought `kde-full` sounded good because I have plenty of space and want to recreate
what I have after installing kubuntu on jane.
But now looking more closely at the references, `kde-full` appears in only two of them, #2 and [#10].

Also, `kde-plasma-desktop` appears in only three of the references, #2, #3, and [#9].

Interestingly, `plasma-desktop` appears in four of the references, #6, #7, [#9], and [#10] --
but two are no longer under consideration.

### Most Popular Option: `kubuntu-desktop`

The most popular option is `kubuntu-desktop` , which appears in eight of the twelve references:
#1, [#4], #5, #6, #7, #8, #11, and #12.

- Note that #1 actually contains two references, but we only count it as one
- Note that in [#9] the user claims this slowed down his PC when they installed it on 17.10

Let's pick this one, `kubuntu-desktop` .

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

