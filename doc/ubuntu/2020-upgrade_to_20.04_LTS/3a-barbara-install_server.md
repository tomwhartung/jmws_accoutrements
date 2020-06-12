
# 3a-barbara-install_server.md

Installing 20.04 server OS on barbara.

# Disk Partitions

Some thoughts:

- I think it will be ok to delete all the Windows partitions
- Why not use barbara as the tar file host?  Something to think about.
- There are currently many small `spare` partitions

```
 $ dfs
/dev/sda10      9.2G  3.4G  5.3G  39% /home
/dev/sda11       10G  3.0G  6.5G  32% /var/www
/dev/sda12      4.5G  3.5G  730M  84% /var/lib
/dev/sda13      3.7G  7.5M  3.4G   1% /mnt/spare/sda13
/dev/sda14      2.7G  4.2M  2.6G   1% /mnt/spare/sda14
/dev/sda15      1.9G  2.8M  1.7G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.4M  4.3G   1% /mnt/spare/sda16
/dev/sda17      2.7G  4.2M  2.6G   1% /mnt/spare/sda17
/dev/sda18      1.9G  198M  1.6G  12% /var/log
/dev/sda20       19G   15G  3.4G  82% /usr/local/tar
/dev/sda5        13G   33M   13G   1% /future
/dev/sda6       923M  1.2M  859M   1% /future/boot
/dev/sda7       9.1G   21M  8.6G   1% /future/home
/dev/sda8        13G  7.2G  5.0G  60% /
/dev/sda9       923M  236M  624M  28% /boot
tomh@barbara: ~
 $
```

# Focal Fossa Installation

TBD and TODO.

- Have install disk but it may be bad.

# Python - Latest Version?

See `1e-jane-needed_for_all_sites.md` to learn why we are using 3.8.2 there, i.e.,
"the current version of python is now 3.8.3, but it is not yet available for upgrading to."

Be sure to **check the version of Python installed when installing 20.04 server on barbara**
and make and adjust plans as necessary.


