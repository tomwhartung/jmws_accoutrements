
# 3b-barbara-server-sanity_please.md

Upgrading barbara to ubuntu server 20.04 focal fossa.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Acheiving Sanity

## Install Vim, Git, RCS, and Chrome

Vim and Git are already installed.

Configure git:

```
git config --global user.email "tomwhartung@gmail.com"
git config --global user.name "Tom Hartung"
```

Use the command line for RCS.

```
apt install rcs
cd /etc
mkdir RCS
ci -l fstab hosts
```

## Static IP

### References

- Commands for the server appear after desktop info; mentions subiquity file in comments
  - https://linuxconfig.org/how-to-configure-static-ip-address-on-ubuntu-20-04-focal-fossa-desktop-server
- Just the server
  - https://www.linuxtechi.com/assign-static-ip-address-ubuntu-20-04-lts/
- Commands for the server appear after desktop info
  - https://linuxhint.com/setup_static_ip_address_ubuntu/

### Process and Commands

#### 1. Check current ip address:

```
$ apt install net-tools
$ ifconfig
. . .
     inet 192.168.1.105     netmask 255.255.255.0
. . .
$ ip add show
. . .
     inet 192.168.1.105/24  ...
. . .
$ ip a
. . .
     inet 192.168.1.105/24  ...
. . .
$
```

#### 2. Parameters

address: 192.168.1.116
gateway: use 192.168.1.1 [tp-link router]
DNS name servers: 192.168.30.2,192.168.31.2

#### 3. Ensure subiquity is disabled:

```
$ cd /etc/cloud/cloud.cfg.d/
$ mkdir RCS
$ ci -l subiquity-disable-cloudinit-networking.cfg     # "Installed version"
$ vi subiquity-disable-cloudinit-networking.cfg
$ cat subiquity-disable-cloudinit-networking.cfg
network: {config: disabled}
$
```

Turns out it was already disabled but whatevs.

#### 4. Update netplan config:

We will update `00-installer-config.yaml` rather than add `50-cloud-init.yaml`.

```
$ cd /etc/netplan/
$ mkdir RCS
$ ci -l 00-installer-config.yaml   # "Installed version"
$ ## vi 50-cloud-init.yaml         # The file according to linuxconfig.org, but it's not there
$ vi 00-installer-config.yaml      # The file according to the other two references, and already there
```

Make the contents of the `00-installer-config.yaml` file look like this:

```
network:
  ethernets:
    enp0s25:
      dhcp4: false
      addresses: [192.168.1.116/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [192.168.30.2,192.168.31.2]
```

Run netplan, fixing any errors that occur.

```
$ netplan apply    # Silence is golden
$
```

## Home Directory

Copy home directory from ava.

## Root User's Home Directory

Reconstruct links, e.g., .bash_aliases, present in /ubuntu-16.04/root to /root as appropriate.

Copy files and directories, e.g., .vim and RCS, from /ubuntu-16.04/root to /root as appropriate

## Fix My `up` Command

My `up` command depends on having python3 and the `sh` module installed.

- Reference: https://pypi.org/project/sh/

Steps, starting with the basics:

- 1. Install `python3`, if it's missing
- 2. Install `pip3`, if it's missing
- 3. Optionally use `update-alternatives` to enable running just `python` and `pip` without the `3`s
- 4. Use `pip` to install the `sh` module

The most important part:

```
pip3 install sh
```

Additional optional but totally cool commands:

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

