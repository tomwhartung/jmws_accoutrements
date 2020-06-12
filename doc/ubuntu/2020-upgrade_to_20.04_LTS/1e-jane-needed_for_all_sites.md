
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
  - 3.1: due 2020-08 - **keep an eye on this**
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

Python2 has reached the end of its life.

This is how to make python3 the default python:

```
$ which python
$ update-alternatives --install /usr/bin/python python /usr/bin/python3 1
$ which python
/usr/bin/python
$ python -V
Python 3.8.2
$
```

Learned about the `update-alternatives` command at https://www.howtoforge.com/tutorial/how-to-install-django-on-ubuntu/

**Check version installed when installing 20.04 server on barbara.**

# Django

References:

- https://www.howtoforge.com/tutorial/how-to-install-django-on-ubuntu/
  - **Detailed and targets ubuntu 20.04**
- https://www.djangoproject.com/download/
  - General yet very concise
  - The page howtoforge.com is better

## Starting from scratch:

```
$ apt list | grep python3-django/
python3-django/focal-updates,focal-updates,focal-security,focal-security 2:2.2.12-1ubuntu0.1 all
$ apt list | grep python3-pip/
python3-pip/focal,focal 20.0.2-5ubuntu1 all
root@jane: ~
$ apt list --installed | grep python3-pip
root@jane: ~
$ apt list --installed | grep python3-django
$
```

## Installing django Globally

At least right now, we want all sites to use the same, current version of django.

So we are not going to worry about environments and the like.

## Installing pip

Install `python3-pip` and run `update-alternatives`:

```
$ apt install python3-pip -y
$ pip --version

Command 'pip' not found, but there are 18 similar ones.

$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
$ update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
$
```

## Installing the Latest Version of Django

The `apt` command wants to install version 2.2:

```
$ apt show python3-django
Package: python3-django
Version: 2:2.2.12-1ubuntu0.1
. . .
. . .
. . .
$
```

We want the latest, version 3.0.6.

**Use `pip` to install django instead of `apt`.**

```
$ pip install django==3.0.6
Collecting django==3.0.6
  Downloading Django-3.0.6-py3-none-any.whl (7.5 MB)
     |████████████████████████████████| 7.5 MB 245 kB/s
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 146 kB/s
Collecting pytz
  Downloading pytz-2020.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 151 kB/s
Collecting asgiref~=3.2
  Downloading asgiref-3.2.7-py2.py3-none-any.whl (19 kB)
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.2.7 django-3.0.6 pytz-2020.1 sqlparse-0.3.1
$ django-admin --version
3.0.6
$ python
Python 3.8.2 (default, Apr 27 2020, 15:53:34)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
3.0.6
>>> exit()
$
```


# Flask

TBD.
