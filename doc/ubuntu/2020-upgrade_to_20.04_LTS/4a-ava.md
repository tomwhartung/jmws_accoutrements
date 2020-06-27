
# 2a-ava.md

Upgrading ava by installing into existing `/mnt/future*` and `/mnt/spare*` partitions

# Upgrading to Kubuntu 20.04 LTS (Focal Fossa)

Install kubuntu desktop 20.04 LTS while Leaving existing OS as-is - if possible.


# Disk Partitions

## Partitions Before

```
/dev/sda10      4.5G  9.4M  4.2G   1% /mnt/future/home
/dev/sda11       20G  2.2G   16G  12% /var/www
/dev/sda12      931M  1.3M  866M   1% /mnt/spare/sda12
/dev/sda14      4.5G  357M  3.9G   9% /usr/src
/dev/sda16      4.5G  119M  4.1G   3% /var/cache
/dev/sda17      4.5G  781M  3.5G  19% /var/log
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
/dev/sda19       91G   38G   49G  44% /usr/local/tar
/dev/sda5        22G  2.5G   19G  12% /
/dev/sda6       931M  109M  758M  13% /boot
/dev/sda7       4.5G  177M  4.1G   5% /home
/dev/sda8        22G   44M   21G   1% /mnt/future
/dev/sda9       931M  1.2M  866M   1% /mnt/future/boot
```

**Also: we can use the three windows 7 partitions, a total of 240G.**

## Partitions After Consolidation

Moved files in all partitions containing 16.04 files, e.g., `/var/www`, `/usr/src`, `/home`, etc.
**except the `/boot` partition, of course,** to where they belong under `/`, making as many
partitions as possible spare.

```
/dev/sda10      4.5G  9.3M  4.2G   1% /mnt/spare/sda10
/dev/sda11       20G   44M   19G   1% /mnt/spare/sda11
/dev/sda12      931M  1.2M  866M   1% /mnt/spare/sda12
/dev/sda14      4.5G  9.3M  4.2G   1% /mnt/spare/sda14
/dev/sda15      4.5G  9.3M  4.2G   1% /mnt/spare/sda15
/dev/sda16      4.5G  9.3M  4.2G   1% /mnt/spare/sda16
/dev/sda17      4.5G  9.3M  4.2G   1% /mnt/spare/sda17
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
/dev/sda19       91G   38G   49G  44% /usr/local/tar
/dev/sda5        22G  6.0G   15G  29% /
/dev/sda6       931M  109M  758M  13% /boot
/dev/sda7       4.5G  9.3M  4.2G   1% /mnt/spare/sda7
/dev/sda8        22G   44M   21G   1% /mnt/spare/sda8
/dev/sda9       931M  1.2M  866M   1% /mnt/spare/sda9
```

Hoping I can consolidate these....

## Partitions at Install Time

Partitions after using the kubuntu disk to consolidate them...

```
```

## Partitions - Proposed

```
/dev/sda1      12.6G  0.0M 12.6G   1% /mnt/spare/sda1
/dev/sda2       301M  0.0M  301M   1% /
/dev/sda3       258G  0.0M  258G   1% /   - Can I split this up?  Do I want to?
/dev/sda4       [extended]

/dev/sda5        22G  2.5G   19G  12% /ubuntu-16.04/
/dev/sda6       931M  109M  758M  13% /ubuntu-16.04/boot
/dev/sda7       4.5G  177M  4.1G   5% /ubuntu-16.04/home

/dev/sda8        22G   44M   21G   1% /home  - OK to format
/dev/sda9       931M  1.2M  866M   1% /boot  - OK to format

/dev/sda10      4.5G  9.4M  4.2G   1% /mnt/spare/sda10
/dev/sda11       20G  2.2G   16G  12% /var/www              - Reuse as-is, do NOT format
/dev/sda12      931M  1.3M  866M   1% /mnt/spare/sda12
/dev/sda14      4.5G  357M  3.9G   9% /mnt/spare/sda14
/dev/sda16      4.5G  119M  4.1G   3% /mnt/spare/sda16
/dev/sda17      4.5G  781M  3.5G  19% /ubuntu-16.04/var/log
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
/dev/sda19       91G   38G   49G  44% /usr/local/tar        - Reuse as-is, do NOT format
```

## Partitions After

```
```

