
# 3d-barbara-rip_cds.md

Goal:

- [x] Start using barbara to rip CDs to mp3

# Start using barbara to rip CDs to mp3

## Create essential directories

Commands run:
```
cd /
sudo mkdir art
sudo chown tomh:tomh art
mkdir -p art/music/mp3-new
```

## Install Easy Tag

Ubuntu Software icon in dock -> Search -> Easy Tag -> Launch
- Once it is running, right-click on the icon and Add it as a Favorite

## Ripping CDs - Experiments

### Trying Rhythmbox

- Tested ripping to .ogg and it works ok
- Setting preferences to use mp3 gets this error message:
  - "Install additional software required to use this format"

First try - try installing gstreamer
- Reference:
  - https://www.lifewire.com/complete-guide-rhythmbox-2204885
- Steps run:
  - Run Ubuntu Software via icon in doc
  - Search for "gstreamer" and install

Second try - try installing from "error button"
- In Rhythmbox -> Menu -> Preferences -> Music tab
  - Tried setting "Preferred format" to MPEG Layer 3 4 Audio
  - Tried clicking on error button, then little popup at the top
    - Opens Ubuntu Software to find "Available software for ID3 tag muxer"
    - Then get error message "Unable to find Requested Software"

Third try - try installing first Gstreamer Multimedia Codecs package
- In Rhythmbox -> Menu -> Preferences -> Music tab
  - Tried setting "Preferred format" to MPEG 4 Audio
  - Tried clicking on error button, then little popup at the top
    - Opens Ubuntu Software to find "Available software for MPEG-4 AAC encoder"
    - Then get two options, both named "GStreamer Multimedia Codecs"
  - Try first one, description begins with "This GStreamer plugin supports a large number of audio ..."

Rebooted, does not work.

Fourth try - try installing second Gstreamer Multimedia Codecs package
- In Rhythmbox -> Menu -> Preferences -> Music tab
  - Tried setting "Preferred format" to MPEG 4 Audio
  - Tried clicking on error button, then little popup at the top
    - Opens Ubuntu Software to find "Available software for MPEG-4 AAC encoder"
    - Then get two options, both named "GStreamer Multimedia Codecs"
  - Try second one, description begins with "GStreamer is a streaming media framework, based on graphs ..."
  - Seems to be working, but I will believe it when I see it
    - Concerned because I saw an online post saying gstreamer is sucky ...
    - First track of each CD is less than 320 kpbs, weird
    - The tracks sound fine and file sizes look ok, though

#### Trying k3b

This reference says k3b is the "least worst" ripper for linux:
- https://askubuntu.com/questions/1881/what-are-some-cd-ripping-programs-you-can-use-on-ubuntu
- "The current CD rippers in Ubuntu are terrible. The least worst CD Ripper for Linux is the venerable k3b."

Reference:
- https://userbase.kde.org/K3b

Doesn't seem to rip at the maximum 320 kbps.  Even when I set it to do that, it rips at VBR.  Rats.

#### Possible Hack

Rhythmbox is fine except for the first song, so a possible hack is to:

- 1. Use Rhythmbox to rip cd
- 2. Use k3b to rip first song of each cd

## Ripping CDs - Success

After fiddling around a bit I was able to get k3b to work well.
Frankly it may have been rebooting that fixed it, which seems weird.
Maybe it was opening the preferences in the window that starts ripping the CDs instead of just using the preferences in the menu.

Regardless, it seems to be working well, with one slight glitch:
- In rhythmbox on bette, the quality of the ripped mp3s shows up as "Unknown"
- In banshee on bette, and in rhythmbox on jane, the quality of the ripped mp3s shows up as "320 kbps"

The mp3s sound good even at VBR rates, but it's nice to be able to create them at 320 kbps, because disk space is so cheap these days.

Sweet!

