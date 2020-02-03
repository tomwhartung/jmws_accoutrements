
# 3g-barbara-audacity.md

Installing audacity on barbara, which is running ubuntu 18.04.

FYI, tried installing it using the GUI, and it failed repeatedly, probably because it requires using a special ppa.

## References

This one looks like the best, but it is also quite out of date:

- https://help.ubuntu.com/community/Audacity

These two agree on the same, very simple process.

- https://sourcedigit.com/22111-install-audacity-linux-ubuntu-terminal/
- https://linux4one.com/how-to-install-audacity-on-ubuntu-18-04/

Let's give it a try!

## Installation

Run as root:

```
add-apt-repository ppa:ubuntuhandbook1/audacity
apt-get update
apt-get install audacity
# The following additional packages will be installed:
#   audacity-data libportaudio2 libportsmf0v5 libsuil-0-0 libvamp-hostsdk3v5 libwxbase3.0-0v5 libwxgtk3.0-0v5
# Suggested packages:
#   ladspa-plugin
# The following NEW packages will be installed:
#   audacity audacity-data libportaudio2 libportsmf0v5 libsuil-0-0 libvamp-hostsdk3v5 libwxbase3.0-0v5 libwxgtk3.0-0v5
```

So far, so good.

## Try It Out

### Start It Up

Try running it as tomh:

```
which audacity
# /usr/bin/audacity
audacity &
```

1. Find icon in taskbar, move it to a location near amarok, K3b, and Easytag, and lock it there.
2. Exit and use the taskbar icon to run it in the future.

### Use It to Record Something

Try recording something on vinyl.

Hmmmm.

