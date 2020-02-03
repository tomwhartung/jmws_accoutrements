
# 3g-barbara-audacious.md

Installing audacious on barbara, which is running ubuntu 18.04.

FYI, tried installing it using the GUI, and it failed repeatedly.

## Reference

So found this reference, hope it works.

- https://www.audacious-media-player.org/download

That reference claims the version in the distro is frequently out of date.

To get more recent versions, follow the instructions on these sites to update the ppa and all.

- https://www.itsmarttricks.com/how-to-install-audacious-audio-player-in-ubuntu-18-04/
- http://ubuntuhandbook.org/index.php/2018/08/audacious-3-10-released-install-ubuntu-18-04/

## Installation

Run as root:

```
apt-get update
apt-get install audacious
# The following NEW packages will be installed:
#  audacious audacious-plugins audacious-plugins-data libaudcore5 libaudgui5 libaudtag3 libcue1 libsdl2-2.0-0 libsidplayfp4
```

Note that this command also installs the plugins package.

## Try It Out

Try recording something on vinyl.

Hmmmm.

