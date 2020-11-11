
# 4e-ava-apache.md

Installing apache on ava.

# Process - The Big Picture

- [x] 1. Install Apache
- [x] 2. Fix Configuration Files
- [ ] 3. Setup SSL - later...

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
apt install libapache2-mod-wsgi-py3
cd /etc/apache2/conf
```

# Fix the Configuration Files

Overview:

Use files on ava as starting points

- 1. Create a tar file to help copy files from ava to barbara
- 2. Update files in top-level directory
- 3. Add site-specific config files from barbara, updating them as needed for ava
  - 3.1. Remove all `*UNUSED*` config files - enough is enough
  - 3.2. Test and ensure all sites work ok.
- 6. Ensure all current versions are checked into RCS

## Step 1: Tar File From ava

Copy the files from barbara in one fell swoop.

On barbara:

```
cd /etc/apache2
tar -cvzf  config_for_ava.tgz apache2.conf envvars sites-available/*.conf
. . .
. . .
. . .
mv config_for_ava.tgz /tmp
cd /tmp
toAva config_for_ava.tgz
```

On ava:

```
cd
l
mkdir unpack
cd  unpack
mv /tmp/config_for_ava.tgz .
l
tar -xvzf config_for_ava.tgz
l
```

## Step 2: Top-level Configuration Files

- 1. Update the files in the top-level directory.

Get updates made for previous installs by looking for "CusTOMizations" in /ubuntu-16.04/etc/apache2

On ava:

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

We are using the config files for each site that we copied from barbara.

### Look for Changes Made by the Maintainers

Quickly checking to see whether the maintainers made any changes to the installed `*default*.conf` server config files since we did barbara:

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

Didn't think so.  **Just copy the old config files into the new directory.**

Note: this is why we use `vhost_combined`:

- https://chrisk.io/apache2-vhost-combined-log-files/

First copy the `*default*.conf` files:

```
cp ~/unpack/sites-available/*default*.conf  .
rd *.conf
ci -l *.conf                    # "Updated to the version of this default file I am more likely to use, cos dats how I roll."
```

Also copy and check in the wsgi test file.

```
cp  ~/unpack/sites-available/150-wsgi.test.conf .
ci -l 150-wsgi.test.conf                         # "Adding a wsgi test file that might come in handy someday when troubleshooting."
```

### Copy the Site-Specific Files, Change the hostname, and Test

Copy the site files used on barbara, rename a few of them, change the hostname, and test the sites.

```
$ l ~/unpack/sites-available/*.com*
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

Check in the files before changing any of them.

```
ci -l 0*.conf        # "Apache config file copied from barbara 2020-07-01."
```

Remove all `*UNUSED*` files and mark the corresponding RCS files as obsolete.

```
$ rm  *UNUSED*
rm: remove regular file '016-artsyvisions.com-le-ssl-redirect-UNUSED.conf'? y
rm: remove regular file '026-groja.com-le-ssl-redirect-UNUSED.conf'? y
rm: remove regular file '046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf'? y
rm: remove regular file '056-seeourminds.com-le-ssl-redirect-UNUSED.conf'? y
rm: remove regular file '066-tomhartung.com-le-ssl-redirect-UNUSED.conf'? y
$ cd RCS
$ l *UNUSED*
-r--r--r-- 1 root root 3766 Jul  1 12:52 016-artsyvisions.com-le-ssl-redirect-UNUSED.conf,v
-r--r--r-- 1 root root 2412 Jul  1 12:52 026-groja.com-le-ssl-redirect-UNUSED.conf,v
-r--r--r-- 1 root root 2466 Jul  1 12:53 046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf,v
-r--r--r-- 1 root root 4042 Jul  1 12:53 056-seeourminds.com-le-ssl-redirect-UNUSED.conf,v
-r--r--r-- 1 root root 3730 Jul  1 12:53 066-tomhartung.com-le-ssl-redirect-UNUSED.conf,v
$ mv 016-artsyvisions.com-le-ssl-redirect-UNUSED.conf,v 016-artsyvisions.com-le-ssl-redirect-UNUSED.conf,o
$ mv 026-groja.com-le-ssl-redirect-UNUSED.conf,v 026-groja.com-le-ssl-redirect-UNUSED.conf,o
$ mv 046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf,v 046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf,o
$ mv 056-seeourminds.com-le-ssl-redirect-UNUSED.conf,v 056-seeourminds.com-le-ssl-redirect-UNUSED.conf,o
$ mv 066-tomhartung.com-le-ssl-redirect-UNUSED.conf,v 066-tomhartung.com-le-ssl-redirect-UNUSED.conf,o
$ l *UNUSED*
-r--r--r-- 1 root root 3766 Jul  1 12:52 016-artsyvisions.com-le-ssl-redirect-UNUSED.conf,o
-r--r--r-- 1 root root 2412 Jul  1 12:52 026-groja.com-le-ssl-redirect-UNUSED.conf,o
-r--r--r-- 1 root root 2466 Jul  1 12:53 046-joomoowebsites.com-le-ssl-redirect-UNUSED.conf,o
-r--r--r-- 1 root root 4042 Jul  1 12:53 056-seeourminds.com-le-ssl-redirect-UNUSED.conf,o
-r--r--r-- 1 root root 3730 Jul  1 12:53 066-tomhartung.com-le-ssl-redirect-UNUSED.conf,o
$ cd -
```

Then edit the remaining files, changing all occurrences of `barbara\.` to `ava.`
There should be precisely one occurrence in each file.
Also, check each file into RCS.

```
vi 0*.conf
rd 0*.conf
ci -l 0*.conf      # "Changed the ServerName or ServerAlias - as appropriate - from barbara to ava."
```

Link only the non-ssl using, "skid row," `0[124568]0*.conf` files in `sites-available` to `sites-enabled`:

**Note: we do not want to link the `000-default.conf` file!**  It may be linked by default.

```
$ cd /etc/apache2/sites-enabled
$ l
total 0
lrwxrwxrwx 1 root root 35 Jul  1 12:17 000-default.conf -> ../sites-available/000-default.conf
$ rm 000-default.conf
$ l ../sites-available/0[124568]0*.conf
$ ln -s ../sites-available/0[124568]0*.conf .
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

Enable vhosts, test the config files, and restart apache2:

```
$ a2enmod vhost_alias
$ apache2ctl configtest
Syntax OK
$ systemctl restart apache2
$
```

## Step 4. Run `collectstatic.sh` for Each django Site

Run `collectstatic.sh` as follows:

```
goavsb                  # /var/www/artsyvisions.com/htdocs/artsyvisions.com/Site/bin
./collectstatic.sh

gosmsb                  # /var/www/seeourminds.com/htdocs/seeourminds.com/Site/bin
./collectstatic.sh

gothsb                  # /var/www/tomhartung.com/htdocs/tomhartung.com/Site/bin
./collectstatic.sh

gotwsb                  # /var/www/tomhartung.com/htdocs/tomhartung.com/Site/bin
./collectstatic.sh
```

## Step 5. Restart Apache and Test

Restart apache and ensure each site loads.

```
systemctl reload apache2
```

Access each site as http://ava.[site_name].com from the My Sites index page in `/var/www`.

Ensure all site-specific config files are checked in.

```
goeaa                   # /etc/apache2/sites-available
l 0*.conf
rd 0*.conf
ci -l 0*.conf           # "Changed for use on ava instead of barbara."
```

