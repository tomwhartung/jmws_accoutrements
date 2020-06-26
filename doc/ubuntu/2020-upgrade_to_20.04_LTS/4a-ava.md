
# 2a-ava.md

Upgrading ava by installing into existing `/mnt/future*` and `/mnt/spare*` partitions

# Upgrading to Kubuntu Desktop 20.04 LTS (Focal Fossa)

Install kubuntu while Leaving Existing OS As-Is - if possible.

# List of `/mnt/future*` and `/mnt/spare*` Partitions

**Also: Windows 7 is using up 240G, and complaining about being counterfeit, lol.**

So what to do with 240G?  Will it let me format it?  Let's try it and see!

# What I Had Before

Use these partitions first:
```
/dev/sda8        22G   44M   21G   1% /mnt/future
/dev/sda10      4.5G  9.4M  4.2G   1% /mnt/future/home
/dev/sda9       931M  1.2M  866M   1% /mnt/future/boot
```

Use these partitions if needed:
```
/dev/sda12      931M  1.3M  866M   1% /mnt/spare/sda12
/dev/sda18       19G   44M   18G   1% /mnt/spare/sda18
```

