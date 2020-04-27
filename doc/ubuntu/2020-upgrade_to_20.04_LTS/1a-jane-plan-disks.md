
# 1a-jane.md

Upgrading jane by installing into existing `/mnt/future*` and `/mnt/spare*` partitions.

# Upgrading to Ubuntu 20.04 LTS (Focal Fossa)

Note: at this time it "is expected on 23 April 2020."
- https://en.wikipedia.org/wiki/Ubuntu_version_history#Table_of_versions

# Upgrading While Leaving Existing OS As-Is

This process should be a little bit easier than always starting from scratch:

- No need to partion disks - always the hardest part
- Will need to burn new DVDs
- Will need to reinstall my favorite programs

# List of `/mnt/future*` and `/mnt/spare*` Partitions

Use these partitions first:
```
/dev/sda7        23G   44M   22G   1% /mnt/future
/dev/sda2       925M  1.2M  860M   1% /mnt/future/boot
/dev/sda9        23G   44M   22G   1% /mnt/future/home
```

Use these partitions if needed:
```
/dev/sda11      924M  1.5M  859M   1% /mnt/spare/sda11
/dev/sda14      174G   60M  165G   1% /mnt/spare/sda14
```

