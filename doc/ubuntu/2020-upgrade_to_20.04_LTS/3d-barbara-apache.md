
# 3d-barbara-apache.md

Installing apache on barbara.

**NOTE:** Not worrying about ssl **working** at this juncture, because the site must be live for that.

We **do** want to set it up to use SSL, though!

# Process - The Big Picture

- [ ] 1. Install Apache
- [ ] 2. Fix Configuration Files
- [ ] 3. Setup SSL

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

### Additional Reference Needed for Setting up barbara

- Explains how to move SSL certificates from one host to another
  - https://serverfault.com/questions/209409/moving-ssl-certificate-from-one-apache-server-to-another

# Install Apache - Process and Commands

## Process Overview:

- 1. Update everything so we have the latest of any associated dependencies, etc.
- 2. Install apache2
- 3. Update configuration files as necessary
  - 3.1. Update main config files
  - 3.2. Update config files for individual sites
- 4. Run `collectstatic.sh` for each django site
- 5. Restart apache and test

## Commands:

```
apt-get update
apt-get upgrade -y
apt install apache2
apt-get install libapache2-mod-wsgi-py3
cd /etc/apache2/conf
```

# Fix the Configuration Files

Overview:

Use files on ava as starting points

- 0. Create a tar file to help copy files from ava to barbara
- 1. Update files in top-level directory
- 2. Add site-specific config files from ava, updating them as needed for barbara
- 3. Rename unused files as done at the end of `1e-jane-needed_for_all_sites.md`
- 4. Test and ensure all sites work ok.
- 5. Ensure all current versions are checked into RCS
- 6. Clean up the files as appropriate, e.g., deleting obsolete comments, etc.
- 7. Check all final versions into RCS

## Step 1: Tar File From ava

Copy the files from ava in one fell swoop.

On ava:

```
cd /etc/apache2
tar -cvzf  config_for_barbara.tgz apache2.conf envvars sites-available/*.conf
. . .
. . .
. . .
mv config_for_barbara.tgz /tmp
cd /tmp
toBarbara config_for_barbara.tgz
```

## Step 2: Top-level Configuration Files

- 1. Update the files in the top-level directory.

Get updates made for previous installs by looking for "CusTOMizations" in /ubuntu-16.04/etc/apache2

On barbara:

```
cd /etc/apache2/
l
mkdir RCS
ci -l apache2.conf             # 'Installed version.'
rd apache2.conf
diff ~/unpack/apache2.conf apache2.conf     # cusTOMizations plus other updates
cat ~/unpack/apache2.conf                   # grab just the cuTOMizations
cat >> apache2.conf                         # and paste them at the end
rd apache2.conf
ci -l apache2.conf             # 'Added cusTOMizations: "ServerName ava", disable indexes, and a bunch of comments.'

diff ~/unpack/envvars envvars      # just cusTOMizations
cat ~/unpack/envvars               # grab just the cusTOMizations
cat >> envvars                     # and paste them at the end
rd envvars
ci -l envvars                  # 'Added definitions of GROJA_MAIL_FROM and GROJA_MAIL_TO .'
```

## Step 3: Site-specific Configuration

Updating the configuration part two - update the virtual hosts files.

Check in the versions installed in /etc/apache2/sites-available :

```
cd /etc/apache2/sites-available
mkdir RCS
ci -l 000-default.conf default-ssl.conf        # 'Installed version.'
rd *.conf
```

Note that old config files for each site are in /ubuntu-16.04/etc/apache2/sites-available .

### Look for Changes Made by the Maintainers

First, though, see whether the maintainers have made any changes to the installed `*default*.conf` server config files:

```
$ diff ~/unpack/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
11,14c11,12
<       ### ServerAdmin webmaster@localhost
<       ### DocumentRoot /var/www/html
<       ServerAdmin junk@tomhartung.com
<       DocumentRoot /var/www
---
>       ServerAdmin webmaster@localhost
>       DocumentRoot /var/www/html
22d19
<       LogLevel info
24c21
<       CustomLog ${APACHE_LOG_DIR}/access.log vhost_combined
---
>       CustomLog ${APACHE_LOG_DIR}/access.log combined
$ diff ~/unpack/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
14c14
<               CustomLog ${APACHE_LOG_DIR}/access.log vhost_combined
---
>               CustomLog ${APACHE_LOG_DIR}/access.log combined
$
```

**These are changes we want to keep:** so just copy the old config files into the new directory.

```
cp ~/unpack/sites-available/000-default.conf .
cp ~/unpack/sites-available/default-ssl.conf  .
rd *.conf
ci -l *.conf                    # "Updated to the version of this default file I am more likely to use."
```

Also copy and check in the wsgi test file.

```
cp  ~/unpack/sites-available/150-wsgi.test.conf .
ci -l 150-wsgi.test.conf                         # "Adding a wsgi test file that might come in handy someday when troubleshooting."
```

### Copy and Rename the Files, Change the hostname, and Test

Copy the site files used on ava, rename a few of them, change the hostname, and test the sites.

```
$ ~/unpack/sites-available/*.com*
total 144
-rw-r--r-- 1 root root 3578 Dec 29  2018 /root/unpack/sites-available/010-artsyvisions.com.conf
-rw-r--r-- 1 root root 3687 Dec 29  2018 /root/unpack/sites-available/012-artsyvisions.com-redirect.conf
. . .
. . .
. . .
-rw-r--r-- 1 root root 2086 May 29  2017 /root/unpack/sites-available/082-tomwhartung.com-redirect.conf
-rw-r--r-- 1 root root 2406 Jun  1  2017 /root/unpack/sites-available/084-tomwhartung.com-le-ssl.conf
$ cp ~/unpack/sites-available/*.com* .
```

Rename files that we do not use, adding `UNUSED` to the name.

