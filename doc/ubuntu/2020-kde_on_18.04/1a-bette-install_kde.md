
# 1a-bette-install_kde.md

I like using KDE on jane.

This file is about installing KDE side-by-side with gnome on bette, which is already running Ubuntu 18.04.

# References

These are listed in the order in which they came up when searching duckduckgo for "how to install kde on ubuntu 18.04" .

- tasksel & kubuntu-desktop & sddm
  - https://vitux.com/how-to-install-the-kde-plasma-desktop-on-ubuntu-18-04-lts/
  - https://linuxconfig.org/how-to-install-kde-plasma-desktop-on-ubuntu-18-04-bionic-beaver-linux

- kde-full | kde-standard | kde-plasma-desktop & sddm
  - https://itsfoss.com/install-kde-on-ubuntu/

- kde-plasma-desktop & sddm
  - https://www.configserverfirewall.com/ubuntu-linux/ubuntu-install-kde/

- tasksel & kde-desktop and tasksel & kubuntu-desktop and software-properties-common
  - https://kifarunix.com/install-kde-plasma-on-debian-10-9-ubuntu-18-04/
  - A little confusing, also runs add-apt-repository ppa:kubuntu-ppa/backports

- tasksel & kubuntu-desktop & sddm
  - https://www.fossmint.com/install-kde-plasma-on-ubuntu/

- tasksel & kubuntu-desktop & plasma-desktop
  - https://www.fossmint.com/install-kde-plasma-on-ubuntu/

- tasksel & kubuntu-desktop OR plasma-desktop
  - https://itsubuntu.com/install-latest-kde-plasma-ubuntu-18-04/

- kubuntu-desktop & sddm
  - https://www.osradar.com/how-to-install-kde-plasma-on-ubuntu-18-04/
  - Includes commands to use to delete it

- plasma-desktop OR kde-plasma-desktop & sddm
  - https://askubuntu.com/questions/999244/how-to-install-kde-plasma-without-installing-full-kubuntu-desktop

- add-apt-repository ppa:kubuntu-ppa/backports & plasma-desktop OR kde-full OR kde-standeard
  - https://www.how2shout.com/how-to/how-install-kde-plasma-5-17-de-on-ubuntu-18-04-or-19-10.html

- tasksel & kubuntu-desktop & sddm
  - https://linuxtips.us/install-kde-plasma-ubuntu-18-04/

- tasksel & kubuntu-desktop & sddm
  - https://wpcademy.com/how-to-install-kde-plasma-on-ubuntu-18-04-lts/

# Analysis

Definitely seeing a bit of variety in the results but also quite a bit of similarity.
I am happy with what I have now on bette but want to try out KDE on it because I am digging what I now have on jane with 20.04.
Also, I have plenty of space in `/`:

```
/dev/sda3       217G   35G  171G  17% /   ## "plenty of space" is an understatement!
```

Not sure why I set things up this way, hmmm.

So I want to "play it safe," which means not cutting any corners, which in turn means installing `tasksel` for sure.

# Proposed Process Plan

Here is what I will try.  May need to adjust this as necessary.

## Install `tasksel`

Assuming `tasksel` is short for "task selection."
I definitely want to be able to choose between KDE and Gnome, so I can return to the old familar UI anytime I want.

Not sure why some of the pages do not mention this step.
Maybe I'll figure that out once I get to it.
Surely it could not hurt to do it?

## Install `kde-full`

I have plenty of space and am looking to recreate what I have after installing kubuntu on jane.

May also need to install kde-plasma?

## Run the `sddm` Step

Haven't looked at this closely but

Not sure why some of the pages do not mention this step.
Maybe I'll figure that out once I get to it.
Surely it could not hurt to do it?

