
# 4d-ava-needed_for_all_sites.md

Instructions for installing the latest stable versions of software needed for two or more sites:

- Python
- Django
- Flask
- Apache: see `4e-ava-apache.md`

# Cloning the Source Repos

Extract the source files for the six sites by entering the following commands:

```
govw        # /var/www
mkdir -p artsyvisions.com/htdocs
cd artsyvisions.com/htdocs
git clone git@github.com:tomwhartung/artsyvisions.com.git

govw        # /var/www
mkdir -p groja.com/htdocs
cd groja.com/htdocs
git clone git@github.com:tomwhartung/groja.com.git

govw        # /var/www
mkdir -p joomoowebsites.com/htdocs
cd joomoowebsites.com/htdocs
git clone git@github.com:tomwhartung/joomoowebsites.com.git

govw        # /var/www
mkdir -p seeourminds.com/htdocs
cd seeourminds.com/htdocs
git clone git@github.com:tomwhartung/seeourminds.com.git

govw        # /var/www
mkdir -p tomhartung.com/htdocs
cd tomhartung.com/htdocs
git clone git@github.com:tomwhartung/tomhartung.com.git

govw        # /var/www
mkdir -p tomwhartung.com/htdocs
cd tomwhartung.com/htdocs
git clone git@github.com:tomwhartung/tomwhartung.com.git
```

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

# Python

The current version of python is now 3.8.3, but it is not yet available for upgrading to.

## Consideration: Python - Latest Version?

See `1e-jane-needed_for_all_sites.md` to learn why we are using 3.8.2 there, i.e.,
"the current version of python is now 3.8.3, but it is not yet available for upgrading to."

**The main thing it should be current and match what we use on jane and ava.**

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

## Finding the Starting Point

The `pip3` package should already be installed from the last step, `3b-barbara-server-sanity_please.md`,
and should run when we enter just `pip`.

```
$ apt list | grep python3-pip/
python3-pip/focal,now 20.0.2-5ubuntu1 all [installed]
$ apt list | grep python3-django/
python3-django/focal-updates,focal-updates,focal-security,focal-security 2:2.2.12-1ubuntu0.1 all
$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
$
```

## Installing the Latest Version of Django

Use `pip` to install django instead of `apt`, so we get the current version.

```
$ pip install django==3.0.6
Collecting django==3.0.6
  Downloading Django-3.0.6-py3-none-any.whl (7.5 MB)
     |████████████████████████████████| 7.5 MB 163 kB/s
Collecting asgiref~=3.2
  Downloading asgiref-3.2.10-py3-none-any.whl (19 kB)
Collecting pytz
  Downloading pytz-2020.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 169 kB/s
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 140 kB/s
Installing collected packages: asgiref, pytz, sqlparse, django
Successfully installed asgiref-3.2.10 django-3.0.6 pytz-2020.1 sqlparse-0.3.1
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

Get a copy of `gitignored/Site/Site/settings.py` from another host, i.e., barbara.

Copy the `settings.py` file to ava.

Commands to run on barbara:

```
goav                     # var/www/artsyvisions.com/htdocs/artsyvisions.com
l
cd gitignored/Site/Site/
l
toBarbara -y settings.py

govw                     # /var/www
cd seeourminds.com/htdocs/seeourminds.com/gitignored/Site/Site/
toBarbara -y settings.py

govw                     # /var/www
cd tomhartung.com/htdocs/tomhartung.com/gitignored/Site/Site/
toBarbara -y settings.py

govw                     # /var/www
cd tomwhartung.com/htdocs/tomwhartung.com/gitignored/Site/Site/
toBarbara -y settings.py
```

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Review and remember: **`SECURITY WARNING: don't run with debug turned on in production!`**

## Check All Django Sites for Sanity

Running `run.sh` for all django sites shows no errors.

All django sites should now be operational.

# Flask

References:

- https://en.wikipedia.org/wiki/Flask_(web_framework)
- https://flask.palletsprojects.com/en/1.1.x/installation/
  - Contains command to use pip to install flask, along with info about virtual environments
- https://pypi.org/project/Flask/
  - Python Package Index - project page
- https://python-forum.io/Thread-How-to-install-flask-boostrap
  - Contains command to use pip to install flask_bootstrap

## Installing flask Globally

At least for right now, we want all sites to use the same, current version of flask.

So we are not going to worry about environments and the like.

## Starting From Not Quite Scratch:

Having installed django, we now have pip already installed.

