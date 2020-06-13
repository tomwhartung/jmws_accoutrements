
# 1b-jane-sanity_please.md

Upgrading jane to 20.04.

# Acheiving Sanity

## Home Directory

Restore home directory, one file and directory at a time, for safety.

## Root User's Home Directory

Reconstruct links, e.g., .bash_aliases, present in /ubuntu-16.04/root to /root as appropriate.

Copy files and directories, e.g., .vim and RCS, from /ubuntu-16.04/root to /root as appropriate

## Install Vim, Git, RCS, and Chrome

Vim, Git, and RCS: use the command line.

```
apt list vim
apt install vim
apt list git
apt install git
apt list rcs
apt install rcs
cd /etc
mkdir RCS
ci -l fstab hosts
```

Configure git:

```
git config --global user.email "tomwhartung@gmail.com"
git config --global user.name "Tom Hartung"
```

## Install Chrome

Download from google then install:

```
dpkg -i google-chrome-stable_current_amd64.deb    ## got an error first time
apt install libappindicator3-1
dpkg -i google-chrome-stable_current_amd64.deb    ## worked ok the second time
apt-get install -f
```

Find in menu then Add to Favorites.

## Fix My `up` Command

My `up` command depends on having python3 and the `sh` module installed.

Steps:

- 1. Install python3, if it's missing
- 2. Install pip, if it's missing
- 3. Use pip to install the sh module

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
$
```

## Install Chromium and Opera

Use Ubuntu software app -- i.e., **Discover** -- to install.

Find in menu then Add to Favorites.

Ahh, that is much better!

