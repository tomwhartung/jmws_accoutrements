
# 3c-barbara-sanity.md

Achieving sanity as quickly as possible on barbara by installing essential programs

# Essentials

Immediate Goals:

- Restore home directory
- Get barbara on the the network
- Get look and feel to be consistent with others
- Start using barbara to rip CDs to mp3

# Details

## Restore home directory

Copy of old home directory is in `/ubuntu-16.04/home` .

```
cd /home
sudo mkdir tomh-installed
sudo chown tomh:tomh tomh-installed
cp -rp tomh/* tomh-installed
cp -rp tomh/.[a-zA-Z]* tomh-installed
cd tomh
cp -rp /ubuntu-16.04/home/tomh/* .
cp -rp /ubuntu-16.04/home/tomh/.[a-zA-Z]* .
```

Reboot


## Get barbara on the the network



## Get look and feel to be consistent with others



## Start using barbara to rip CDs to mp3




