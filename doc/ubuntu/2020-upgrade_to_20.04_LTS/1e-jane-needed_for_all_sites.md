
# 1e-jane-needed_for_all_sites.md

Instructions for installing the latest stable versions of software needed for two or more sites:

- Python
- Flask
- Django

# Latest Stable Versions

Per the wikipedia.

- Python: stick with 3.8.2 (see below)
  - Stable release is now 3.8.3
  - 3.8.2 is already installed with 20.04
  - 3.8.x: Full support through 2021-04, with security fixes through 2024-10
- Django: 3.0.6
  - Stable release: 3.0.6
  - 3.2 LTS: due 2021-04, will be supported until at least 2024-04
  - 4.0: due 2021-12, will be supported until at least 2023-04
- Flask: 1.1.2
  - Stable release: 1.1.2

For additional goals and an overall plan see `1d-jane-upgrade_all_sites-overview.md`.

For details for each site in the `2*.md` files, e.g., `2a-artsyvisions.md` in this directory.

# Python

The current version of python is now 3.8.3, but it is not yet available for upgrading to.

```
$ apt list --installed | grep python3/focal
python3/focal,now 3.8.2-0ubuntu2 amd64 [installed]
$ apt-get upgrade python3
. . .
. . .
. . .
python3 is already the newest version (3.8.2-0ubuntu2).
. . .
. . .
. . .
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
$
```

**Check version installed when installing 20.04 server on barbara.**

# Django

# Flask

TBD.
