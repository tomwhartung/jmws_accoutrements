
# 4b-ava-sanity_please.md

Upgrading ava to 20.04.

# Acheiving Sanity

## Home Directory

Restore the `/home/tomh` directory from barbara, saved on the thumb drive.

## Root User's Home Directory

Reconstruct links to ~tomh/.bash_aliases, etc., present in /root on another host, e.g., bette, to /root as appropriate.

Copy files and directories to /root, e.g., .vim and RCS, from /root on another host, e.g., bette, to /root as appropriate.

## Install Vim, Git, RCS, and Chrome

Vim, Git, and RCS: use the command line.

```
apt-get update
apt vim
apt install vim git rcs
cd /etc
mkdir RCS
ci -l fstab hosts
apt-get upgrade -y
```

Configure git:

```
git config --global user.email "tomwhartung@gmail.com"
git config --global user.name "Tom Hartung"
```

## Setup Static IP

Access Settings -> Network -> Connections -> IPv4 Tab

Method: Manual
DNS: 192.168.30.2, 192.168.31.2
Netmask: 255.255.255.0
Gateway: 192.168.1.1

## Install Chrome

Download from google then install:

```
apt install libappindicator3-1
cd ~/Downloads
cp ~tomh/Downloads/google-chrome-stable_current_amd64.deb .
apt install ./google-chrome-stable_current_amd64.deb
```

Find in menu then Add to Favorites.

## Fix My `up` Command

My `up` command depends on having python3 and the `sh` module installed.

- Reference: https://pypi.org/project/sh/

Steps, starting with the basics:

- 1. Install `python3`, if it's missing
- 2. Install `pip3`, if it's missing
- 3. Optionally use `update-alternatives` to enable running just `python` and `pip` without the `3`s
- 4. Use `pip` to install the `sh` module

Commands:

```
$ apt list --installed | grep python3/focal
python3/focal,now 3.8.2-0ubuntu2 amd64 [installed]
$ which python
$ update-alternatives --install /usr/bin/python python /usr/bin/python3 1
$ which python
/usr/bin/python
$ python -V
Python 3.8.2
$ apt install python3-pip -y
$ pip --version
Command 'pip' not found, but there are 18 similar ones.
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
$ update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
$ pip3 install sh
$
```

## Install Chromium and Opera

Use Ubuntu software app -- i.e., **Discover** -- to install.

Find in menu then Add to Favorites.

Ahh, that is much better!

