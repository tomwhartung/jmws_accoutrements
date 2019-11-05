
# 1f-bette-rip_to_mp3.md

Rhythmbox and Soundjuicer do not seem to recognize that there is a CD in the drive.  Hmm.

Thinking about trying RubyRipper, and if that doesn't work, maybe ripperx.

## References

- Recommends Soundjuicer but includes steps to install RubyRipper and many others:
  - https://askubuntu.com/questions/1881/what-are-some-cd-ripping-programs-you-can-use-on-ubuntu
- Includes steps to install RubyRipper:
  - https://help.ubuntu.com/community/CDRipping
- RubyRipper home page:
  - http://wiki.hydrogenaud.io/index.php?title=Rubyripper
- Focus is on soundjuicer and k3b, but has some info on some others:
  - https://www.linux.com/news/ripping-audio-cds-linux/
- How to convert to mp3 - not really relevant to what I want
  - https://linuxconfig.org/how-to-convert-to-and-from-mp3-on-linux

## RubyRipper

Looking at
- (1) https://askubuntu.com/questions/1881/what-are-some-cd-ripping-programs-you-can-use-on-ubuntu
and
- (2) https://help.ubuntu.com/community/CDRipping

Install dependencies:

```
sudo apt-get install cd-discid cdparanoia flac lame mp3gain normalize-audio ruby-gnome2 ruby vorbisgain   ## (1)
sudo apt-get install cd-discid cdparanoia flac lame mp3gain normalize-audio ruby-gnome2 ruby vorbisgain   ## (2)
```

Ooops, got an error:
- `E: Package 'mp3gain' has no installation candidate`

Found this fix:
- https://launchpad.net/~flexiondotorg/+archive/ubuntu/audio

Ran these commands to fix error:

```
sudo add-apt-repository ppa:flexiondotorg/audio
sudo apt-get update
```

Try again to install dependencies:
```
sudo apt-get install cd-discid cdparanoia flac lame mp3gain normalize-audio ruby-gnome2 ruby vorbisgain
```

Install rubyripper:
```
sudo add-apt-repository ppa:aheck/ppa
```

Oops, got an error:
- `E: The repository 'http://ppa.launchpad.net/aheck/ppa/ubuntu bionic Release' does not have a Release file.`
- `N: Updating from such a repository can't be done securely, and is therefore disabled by default.`
- `N: See apt-secure(8) manpage for repository creation and user configuration details.`

Possible solution:
- https://askubuntu.com/questions/866901/what-can-i-do-if-a-repository-ppa-does-not-have-a-release-file

## Ripperx

Try installing ripperx:
```
apt-get install ripperx
```

It runs, but does not seem to see the CD Rom - same deal as with Rhythymbox and Soundjuicer.  Hmm.
```
which ripperx
/usr/bin/ripperx
```

