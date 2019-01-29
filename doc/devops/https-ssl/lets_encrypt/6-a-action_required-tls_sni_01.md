
# 6-action_required-tls_sni_01.md

This file describes the process used in response to emails from
Let's Encrypt.

# The Emails

See these files in the current directory:

- `6-b-Action_required-2019_01_18.eml`
- `6-c-Action_required-2019_01_27.eml`

# References

The email `6-c-Action_required-2019_01_27.eml` has this link to a convenient how-to:

- https://community.letsencrypt.org/t/how-to-stop-using-tls-sni-01-with-certbot/83210

Previous emails had less-helpful links, that are worth mentioning nonetheless, should issues occur:

- Announcement:
  - https://community.letsencrypt.org/t/february-13-2019-end-of-life-for-all-tls-sni-01-validation-support/74209
- Forum:
  - https://community.letsencrypt.org/t/action-required-lets-encrypt-certificate-renewals/82834

# Process

Running this process on `barbara` and `ava` only.

[x] barbara
[x] ava

## 1. Upgrade certbot

First we follow the process on this page to upgrade certbot:

- https://certbot.eff.org/lets-encrypt/ubuntuxenial-apache

**I followed ONLY the Install process on this page.**

The process proceeded smoothly.

Commands run:

```
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository universe
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-apache
$ certbot --version
certbot 0.28.0
$
```

## 2. "Remove any explicit references to tls-sni-01"

The process calls for running this command:

```
sudo sh -c "sed -i.bak -e 's/^\(pref_challs.*\)tls-sni-01\(.*\)/\1http-01\2/g' /etc/letsencrypt/renewal/*; rm -f /etc/letsencrypt/renewal/*.bak"
```

However, looking at the `/etc/letsencrypt/renewal/*` files, I do not see
anything that looks like `"tls-sni-01"` , hmmm.

So I am running this command, and not removing the .bak files, to see if I am
missing something maybe, first on `barbara`, then on `ava`:

```
sh -c "sed -i.bak -e 's/^\(pref_challs.*\)tls-sni-01\(.*\)/\1http-01\2/g' /etc/letsencrypt/renewal/*"
```

Comparing the new files to their .bak versions

```
$ cd /etc/letsencrypt
$ sum renewal/*
```

The output from the `sum` command shows the files are indeed unchanged, hmmm.

## 3. "Do a full renewal dry run:"

The process calls for running this command:

```
sudo certbot renew --dry-run
```

### 3.1. Dry Run Results

The results indicate:

- Unable to do the dry run on `barbara` - because it is not live
  - The output shows however it is performing `http-01 challenge`s - which is good
- The renewal process is using `http-01` and not `tls-sni-01` - which is the goal
- We need to archive the files for tomh.info and jenniferj.info

### 3.2. Archiving config for obsolete sites

As root:

```
cd /etc/letsencrypt/renewal
mkdir RCS
ci -l *.conf
# "Lets Encrypt config file"
cd RCS/
mv tomh.info.conf,v tomh.info.conf,o
mv www.jenniferj.info.conf,v www.jenniferj.info.conf,o
l
cd ..
rm tomh.info.conf* www.jenniferj.info.conf*
rm -f *.bak
l
```

### 3.3. Dry Run Output

Following is the output from the dry run, showing it is using http-01 and not
tls-sni-01, which is  obsolete.

```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/joomoowebsites.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for joomoowebsites.com
http-01 challenge for www.joomoowebsites.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/joomoowebsites.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/groja.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for groja.com
http-01 challenge for www.groja.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/groja.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/www.tomwhartung.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for tomwhartung.com
http-01 challenge for www.tomwhartung.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/www.tomwhartung.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/tomhartung.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for tomhartung.com
http-01 challenge for www.tomhartung.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/tomhartung.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/artsyvisions.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for artsyvisions.com
http-01 challenge for www.artsyvisions.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/artsyvisions.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/www.seeourminds.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator apache, Installer apache
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for seeourminds.com
http-01 challenge for www.seeourminds.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of apache server; fullchain is
/etc/letsencrypt/live/www.seeourminds.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

