
# 2-wtf-network_broken_after_reboot.md

Installed Ubuntu 24.04 from scratch on barbara, and the network is broken after a reboot.

- This is proving to be a non-trivial error, and has apparently many others have experienced this issue.

So, wtf indeed.

# Failed Attempts to Fix This

## First Attempt: `ubuntu 24.04 network is unreachable`

### Initial Diagnosis

- Later versions - 17.xx-18.xx and up - of Ubuntu have switched from using `/etc/network/interfaces` to `/etc/netplan`
- Figured this out by looking for uses of "net" in `/var/log/syslog`
- I can see files in `/etc/netplan` while there are none under `/etc/network/interfaces`, so apparently this is the root of the issue
  - The `syslog` file contained an error message about `network/interfaces` being missing, and I verified there's nothing there
  - The configurations I've set up are, on the other hand, visible in `/etc/netplan`

These two references suggest a similar cause for this:

- [https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing](https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing)
- [https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/](https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/)

So I tried changing the `/etc/default/grub` file, as both pages recommend, but that didn't work.

- This was supposed to change it back to using the `/etc/network/interfaces` file
- One of these seems to think that Ubuntu decides which to use based on whether `net-tools` and `ifupdown` are installed
  - I have these installed - they are on my list of essential packages to install
   - **Maybe that's where I messed up??**
- Note that these two sources do not seem to be in 100% agreement
  - See the comment to the solution on the askubuntu.com page

Maybe I need to manually add an `/etc/network/interfaces` file?
This page explains how to do this:

- [https://www.cyberciti.biz/faq/setting-up-an-network-interfaces-file/](https://www.cyberciti.biz/faq/setting-up-an-network-interfaces-file/)

So I changed the `grub` file back to the way it was -- back to the installed version that I'd checked into RCS.

## Subsequent Attempts: Refining the Search

### ""


### Searching for 'ubuntu Oracular Oriole 24.04 "temporary failure in name resolution" '

Found this page:

- [https://askubuntu.com/questions/1524158/temporary-failure-in-name-resolution-on-new-ubuntu-server-setup](https://askubuntu.com/questions/1524158/temporary-failure-in-name-resolution-on-new-ubuntu-server-setup)

Which mentions the `netplan` command in one of the comments.
So I ran `man netplan`:

- It has a `--debug` option


