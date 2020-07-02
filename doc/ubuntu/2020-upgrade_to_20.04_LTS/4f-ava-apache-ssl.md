
# 4f-ava-apache-ssl.md

Implementing ava as a backup server, so it needs to be able to run ssl.

# Setup SSL

We want to use the same certificates we are using on barbara.

- All letsencrypt files are in `/etc/letsencrypt`

## References

- (1) Formely I thought this was "the life-saving reference," but now I am not so sure:
  - https://serverfault.com/questions/209409/moving-ssl-certificate-from-one-apache-server-to-another
  - It is from 2010-12-05, making it almost ten years old
- (2) This one also says to just copy the files referenced in the apache config file:
  - https://askubuntu.com/questions/437340/how-to-export-an-ssl-certificate-from-one-to-another-server-server-migration
  - This reference is also fairly old, from 2014
- (3) A **much** more detailed and newer - 201[89], ubuntu 16.04 - reference :
  - https://www.liquidweb.com/kb/transfer-an-ssl-to-ubuntu-16-04-or-centos-7/
  - Has some interesting things but is not 100% correct - see below
- (4) From 2019-03-26 and for 18.04
  - https://ivanderevianko.com/2019/03/migrate-letsencrypt-certificates-certbot-to-new-server
  - This looks like the best one so far
- (5) From 2020-04-29 and for 20.04
  - https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04
  - The most current reference but shows how to start from scratch rather than how to migrate
- (6) From /etc/letsencrypt//README
  - https://certbot.eff.org/docs/using.html#where-are-my-certificates
  - Looks like a comprehensive reference rather than a how-to
  - Maybe use for troubleshooting
- (7) From 2020-06-05 and for 20.04
  - https://www.cyberciti.biz/faq/how-to-install-apache-on-ubuntu-20-04-lts/
  - Maybe use for troubleshooting apache issues?
- (8) From 2020-06-07 and for 20.04
  - https://www.cyberciti.biz/faq/how-to-secure-apache-with-mod_md-lets-encrypt-on-ubuntu-20-04-lts/
  - Instructions for starting from scratch, which I do not want to do
  - Also it looks a little suspicious, e.g., several grammatical errors
  - More significantly the page for the mod_md module on apache.org says it is "Experimental"
    - https://httpd.apache.org/docs/2.4/mod/mod_md.html
  - Maybe use for troubleshooting?

## Observations

### "New" commands:

Reference (7) has some sample commands for managing apache:

```
systemctl restart apache2        # what the references suggest running to restart apache
systemctl start apache2.service
systemctl stop apache2.service
systemctl reload apache2.service
systemctl status apache2.service
```

Another "new" command:

```
apache2ctl -S               # shows the status of virtual hosts, etc.
apache2ctl configtest       # test the syntax in the config files
```

### Need the Entire `/etc/letsencrypt` Directory Tree

It's clear from setting up barbara that we need the entire `/etc/letsencrypt` directory tree.
For details behind this reasoning, see `3e-barbara-apache-ssl.md`.

### Installing Required `certbot` Packages

Reference (5) points out we need to install two certbot packages, `certbot` and `python3-certbot-apache`.

### Renewal crontab and Testing

Reference (4) points out that there is a crontab, but the one installed with certbot seems to do just fine.

Reference (4) also points out we can test the renewal:

```
letsencrypt renew --dry-run
```

## Process

This process was successful on barbara.  For details, see `3e-barbara-apache-ssl.md`.

- [x] 1. Install certbot packages
- [x] 2. Put all of the `/etc/letsencrypt` directory on barbara into a tar file
- [x] 3. Copy the tar file to barbara and unpack it
- [x] 4. Enable mod_ssl on ava
- [x] 5. Switch over the apache config files
    - [x] 5.1. Disable the `0[124568]0-*` files in `/etc/apache2/sites-available/`
    - [x] 5.2. Enable the `0?[24]-*` files in `/etc/apache2/sites-available/`
    - [x] 5.3. Check apache Config and Restart Apache
- [ ] 6. Switch server to barbara
    - [ ] 6.1. Tail apache access and error log files on ava and barbara
          - `tapa` and `tape` aliases
    - [ ] 6.2. Update tp-link router at `192.168.1.1`
          - Be sure to document changes made so we can un-do them if necessary
    - [ ] 6.3. Update `/etc/hosts` and `/var/www/inde .html` on jane
    - [ ] 6.4. Test sites in browser
          - Check https, which should work
          - Check http, which should redirect to https
- [ ] 7. Decide whether to keep barbara the server or fall back to ava and regroup
- [ ] 8. If necessary, create crontab on barbara, or check to see if certbot has one - **?????**
- [ ] 9. Troubleshooting tomwhartung.com

## Steps, Commands, and Notes

Following the steps with increased confidence, having run through this process, successfully for the most part, on barbara.

### 1. Install Certbot Packages

On ava:

```
$ apt list certbot python3-certbot-apache
Listing... Done
certbot/focal,focal 0.40.0-1 all
python3-certbot-apache/focal,focal 0.39.0-1 all
$ apt install certbot python3-certbot-apache
. . .
. . .
. . .
$ apt list certbot python3-certbot-apache
Listing... Done
certbot/focal,focal,now 0.40.0-1 all [installed]
python3-certbot-apache/focal,focal,now 0.39.0-1 all [installed]
$ cd /etc
$ ll letsencrypt
total 20
drwxr-xr-x   2 root root  4096 Jul  2 11:19 .
drwxr-xr-x 136 root root 12288 Jul  2 11:19 ..
-rw-r--r--   1 root root   121 May 26  2018 cli.ini
$ cat  letsencrypt/cli.ini
# Because we are using logrotate for greater flexibility, disable the
# internal certbot logrotation.
max-log-backups = 0$                      # sic - the file is missing a newline at the end
```

