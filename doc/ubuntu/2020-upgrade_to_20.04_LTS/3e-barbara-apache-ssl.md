
# 3e-barbara-apache-ssl.md

Switching the server over to barbara and implementing ssl.

# Setup SSL

We want to use the same certificates we are using on ava, now on barbara.

- These files are all in `/etc/letsencrypt`

## References

The reference below is like 10 years old and this SSL stuff was giving me nightmares recently so let's dig a little deeper.

- (1) "The life-saving reference:"
  - https://serverfault.com/questions/209409/moving-ssl-certificate-from-one-apache-server-to-another
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
  - Maybe use for troubleshooting
- (8) From 2020-06-07 and for 20.04
  - https://www.cyberciti.biz/faq/how-to-secure-apache-with-mod_md-lets-encrypt-on-ubuntu-20-04-lts/
  - Maybe use for troubleshooting

## Observations

It's clear there is more than what references (1) and (2) propose, i.e., just copying the files.

Sample investigative commands from reference (3) show discrepancies between what they say and what I am seeing.

```
apache2ctl -S
apt-get install mod_ssl     # "E: Unable to locate package mod_ssl" - interesting
```

Reference (4) points out:

- Apache conf files want to the file in `/etc/letsencrypt/options-ssl-apache.conf` - not mentioned in (1) or (2), oops
  - Include /etc/letsencrypt/options-ssl-apache.conf
- Apache conf files point to "files" in `/etc/letsencrypt/live/*/` - but these are links, oops
  - SSLCertificateFile    /etc/letsencrypt/live/*/fullchain.pem
  - SSLCertificateKeyFile /etc/letsencrypt/live/*/privkey.pem

E.g., for groja.com:

```
$ l /etc/letsencrypt/live/groja.com/*
-rw-r--r-- 1 root root 543 May 24  2017 /etc/letsencrypt/live/groja.com/README
lrwxrwxrwx 1 root root  34 May 13 03:20 /etc/letsencrypt/live/groja.com/cert.pem -> ../../archive/groja.com/cert19.pem
lrwxrwxrwx 1 root root  35 May 13 03:20 /etc/letsencrypt/live/groja.com/chain.pem -> ../../archive/groja.com/chain19.pem
lrwxrwxrwx 1 root root  39 May 13 03:20 /etc/letsencrypt/live/groja.com/fullchain.pem -> ../../archive/groja.com/fullchain19.pem
lrwxrwxrwx 1 root root  37 May 13 03:20 /etc/letsencrypt/live/groja.com/privkey.pem -> ../../archive/groja.com/privkey19.pem
```

So we will need the `archive` directory.

Reference (4) also points out that the `renewal` directory has important config files:

```
$ l renewal/*.conf
-rw-r--r-- 1 root root 539 May 13 03:20 renewal/artsyvisions.com.conf
-rw-r--r-- 1 root root 504 May 13 03:20 renewal/groja.com.conf
-rw-r--r-- 1 root root 549 May 15 22:47 renewal/joomoowebsites.com.conf
-rw-r--r-- 1 root root 529 May 14 03:17 renewal/tomhartung.com.conf
-rw-r--r-- 1 root root 554 May 13 22:39 renewal/www.seeourminds.com.conf
-rw-r--r-- 1 root root 554 May 14 03:18 renewal/www.tomwhartung.com.conf
$
```

There is also a `renewal-hooks` directory that we will need to copy.

Reference (4) also points out that there is a crontab, but theirs is different from what I have.

```
$ cd /etc/letsencrypt
$ crontab -l
#
# Check the Let's Encrypt certificates for expiration every day at 3:15 AM.
#
15 3 * * * /usr/bin/certbot renew --quiet
$ crontab -l > crontab-ssl
$ pwd
/etc/letsencrypt
$ l
total 60
-rw-r--r--  1 root root    64 Jan 28  2019 .updated-options-ssl-apache-conf-digest.txt
drwx------  6 root root  4096 Jan 28  2019 accounts
drwx------ 10 root root  4096 May 28  2017 archive
-rw-r--r--  1 root root   121 Nov  7  2018 cli.ini
-rw-r--r--  1 root root   122 Jun 25 21:16 crontab-ssl
drwxr-xr-x  2 root root 12288 May 15 22:47 csr
drwx------  2 root root 12288 May 15 22:47 keys
drwx------ 10 root root  4096 May 28  2017 live
-rw-r--r--  1 root root  1619 Jan 28  2019 options-ssl-apache.conf
drwxr-xr-x  3 root root  4096 Jun 25 13:42 renewal
drwxr-xr-x  5 root root  4096 Oct 29  2017 renewal-hooks
$
```

We may want to recreate that on barbara.

Reference (4) also points out certbot has a cronjob that does the renewal:

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

**We are apparently doing both on ava, which may not be necessary.**

Reference (4) also points out we can test the renewal:

```
letsencrypt renew --dry-run
```

Reference (5) points out we need to install certbot packages:

On ava:

```
$ apt list certbot python3-certbot-apache
Listing... Done
certbot/xenial,xenial,now 0.31.0-1+ubuntu16.04.1+certbot+1 all [installed,automatic]
python3-certbot-apache/xenial,xenial,now 0.31.0-1+ubuntu16.04.1+certbot+1 all [installed]
$
```

On barbara:

```
$ apt list certbot python3-certbot-apache
Listing... Done
certbot/focal 0.40.0-1 all
python3-certbot-apache/focal 0.39.0-1 all
$
```

## Plan

If the plan doesn't work, we can always switch the server back to ava and "regroup."

**The sequence of these steps may need to be modified somewhat.**

- 1. Put all of the `/etc/letsencrypt` on ava into a tar file
- 2. Copy the tar file to barbara and unpack it
- 3. Install certbot packages
  - `apt list certbot python3-certbot-apache`
- 4. Enable mod_ssl on barbara
  - `a2enmod ssl`
- 5. Switch over the apache config files
  - 5.1. Disable the `0[124568]0-*` files in `/etc/apache2/sites-avalaible/`
    - `a2dissite ...`
  - 5.2. Enable the `0[124568]2-*` files in `/etc/apache2/sites-avalaible/`
    - `a2ensite ...`
  - 5.3. Enable the `0[124568]4-*` files in `/etc/apache2/sites-avalaible/`
    - `a2ensite ...`
- 6. Switch server to barbara
  - 6.1. Tail apache access and error log files
    - `tapa` and `tape` aliases
  - 6.2. Update tp-link router at `192.168.1.1`
    - Be sure to document changes made so we can un-do them if necessary
  - 6.3. Test sites in browser
    - Check https, which should work
    - Check http, which should redirect to https
- 7. Decide whether to keep barbara the server or fall back to ava and regroup
- 1.
- 1. Troubleshooting
- 1.
- 1. If necessary, create crontab on barbara, or check to see if certbot has one - **?????**
- 1.
- 1. More??
- 1.

## Notes and Commands

Ok, here we go!

