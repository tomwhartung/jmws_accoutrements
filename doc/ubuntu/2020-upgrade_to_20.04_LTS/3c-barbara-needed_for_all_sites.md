
# 3c-barbara-needed_for_all_sites.md

Instructions for installing the latest stable versions of software needed for two or more sites:

- Python
- Django
- Flask
- Apache

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

## Consideration: Python - Latest Version?

See `1e-jane-needed_for_all_sites.md` to learn why we are using 3.8.2 there, i.e.,
"the current version of python is now 3.8.3, but it is not yet available for upgrading to."

Be sure to **check the version of Python installed when installing 20.04 server on barbara**
and make and adjust plans as necessary.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

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
$ apt list | grep python3-pip/
python3-pip/focal,focal,now 20.0.2-5ubuntu1 all [installed]
$ apt list --installed | grep python3-pip
$ apt list --installed | grep python3-flask/
$
```

## Installing pip

Having installed django, we now have pip already installed.

For details about the process, see "Installing pip" above.

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

Both flask sites are now operational!

# Apache

Installing apache on jane to help identify the process we need when we install it on barbara and ava,
and so that jane can serve as an extra backup server in case we need it someday.

Not worrying about ssl at this juncture.

## References

There are many references showing how to install LAMP.
Fortunately we are done with all that and just want to install apache2

- Includes info about setting up SSL
  - https://tecadmin.net/install-apache-ubuntu-20-04/
- Includes info about setting up Virtual Hosts:
  - https://linuxhint.com/install_apache_server_setup_virtual_hosts_ubuntu/
- Includes Firewall configuration:
  - https://linuxhint.com/install_apache_web_server_ubuntu/
- How to enable wsgi apps - needed for python:
  - https://askubuntu.com/questions/25374/how-do-you-install-mod-wsgi

## Process and Commands

### Process Overview:

- 1. Update everything so we have the latest of any associated dependencies, etc.
- 2. Install apache2
- 3. Update configuration files as necessary
  - 3.1. Update main config files
  - 3.2. Update config files for individual sites
- 4. Run `collectstatic.sh` for each django site
- 5. Restart apache and test

### Commands:

```
apt-get update
apt-get upgrade -y
apt install apache2
## apt-get install libapache2-mod-wsgi      ## WRONG!!!  SEE BELOW!!!
apt-get install libapache2-mod-wsgi-py3     ## YES!!!  SEE BELOW!!!
cd /etc/apache2/conf
```

## Fixing the Configuration Files

### Part 1: Installation-wide Configuration

Updating the configuration part one - update the files in the top-level directory.

Get updates made for previous installs by looking for "CusTOMizations" in /ubuntu-16.04/etc/apache2

```
cd /etc/apache2/
l
mkdir RCS
ci -l apache2.conf       # 'Installed version.'
vi apache2.conf          # Add "CusTOMizations"
rd apache2.conf
ci -l apache2.conf       # 'Added "ServerName jane" and a bunch of comments.'
ci -l envvars            # 'Installed version.'
vi envvars               # Add "CusTOMizations"
rd envvars
ci -l envvars            # 'Added definitions of GROJA_MAIL_FROM and GROJA_MAIL_TO .'
```

### Part 2: Site-specific Configuration

Updating the configuration part two - update the virtual hosts files.

Check in the versions installed in /etc/apache2/sites-available :

```
cd /etc/apache2/sites-available
mkdir RCS
ci -l 000-default.conf default-ssl.conf        # 'Installed version.'
rd *.conf
```

Note that old config files for each site are in /ubuntu-16.04/etc/apache2/sites-available .

#### Look for Changes Made by the Maintainers

First, though, see whether the maintainers have made any changes to the installed `*default*.conf` server config files:

```
diff /ubuntu-16.04/etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
diff /ubuntu-16.04/etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
```

I am seeing some changes I made to these files, and these two lines that are not in the installed version
yet are commented out in my old versions:

```
3,4d2
<       ### <VirtualHost *:443>
<       ### <VirtualHost jane.seeourminds.com:443>
```

Not totally sure where those came from or why, but they look like ideas I tried but that did not work,
and I left them in there so I wouldn't waste time trying them again.

More than that, lines 1-2 in both the old and new `default-ssl.conf` files are:

```
<IfModule mod_ssl.c>
        <VirtualHost _default_:443>
