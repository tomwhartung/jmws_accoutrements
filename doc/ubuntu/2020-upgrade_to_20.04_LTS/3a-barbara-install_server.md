
# 3a-barbara-install_server.md

Installing Ubuntu 20.04 focal fossa server on barbara.

# Disk Partitions

## Partitions Before

This is the before picture:

```
/dev/sda5        13G   33M   13G   1% /future
/dev/sda6       923M  1.2M  859M   1% /future/boot
/dev/sda7       9.1G   21M  8.6G   1% /future/home
/dev/sda8        13G  7.5G  4.7G  62% /
/dev/sda9       923M  236M  624M  28% /boot
/dev/sda10      9.2G  3.4G  5.3G  39% /home
/dev/sda11       10G  3.0G  6.5G  32% /var/www
/dev/sda12      4.5G  3.5G  730M  84% /var/lib
/dev/sda13      3.7G  7.5M  3.4G   1% /mnt/spare/sda13
/dev/sda14      2.7G  4.2M  2.6G   1% /mnt/spare/sda14
/dev/sda15      1.9G  2.8M  1.7G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.4M  4.3G   1% /mnt/spare/sda16
/dev/sda17      2.7G  4.2M  2.6G   1% /mnt/spare/sda17
/dev/sda18      1.9G  198M  1.6G  12% /var/log
/dev/sda20       19G  8.0G  9.9G  45% /usr/local/tar
```

Note: These partitions take up about (13+10) + (13+10+10) + (5+4+3+2) + (5+3+2+19) = 21 + 33 + 14 + 29 = about 100G

Also note: Windows 10 is using 116G.

## Dump Windows?  Yes I Think So.

### Reasons to Dump Windows

Reasons to delete all the Windows partitions:

- ~~Never~~ Rarely use it except to update it
- It will lose support soon
- If I need a Windows or Mac for something, what I don't know, I can always buy a new cheap one
- Using barbara as the tar file host frees up space on others

### Reasons to Keep Windows

I can't think of one single one.

## Partitions After

Delete all existing partitions and start from scratch!

**Total available space is about 200G.**

### New Partitions

Create these new partitions:

/boot            1G
/               20G
/var            20G
/usr/local/tar  60G
/mnt/spare     100G

# Focal Fossa Installation

- Have install disk but it may be bad.

## Consideration: Python - Latest Version?

See `1e-jane-needed_for_all_sites.md` to learn why we are using 3.8.2 there, i.e.,
"the current version of python is now 3.8.3, but it is not yet available for upgrading to."

Be sure to **check the version of Python installed when installing 20.04 server on barbara**
and make and adjust plans as necessary.


