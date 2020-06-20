
# 3b-barbara-server-sanity_please.md

Upgrading barbara to ubuntu server 20.04 focal fossa.

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

## Update Home Directories

Copy selected files from the 18.04 home directories saved in `/dev/sda8` and `/dev/sda10`,
which must first be mounted.

### Mount the `/ubuntu-18.04*` Directories

Mount `/dev/sda8` on `/ubuntu-18.04` and `/dev/sda10` on `/ubuntu-18.04/home`, and update fstab to do that at boot:

```
cd /
ll
mkdir ubuntu-18.04
mount /dev/sda8 /ubuntu-18.04
mount /dev/sda10 /ubuntu-18.04/home
blkid /dev/sda8
blkid /dev/sda10
cd etc
vi fstab
```

## Update `tomh`'s Home Directory

Make sure to **not destroy any installed files,** then copy selected files from `/ubuntu-18.04/home/tomh`.

```
mkdir .ssh
cd .ssh
cp -r /ubuntu-18.04/home/tomh/.ssh/* .
cd
mkdir RCS
ci -l .bashrc   # "Installed version"
mkdir RCS
ci -l .bashrc
diff .bashrc /ubuntu-18.04/home/tomh/.bashrc
```

The only differences are my CusTOMizations, so we are good to go.

```
cp /ubuntu-18.04/home/tomh/.bashrc .
rcsdiff ./.bashrc
vi ./.bashrc                    # delete obsolete CusTOMizations, e.g., for coursera
rcsdiff ./.bashrc
ci -l ./.bashrc                 # "Added my CusTOMizations."
ll
ll /ubuntu-18.04/home/tomh/
ll /ubuntu-18.04/home/tomh/.bash*
ll /ubuntu-18.04/home/tomh/.bash_aliases*
grep .bash_aliases .bashrc
ll /ubuntu-18.04/home/tomh/.bash_aliases*
cp /ubuntu-18.04/home/tomh/.bash_aliases* .
. ./.bashrc
l /ubuntu-18.04/home/tomh/.bash*                            # We can now run just "l"
diff  /ubuntu-18.04/home/tomh/.bash_logout .bash_logout     # No differences
l /ubuntu-18.04/home/tomh/
cp -r /ubuntu-18.04/home/tomh/bin .
cp /ubuntu-18.04/home/tomh/d.e  /ubuntu-18.04/home/tomh/r* .
l /ubuntu-18.04/home/tomh/.vim*
cp -r /ubuntu-18.04/home/tomh/.vimrc  /ubuntu-18.04/home/tomh/.vim .
l
mkdir tmp
```

## Update Root User's Home Directory

Copy files and directories, e.g., .vim and RCS, from /ubuntu-16.04/root to /root as appropriate

```
ll
ll /ubuntu-18.04/
ll /ubuntu-18.04/root/
mkdir RCS
ci -l .bashrc      # "Installed version"
ll
ll /ubuntu-18.04/root/
diff .bashrc /ubuntu-18.04/root/.bashrc    # Only differences are my CusTOMizations
rcsdiff .bashrc
diff .bashrc /ubuntu-18.04/root/.bashrc
cp /ubuntu-18.04/root/.bashrc .
```

Reconstruct links, e.g., to .bash_aliases, present in /ubuntu-18.04/root to /root as appropriate.

```
ll /ubuntu-18.04/root/
ln -s /home/tomh/.bash_aliases .
ln -s /home/tomh/.bash_aliases-barbara  .
ln -s /home/tomh/.vimrc  .
ln -s /home/tomh/.vim  .
ln -s /home/tomh/bin  .
mkdir tmp
ll /ubuntu-18.04/root/
cp /ubuntu-18.04/root/postgres_commands.txt .
ll
. ./.bashrc
rd .bashrc
ci -l .bashrc       # "Added my CusTOMizations."
```

## Reboot

Reboot and check for mounted filesystems and the presence of aliases.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Install `python`, `pip`, and the `sh` Module

The sites use `python3` aka `python` so might as well might as well properly install it now.

### Process

- 1. Install `python3`, if it's missing
- 2. Install `pip3`, if it's missing
- 3. Optionally use `update-alternatives` to enable running just `python` and `pip` without the `3`s
- 4. Use `pip` to install the `sh` module

### Commands

Run these commands:

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
## Fix My `up` Command

My `up` command depends on having python3 and the `sh` module installed.

- Reference: https://pypi.org/project/sh/

The most important part:

```
pip3 install sh
```


