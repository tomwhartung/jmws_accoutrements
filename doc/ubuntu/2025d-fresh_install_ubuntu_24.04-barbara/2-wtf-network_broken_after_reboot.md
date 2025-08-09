
# 2-wtf-network_broken_after_reboot.md

Installed Ubuntu 24.04 from scratch on barbara, and the network is broken after a reboot.

- This is proving to be a non-trivial error, and has apparently many others have experienced this issue.

So, wtf indeed.

# Failed Attempts to Fix This

## First Attempt:

## Searching for " ubuntu network error interfaces file doesn't exist "

- The `/var/log/syslog` file contained an error message about `network/interfaces` being missing, and I verified there's nothing there
- Figured this out by looking for uses of "net" in `syslog`

### Initial Diagnosis

- Later versions - 17.xx-18.xx and up - of Ubuntu have switched from using `/etc/network/interfaces` to `/etc/netplan`
  - [https://askubuntu.com/questions/1268721/cannot-find-etc-network-interfaces-file-doesnt-exist#1268742](https://askubuntu.com/questions/1268721/cannot-find-etc-network-interfaces-file-doesnt-exist#1268742)
- **This page has a fairly good explantion of the situation:**
  - [https://askubuntu.com/questions/1031709/ubuntu-18-04-switch-back-to-etc-network-interfaces](https://askubuntu.com/questions/1031709/ubuntu-18-04-switch-back-to-etc-network-interfaces)
- I can see files in `/etc/netplan` while there are none under `/etc/network/interfaces`, so apparently this is the root of the issue
  - The configurations I've set using the **Settings** option up are, on the other hand, visible in `/etc/netplan`

### Digging Deeper

One page I saw seems to think that Ubuntu decides which to use based on whether `ifupdown` and/or `net-tools` are installed

- The main answer and its first comment on this page suggests that installing `ifupdown` causes Ubuntu to use `network/interfaces`
  - [https://askubuntu.com/questions/1031709/ubuntu-18-04-switch-back-to-etc-network-interfaces](https://askubuntu.com/questions/1031709/ubuntu-18-04-switch-back-to-etc-network-interfaces)
- I have these installed - they are on my list of essential packages to install
  - **Maybe that's where I messed up??**

### Use `interfaces` or `netplan`?

For documentation, see:

- Run `man interfaces` - or see one of the links below
- [https://netplan.io/](https://netplan.io/)

### Gentoo, LOL, Dems Was de Days!

The answer on this page asserts that there are multiple ways to define and access your network:

- [https://superuser.com/questions/1566174/etc-network-interfaces-file-not-found](https://superuser.com/questions/1566174/etc-network-interfaces-file-not-found)

Umm, let's stay away from gentoo, hmm-k ;-D .

### Trying to *Go Back*

The following two references suggest a similar cause for Ubuntu wanting to use the `interfaces` file, and how to make it *go back* to using it:

- [https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing](https://askubuntu.com/questions/1276847/looking-for-etc-network-interfaces-is-missing)
- [https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/](https://www.golinuxcloud.com/etc-network-interfaces-missing-ubuntu/)
- Note that these two sources do not seem to be in 100% agreement
  - See the comment to the solution on the askubuntu.com page

So I tried changing the `/etc/default/grub` file -- this was supposed to change it back to using the `/etc/network/interfaces` file -- as both pages recommend,
but that didn't work - at first...

Maybe I need to manually add an `/etc/network/interfaces` file?
This page explains how to do that:

- [https://www.cyberciti.biz/faq/setting-up-an-network-interfaces-file/](https://www.cyberciti.biz/faq/setting-up-an-network-interfaces-file/)

Let's try doing that ...






So I changed the `grub` file back to the way it was -- back to the installed version that I'd checked into RCS.

## Subsequent Attempts: Refining the Search

### Searching for 'ubuntu 24.04 network is unreachable'


### Searching for 'ubuntu Oracular Oriole 24.04 "temporary failure in name resolution" '

Found this page:

- [https://askubuntu.com/questions/1524158/temporary-failure-in-name-resolution-on-new-ubuntu-server-setup](https://askubuntu.com/questions/1524158/temporary-failure-in-name-resolution-on-new-ubuntu-server-setup)

Which mentions the `netplan` command in one of the comments.
So I ran `man netplan`:

- It has a `--debug` option
- Probably would want to run `netplan apply` or `netplan try`
- Do we want to use netplan?  Is it better?
  - One page said it was, another said it's impossible, I do not remember specifics, because I am just quickly scanning a lot of these search results