Note that the only file installed, `cli.ini`, matches the one installed on barbara.

On barbara:

```
$ cd /etc
$ cat letsencrypt/cli.ini
# Because we are using logrotate for greater flexibility, disable the
# internal certbot logrotation.
max-log-backups = 0$                      # sic - the file is missing a newline at the end
```

### 2. Put the `/etc/letsencrypt` Directory on barbara Into a Tar File

Put all of the `/etc/letsencrypt` directory on barbara into a tar file.

On barbara:

```
cd /etc
tar -cvzf /tmp/letsencrypt-for_ava-2020_06_26.tgz letsencrypt/
chown tomh:tomh /tmp/letsencrypt-for_ava-2020_06_26.tgz
```

### 3. Copy the Tar File to ava, and Unpack and Install It

On barbara:

```
cd /tmp
toAva letsencrypt-for_ava-2020_06_26.tgz
```

On ava:

```
cd ~/unpack/
ll
rm -fr *
mv /tmp/letsencrypt-for_ava.tgz .
ll
tar -xvzf letsencrypt-for_ava.tgz
cd /etc
ll letsencrypt/
diff  letsencrypt/cli.ini ~/unpack/letsencrypt/cli.ini
mv letsencrypt letsencrypt-installed
mv ~/unpack/letsencrypt .
ll letsencrypt
```

### 4. Enable mod_ssl on barbara

For grins, restart apache and test sites before enabling the module.

```
$ a2enmod ssl
Considering dependency setenvif for ssl:
Module setenvif already enabled
Considering dependency mime for ssl:
Module mime already enabled
Considering dependency socache_shmcb for ssl:
Enabling module socache_shmcb.
Enabling module ssl.
See /usr/share/doc/apache2/README.Debian.gz on how to configure SSL and create self-signed certificates.
To activate the new configuration, you need to run:
  systemctl restart apache2
$ systemctl restart apache2
$
```

The sites still work after running `systemctl restart apache2`.

### 5. Switch Over the Apache Config Files

Use `ln -s` instead of `a2dissite ...` and `a2ensite ...`!

#### 5.1. Disable the `0[124568]0-*` files in `/etc/apache2/sites-available/`

```
goeae     # /etc/apache2/sites-enabled
rm -f *.conf
```

#### 5.2. Enable the `0?[24]-*` files in `/etc/apache2/sites-available/`

```
l ../sites-available/0?[24]*.conf
ln -s  ../sites-available/0?[24]*.conf
```

Voila!

#### 5.3. Check Apache Config and Restart Apache

```
$ apache2ctl configtest
Syntax OK
$ systemctl restart apache2
$
```

### 5. Switch server to barbara

#### 6.1. Tail apache access and error log files on ava and barbara

On barbara and ava, four windows total.

```
tapa  # In one window
tape  # In another
```

#### 6.2. Update tp-link router at `192.168.1.1`

Process:

1. Access http://192.168.1.1/ and sign in
2. Menu -> Advanced -> NAT -> Virtual Server
3. ava -> Inactivate
4. ava -> Edit (Pencil) -> Change both port parameters to 81
5. ava-ssl -> Inactivate
6. ava-ssl -> Edit (Pencil) -> Change both port parameters to 445
7. barbara -> Edit (Pencil) -> Change both port parameters to 80
8. barbara -> Activate
9. barbara-ssl -> Edit (Pencil) -> Change both port parameters to 443
10. barbara-ssl -> Activate

#### 6.3. Update `/etc/hosts` and `/var/www/index.html` on jane

Update `/etc/hosts` and `/var/www/index.html` on jane to reflect the `www.*` and [no-prefix] sites are all now on barbara, `192.168.0.116`.

#### 6.4. Test sites in browser

All sites work ok except tomwhartung.com , which redirects to artsyvisions.com.  Rats.

#### 6.5. Log Files

- [x] Seeing activity in the logfiles on barbara.
- [x] Seeing **NO** activity in the logfiles on ava.

Nice.

### 7. Decide whether to keep barbara the server or fall back to ava and regroup

Since I do not have anything for tomwhartung.com yet, I say it's not a biggie, but try to fix it asap.

### 8. If necessary, create crontab on barbara, or check to see if certbot has one - **?????**

I do not think it is necessary, because the certbot cronjob is there.

```
$ cat /etc/cron.d/certbot
# /etc/cron.d/certbot: crontab entries for the certbot package
#
# Upstream recommends attempting renewal twice a day
#
# Eventually, this will be an opportunity to validate certificates
# haven't been revoked, etc.  Renewal will only occur if expiration
# is within 30 days.
#
# Important Note!  This cronjob will NOT be executed if you are
# running systemd as your init system.  If you are running systemd,
# the cronjob.timer function takes precedence over this cronjob.  For
# more details, see the systemd.timer manpage, or use systemctl show
# certbot.timer.
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

0 */12 * * * root test -x /usr/bin/certbot -a \! -d /run/systemd/system && perl -e 'sleep int(rand(43200))' && certbot -q renew
$
```

This must have been installed when I installed the certbot packages in Step 2.

**Hope it does what I think it does.**

### 9. Troubleshooting tomwhartung.com

Found a misconfiguration for STATIC_FILES in settings.py, but fixing it did not help.

I suspect it has something to do with ssl.

To be continued in `3f-barbara-fix-tomwhartung.md`.

