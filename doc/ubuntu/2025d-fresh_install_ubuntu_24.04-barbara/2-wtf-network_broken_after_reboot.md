
# 2-wtf-network_broken_after_reboot.md

Installed Ubuntu 24.04 from scratch on barbara, and the network is broken after a reboot.

- This is proving to be a non-trivial error, and has apparently many others have experienced this issue.

So, wtf indeed.

# First Attempt

- Later versions - 17.xx-18.xx and up - of Ubuntu have switched from using `/etc/network/interfaces` to `/etc/netplan`
- Figured this out by looking for uses of "net" in `/var/log/syslog`
- I can see files in `/etc/netplan` while there are none under `/etc/network/interfaces`, so apparently this is the root of the issue
  - The `syslog` file contained an error message about `network/interfaces` being missing, and I verified there's nothing there
  - The configurations I've set up are, on the other hand, visible in `/etc/netplan`

These two references suggest a similar fix for this:

- [https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing](https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing)
- [https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/](https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/)

So I tried changing the `/etc/default/grub` file, but that didn't work.

