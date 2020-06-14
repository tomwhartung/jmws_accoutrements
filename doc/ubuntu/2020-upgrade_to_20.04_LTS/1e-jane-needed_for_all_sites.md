
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

## Installing django Globally

At least for right now, we want all sites to use the same, current version of django.

So we are not going to worry about environments and the like.

## Starting From Scratch:

```
$ apt list | grep python3-django/
python3-django/focal-updates,focal-updates,focal-security,focal-security 2:2.2.12-1ubuntu0.1 all
$ apt list | grep python3-pip/
python3-pip/focal,focal 20.0.2-5ubuntu1 all
$ apt list --installed | grep python3-pip
$ apt list --installed | grep python3-django
$
```

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

The `apt` command wants to install version 2.2, **but that's not what we want!**:

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

## The Settings File Is Needed for All Django Sites

Get a copy of `gitignored/Site/Site/settings.py` from another host, e.g., bette.

Use `rcsdiff` to check the settings file for changes, and if there are differences, check in the current version.

Then copy the `settings.py` file along with the `RCS` directory to jane.

Review and remember: **`SECURITY WARNING: don't run with debug turned on in production!`**

# Flask

References:

- https://en.wikipedia.org/wiki/Flask_(web_framework)
- https://flask.palletsprojects.com/en/1.1.x/installation/
  - Contains command to use pip toinstall flask, along with info about virtual environments
- https://pypi.org/project/Flask/
  - Python Package Index - project page

## Installing flask Globally

At least for right now, we want all sites to use the same, current version of flask.

So we are not going to worry about environments and the like.

## Starting From Not Quite Scratch:

Having installed django, we now have pip already installed.

```
$ apt list | grep python3-flask/
python3-flask/focal,focal 1.1.1-2 all
$ apt list | grep python3-pip/
python3-pip/focal,focal,now 20.0.2-5ubuntu1 all [installed]
$ apt list --installed | grep python3-pip
$ apt list --installed | grep python3-flask/
$
```

## Installing pip

Having installed django, we now have pip already installed.  For details about the process, see "Installing pip" above.

## Installing the Latest Version of flask

The apt list command above under "Starting From Not Quite Scratch" shows the "current version" as being 1.1.1-2.

The wikipedia page above under "References" shows the "current version" as being 1.1.2.  Note the subtle difference!

We want the latest, so we go to https://flask.palletsprojects.com/en/1.1.x/installation/ and find the very simple command we need to run.

**Using `pip` to install flask instead of `apt`.**

```
$ pip install Flask
Collecting Flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 145 kB/s
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 143 kB/s
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 141 kB/s
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 144 kB/s
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux1_x86_64.whl (32 kB)
Installing collected packages: MarkupSafe, Jinja2, click, Werkzeug, itsdangerous, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
$
```

## The Settings File Is Needed for All Django Sites

Get a copy of `gitignored/Site/Site/settings.py` from another host.

E.g., on bette for joomoowebsites.com:

```
$ gojm                                 # /var/www/joomoowebsites.com/htdocs/joomoowebsites.com/
$ cd gitignored/Site/
$ l
$ rd  joomoowebsites_config.py         # if there are differences, check in the current version
$ toJane -y joomoowebsites_config.py
$ cd RCS/
$ toJane -y
$
```

And on bette for groja.com:

```
$ gog                           # /var/www/groja.com/htdocs/groja.com/
$ cd gitignored/Site/
$ l
$ rd groja_config.py            # if there are differences, check in the current version
$ toJane -y groja_config.py
$ cd RCS/
$ toJane -y
$ cd ..
$ l
$ l db/                         # empty
```

**Note: for groja.com we also need the database, so see `2d-groja.md`.**

## The Module Is Needed for All Flask Sites

Running `run.sh` for both sites gives the following error:

```
$ gogs
$ cd bin
$ ./run.sh
ModuleNotFoundError: No module named 'flask_bootstrap'
$
```

Find and install the flask_bootstrap module:

```
$ pip search bootstrap | grep -i flask           # pip search is case-insensitive by default, grep is not, so use -i
Bootstrap-Flask (1.3.2)                          - Bootstrap helper for Flask/Jinja2.
Flask-Bootstrap (3.3.7.1)                        - An extension that includes Bootstrap in your project, without any boilerplate code.
Flask-Bootstrap-Components (0.1.8)               - Collection of HTML generation helpers for Flask with Bootstrap 4
root@jane: ~
$ pip install Flask-Bootstrap
Collecting Flask-Bootstrap
  Downloading Flask-Bootstrap-3.3.7.1.tar.gz (456 kB)
     |████████████████████████████████| 456 kB 128 kB/s
. . .
. . .
. . .
Installing collected packages: dominate, visitor, Flask-Bootstrap
Successfully installed Flask-Bootstrap-3.3.7.1 dominate-2.5.1 visitor-0.1.3
$
```

