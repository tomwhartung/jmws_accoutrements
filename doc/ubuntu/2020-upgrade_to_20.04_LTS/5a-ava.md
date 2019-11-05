
# 5a-ava.md

Upgrading ava by installing into existing /mnt/future* partitions.

# Upgrading to Ubuntu 20.04 LTS (Focal Fossa)

Note: at this time it "is expected on 23 April 2020."
- https://en.wikipedia.org/wiki/Ubuntu_version_history#Table_of_versions

# Upgrading While Leaving Existing OS As-Is

This process should be a little bit easier than always starting from scratch:

- No need to partion disks - always the hardest part
- Will need to burn new DVDs
- Will need to reinstall my favorite programs

# List of `/mnt/future*` and `/mnt/spare*` Partitions

Use these first:
```
/dev/sda8        22G   44M   21G   1% /mnt/future
/dev/sda10      4.5G  9.4M  4.2G   1% /mnt/future/home
/dev/sda9       931M  1.2M  866M   1% /mnt/future/boot
```

Use these if needed:
```
/dev/sda12      931M  1.3M  866M   1% /mnt/spare/sda12
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
```

