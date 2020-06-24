
# 3d-barbara-apache.md

Installing apache on barbara.

**NOTE:** Not worrying about ssl **working** at this juncture, because the site must be live for that.

We **do** want to set it up to use SSL, though!

## References

### References Used for Setting up jane

- Includes info about setting up SSL
  - https://tecadmin.net/install-apache-ubuntu-20-04/
- Includes info about setting up Virtual Hosts:
  - https://linuxhint.com/install_apache_server_setup_virtual_hosts_ubuntu/
- Includes Firewall configuration:
  - https://linuxhint.com/install_apache_web_server_ubuntu/
- How to enable wsgi apps - needed for python:
  - https://askubuntu.com/questions/25374/how-do-you-install-mod-wsgi

### Reference Needed for Setting up barbara

- Explains how to move SSL certificates from one host to another
  - https://serverfault.com/questions/209409/moving-ssl-certificate-from-one-apache-server-to-another

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

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