```
mv 014-artsyvisions.com-self_signed-ssl.conf 014-artsyvisions.com-ss_snakeoil-ssl-UNUSED.conf
mv 024-groja.com-self_signed-ssl.conf 024-groja.com-ss_snakeoil-ssl-UNUSED.conf
l *self*   # make sure we got them all

mv 016-artsyvisions.com-le-ssl-redirect.conf 016-artsyvisions.com-le-ssl-redirect-UNUSED.conf
mv 026-groja.com-le-ssl-redirect.conf 026-groja.com-le-ssl-redirect-UNUSED.conf
mv 046-joomoowebsites.com-le-ssl-redirect.conf 046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf
mv 056-seeourminds.com-le-ssl-redirect.conf 056-seeourminds.com-le-ssl-redirect-UNUSED.conf
mv 066-tomhartung.com-le-ssl-redirect.conf 066-tomhartung.com-le-ssl-redirect-UNUSED.conf
l *ssl-redirect*   # make sure we got them all
```

Check in the files before changing any of them.  Don't worry about the `*tomwhartung*` for now, those will come from jane.

```
ci -l 0[12456]*.conf        # "Apache config file copied from ava 2020-06-24."
```

Change all occurrences of `ava\.` to `barbara.`  There should be precisely one occurrence in each file.

```
$ vi 0[12456]*.conf
$
```

Link only the non-ssl using, "skid row," `0[12456]0*.conf` files in `sites-available` to `sites-enabled`:

```
$ cd /etc/apache2/sites-enabled
$ l ../sites-available/0[12456]0*.conf
$ ln -s ../sites-available/0[12456]0*.conf .
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

Test the config files.

```
$ apache2ctl configtest
AH00526: Syntax error on line 33 of /etc/apache2/sites-enabled/010-artsyvisions.com.conf:
Invalid command 'WSGIDaemonProcess', perhaps misspelled or defined by a module not included in the server configuration
Action 'configtest' failed.
The Apache error log may have more information.
```

This is an easy fix: https://stackoverflow.com/questions/20627327/invalid-command-wsgiscriptalias-perhaps-misspelled-or-defined-by-a-module-not#20627328

Might as well enable vhosts while we're at it.

```
$ apt-get install libapache2-mod-wsgi
$ a2enmod wsgi
$ a2enmod vhost_alias
$ apache2ctl configtest
Syntax OK
$
```

Restart apache2:

```
systemctl restart apache2
```

Now getting a 500 error.
Oops, I thought that python2 stuff I saw while isntalling mod-wsgi looked suspicious.

Fix: https://stackoverflow.com/questions/14927345/importerror-no-module-named-django-core-wsgi-apache-virtualenv-aws-wsgi#22477904

```
apt-get remove libapache2-mod-python libapache2-mod-wsgi
apt-get install libapache2-mod-wsgi-py3
systemctl restart apache2
```

Sites starting to render, but the django sites have no style.

### Run `collectstatic.sh` for Each django Site

Run `collectstatic.sh` as follows:

```
goavs                  # /var/www/artsyvisions.com/htdocs/artsyvisions.com/Site
cd bin
./collectstatic.sh

gosss                  # /var/www/seeourminds.com/htdocs/seeourminds.com/Site
cd bin
./collectstatic.sh

goths                  # /var/www/tomhartung.com/htdocs/tomhartung.com/Site
cd bin
./collectstatic.sh
```

### Update the `*-tomwhartung.conf` Files

Get the new `*-tomwhartung.conf` files from jane, and update them for barbara.

On jane:

```
cp 08* ~/tmp
cd ~/tmp
toBarbara 08*
```

On barbara:

```
goeaa          # /etc/apache2/sites-available
$ rd 08*
rcsdiff: RCS/080-tomwhartung.com.conf,v: No such file or directory
rcsdiff: RCS/082-tomwhartung.com-redirect.conf,v: No such file or directory
rcsdiff: RCS/084-tomwhartung.com-le-ssl.conf,v: No such file or directory
$ mv ~tomh/tmp/08* .
mv: overwrite './080-tomwhartung.com.conf'? y
mv: overwrite './082-tomwhartung.com-redirect.conf'? y
mv: overwrite './084-tomwhartung.com-le-ssl.conf'? y
chown root:root 08*
$ vi 08*
```

Change all occurrences of `jane\.` to `barbara.`

Then enable the site, reload apache2, and run `collectstatic.sh`.

```
a2ensite 080-tomwhartung.com
systemctl reload apache2
```

```
gotws                  # /var/www/tomwhartung.com/htdocs/tomwhartung.com/Site
cd bin
./collectstatic.sh
```

## Step 4: Checkin, Cleanup, and Checkin Again

### Check in the Working Versions

Check in all site-specific config files.

```
goeaa                     # /etc/apache2/sites-available
l 0[124568]*.conf
rd 0[124568]*.conf
ci -l 0[12456]*.conf    # "Changed for use on barbara instead of ava."
rd 08*.conf
ci -l 08*.conf          # "Initial version copied from jane."
```

### Cleanup and Retest

- Remove old comments from the trial-and-error days
- Do not change any configuration commands

```
vi 0[124568]*.conf
```

Restart apache and ensure each site still loads

```
systemctl reload apache2
```

Assuming no configuration was changed, everything should still work!

### Check in the Final Working Versions

```
goeaa                     # /etc/apache2/sites-available
l 0[124568]*.conf
rd 0[124568]*.conf
ci -l 0[124568]*.conf    # "Removed old comments that I have deemed unneeded."
```

# Setup SSL

We want to use the same certificates we are using on ava, now on barbara.

**The life-saving reference:**

- https://serverfault.com/questions/209409/moving-ssl-certificate-from-one-apache-server-to-another

