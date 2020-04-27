
# 1a-jane.md

Upgrade jane to 20.04.

# Plan

Upgrade jane by installing into existing `/mnt/future*` and `/mnt/spare*` partitions.

## Upgrading to Ubuntu 20.04 LTS (Focal Fossa)

Upgrade and leave existing OS as-is.

This process should be a little bit easier than always starting from scratch:

- No need to partion disks - always the hardest part
- Will need to burn new DVD
- Will need to reinstall my favorite programs

## List of `/mnt/future*` and `/mnt/spare*` Partitions

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

# Disks

How to name partitions during install:

```

```