```
$ apt list | grep python3-flask/
python3-flask/focal,focal 1.1.1-2 all
$ apt list --installed | grep python3-flask/
$
```

## Installing the Latest Version of flask

The apt list command above under "Starting From Not Quite Scratch" shows the "current version" as being 1.1.1-2.

The wikipedia page above under "References" shows the "current version" as being 1.1.2.  Note the subtle difference!

We want the latest, so we go to https://flask.palletsprojects.com/en/1.1.x/installation/ and find the very simple command we need to run.

**Using `pip` to install flask instead of `apt`.**

```
$ pip install Flask
Collecting Flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 127 kB/s
Requirement already satisfied: click>=5.1 in /usr/lib/python3/dist-packages (from Flask) (7.0)
Requirement already satisfied: Jinja2>=2.10.1 in /usr/lib/python3/dist-packages (from Flask) (2.10.1)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 158 kB/s
Installing collected packages: itsdangerous, Werkzeug, Flask
Successfully installed Flask-1.1.2 Werkzeug-1.0.1 itsdangerous-1.1.0
$
```

## The Settings File Is Needed for All Flask Sites

Get a copy of `gitignored/Site/Site/settings.py` from another host, i.e., `jane`.

Run these commands on jane for joomoowebsites.com and groja.com:

```
gojm                                 # /var/www/joomoowebsites.com/htdocs/joomoowebsites.com/
cd gitignored/Site/
rd joomoowebsites_config.py
toBarbara -y
cd RCS/
toBarbara -y

gog                           # /var/www/groja.com/htdocs/groja.com/
cd gitignored/Site/
rd groja_config.py
toBarbara -y
cd RCS/
toBarbara -y
cd ../..
l db/
cd  db/
lsBarbara
toBarbara NameEmail*
govw
```

## The `flask_bootstrap` Module Is Needed for All Flask Sites

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
Collecting Flask-Bootstrap
  Downloading Flask-Bootstrap-3.3.7.1.tar.gz (456 kB)
     |████████████████████████████████| 456 kB 159 kB/s
Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.8/dist-packages (from Flask-Bootstrap) (1.1.2)
Collecting dominate
  Downloading dominate-2.5.1-py2.py3-none-any.whl (29 kB)
Collecting visitor
  Downloading visitor-0.1.3.tar.gz (3.3 kB)
Requirement already satisfied: Werkzeug>=0.15 in /usr/local/lib/python3.8/dist-packages (from Flask>=0.8->Flask-Bootstrap) (1.0.1)
Requirement already satisfied: Jinja2>=2.10.1 in /usr/lib/python3/dist-packages (from Flask>=0.8->Flask-Bootstrap) (2.10.1)
Requirement already satisfied: itsdangerous>=0.24 in /usr/local/lib/python3.8/dist-packages (from Flask>=0.8->Flask-Bootstrap) (1.1.0)
Requirement already satisfied: click>=5.1 in /usr/lib/python3/dist-packages (from Flask>=0.8->Flask-Bootstrap) (7.0)
Building wheels for collected packages: Flask-Bootstrap, visitor
  Building wheel for Flask-Bootstrap (setup.py) ... done
  Created wheel for Flask-Bootstrap: filename=Flask_Bootstrap-3.3.7.1-py3-none-any.whl size=460123 sha256=50218628f54ca1e38e27ba16eb61f81b568677ff82ad7566df024d458cd0500d
  Stored in directory: /root/.cache/pip/wheels/f2/a3/85/fe8b65a65a447c9906e3b7edb7d9e6c74dfa9c8425c3dd3007
  Building wheel for visitor (setup.py) ... done
  Created wheel for visitor: filename=visitor-0.1.3-py3-none-any.whl size=3931 sha256=c21be597de79994a0b1b4da8484f1c38a103884630f2b6eddba66835f2067e24
  Stored in directory: /root/.cache/pip/wheels/d3/40/52/5dae7760434a82caf8b8f88323029188b2d4ea3ac1235e550a
Successfully built Flask-Bootstrap visitor
Installing collected packages: dominate, visitor, Flask-Bootstrap
Successfully installed Flask-Bootstrap-3.3.7.1 dominate-2.5.1 visitor-0.1.3
$
```

Running `run.sh` for both sites shows they are now operational.

# Apache2

Apache2 is also needed for all sites, but all that is in a different file.

For information about installing apache2 on barbara, see `3d-barbara-apache.md`.