```

Which is obviously the syntax we want for this directive.
The comments are not useful, except to keep me from trying something similar again and again etc.

**Bottom line:** it looks like it will be ok to just copy the old config files into the new directory.

#### Copy the Files and Test

Just copy the files and test it, noting that:

- I really do not plan to use apache on jane
- I can't test ssl unless I go live

And really the whole point of this exercise is to just do what I can to help make
the server shuffle for barbara go more quickly.

```
$ rd *
===================================================================
RCS file: RCS/000-default.conf,v
retrieving revision 1.1
diff -r1.1 000-default.conf
===================================================================
RCS file: RCS/default-ssl.conf,v
retrieving revision 1.1
diff -r1.1 default-ssl.conf
$ l /ubuntu-16.04/etc/apache2/sites-available
total 144
-rw-r--r-- 1 root root 1417 Nov 21  2016 000-default.conf
-rw-r--r-- 1 root root 3509 Nov 24  2018 010-artsyvisions.com.conf
. . .
. . .
. . .
-rw-r--r-- 1 root root 2476 Jun  1  2017 086-tomwhartung.com-le-ssl-redirect.conf
-rw-r--r-- 1 root root 3169 Nov 21  2016 150-wsgi.test.conf
drwxr-xr-x 2 root root 4096 Jun 18 15:22 RCS
-rw-r--r-- 1 root root 6884 May 20  2017 default-ssl.conf
$ cp  /ubuntu-16.04/etc/apache2/sites-available/*.conf .
cp: overwrite './000-default.conf'? y
cp: overwrite './default-ssl.conf'? y
$
```

Link only the regular, "skid row," `??0-*.conf` files in `sites-available` to `sites-enabled`:

```
$ cd /etc/apache2/sites-enabled
$ l ../sites-available/??0-*.conf
$ ln -s  ../sites-available/??0-*.conf .
ln: failed to create symbolic link './000-default.conf': File exists
$ l
total 0
lrwxrwxrwx 1 root root 35 Jun 18 14:36 000-default.conf -> ../sites-available/000-default.conf
lrwxrwxrwx 1 root root 44 Jun 18 17:25 010-artsyvisions.com.conf -> ../sites-available/010-artsyvisions.com.conf
lrwxrwxrwx 1 root root 37 Jun 18 17:25 020-groja.com.conf -> ../sites-available/020-groja.com.conf
lrwxrwxrwx 1 root root 46 Jun 18 17:25 040-joomoowebsites.com.conf -> ../sites-available/040-joomoowebsites.com.conf
lrwxrwxrwx 1 root root 43 Jun 18 17:25 050-seeourminds.com.conf -> ../sites-available/050-seeourminds.com.conf
lrwxrwxrwx 1 root root 42 Jun 18 17:25 060-tomhartung.com.conf -> ../sites-available/060-tomhartung.com.conf
lrwxrwxrwx 1 root root 43 Jun 18 17:25 080-tomwhartung.com.conf -> ../sites-available/080-tomwhartung.com.conf
lrwxrwxrwx 1 root root 37 Jun 18 17:25 150-wsgi.test.conf -> ../sites-available/150-wsgi.test.conf
$
```

That's easier than running `a2ensite`, but oops, we wind up with too many links:

```
$ apache2ctl configtest
AH00526: Syntax error on line 16 of /etc/apache2/sites-enabled/080-tomwhartung.com.conf:
Invalid command 'RewriteEngine', perhaps misspelled or defined by a module not included in the server configuration
Action 'configtest' failed.
The Apache error log may have more information.
$ l sites-enabled/
$ rm  sites-enabled/080-tomwhartung.com.conf
rm: remove symbolic link 'sites-enabled/080-tomwhartung.com.conf'? y
$ apache2ctl configtest
AH00112: Warning: DocumentRoot [/var/www/learn/django/github/customizations/always_learning_python/3-mod_wsgi/documents] does not exist
Syntax OK
$ l sites-enabled/150-wsgi.test.conf
$ more sites-enabled/150-wsgi.test.conf
. . .
. . .
. . .
$ rm sites-enabled/150-wsgi.test.conf
rm: remove symbolic link 'sites-enabled/150-wsgi.test.conf'? y
$ apache2ctl configtest
Syntax OK
$
```

Now to start apache2:

```
systemctl restart apache2
```

Still having issues, as if the virtual hosts are not working.

```
$ rm  sites-enabled/000-default.conf
rm: remove symbolic link 'sites-enabled/000-default.conf'? y
$
```

It might help to enable the vhosts module.

```
l mods-available/          # See vhost_alias
l mods-enabled/            # No vhost_alias
a2enmod vhost_alias
l mods-enabled/            # Now vhost_alias is there
```

Now getting a 500 error.

Fix: https://stackoverflow.com/questions/14927345/importerror-no-module-named-django-core-wsgi-apache-virtualenv-aws-wsgi#22477904

```
apt-get remove libapache2-mod-python libapache2-mod-wsgi
apt-get install libapache2-mod-wsgi-py3
```

Sites starting to render.  Some have no style.

#### Run `collectstatic.sh` for Each django Site

Run `collectstatic.sh` as follows:

```
goavs                  # /var/www/artsyvisions.com/htdocs/artsyvisions.com/Site/bin
cd bin
./collectstatic.sh
gosss                  # /var/www/seeourminds.com/htdocs/seeourminds.com/Site/bin
cd bin
./collectstatic.sh
```

And so on, as necessary.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#### Update the `*-tomwhartung.conf` Files

Finally, we need to update the `*-tomwhartung.conf` files to serve python3 rather than php apps.

