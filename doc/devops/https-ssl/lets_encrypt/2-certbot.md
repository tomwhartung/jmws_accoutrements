
# 2-certbot.md

we are going for setting up https using Let's Encrypt on ava.

Jumping straight to production!  I know!!

# Research

For details on how we came up with this process, see the following files:

- `../README.md` ( https://github.com/tomwhartung/jmws_accoutrements/tree/master/doc/devops/https-ssl )
- `1-comparing_references.md` (in this directory)

The best reference is:

- https://certbot.eff.org/#ubuntuxenial-apache

# Goal

Set up https using Let's Encrypt option on `ava` and `barbara`.

# Results

Got it to work OK!  Certbot is cool!

# Process

These are the steps we are following:

**All commands must be run as root.**

## Step (1): Check apache conf files

- [ ] Ensure the current versions of all apache conf files are checked into RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```
- [ ] Check in any files that are not already checked in.

-> FYI: noticing that the ssl module is not enabled (yet).

## Step (2): Installation

- [ ] Ensure everything else is up-to-date
```
apt-get update
apt-get upgrade
```

- [ ] Add the certbot ppa and install the program (see https://certbot.eff.org/#ubuntuxenial-apache ):
```
apt-get install software-properties-common
apt autoremove     # suggested by output of previous command
add-apt-repository ppa:certbot/certbot
apt-get update
apt-get install python-certbot-apache
```

## Step (3): Configure Modems and Routers

Modems and routers must be configured to accept https requests on port 443 and
pass them through to the appropriate host(s).

Specific steps for this process are beyond the scope of this document.

## Step (4): Generate Certificates

Note that we want to have a separate certificate for each site.

- [ ] If we are setting up a new server, copy and re-use the existing certificates.
- [ ] If we are setting up a new site, see the details in `6b-https-lets_encrypt-configuration.md` in this directory:
  - https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-ava/6b-https-lets_encrypt-configuration.md

## Step (5): Update Apache Config

### Apache Config File Naming Standard

We follow this apache config file naming standard,
using `groja.com` and `seeourminds.com` as examples:
```
020-groja.com.conf
022-groja.com-redirect.conf
024-groja.com-ssl.conf
050-seeourminds.com.conf
052-seeourminds.com-redirect.conf
054-seeourminds.com-ssl.conf
```

With the purpose and contents of each being as follows:

* `0?0-[domain_name].conf` - processes http requests on port 80
  * leave current files as-is
* `0?2-[domain_name]-redirect.conf` - redirects http on port 80 to https on port 443
  * For an example, see current the version of `050-seeourminds.com.conf` on jane
* `0?4-[domain_name]-ssl.conf` - configured to handle https/443/ssl requests
  * For an example, see current the version of `051-seeourminds.com-ssl.conf` on jane

### For Details

- [ ] If we are setting up a new server, try to re-use the existing config files.
- [ ] If we are setting up a new site, see the details in `6b-https-lets_encrypt-configuration.md` in this directory:
  - https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-ava/6b-https-lets_encrypt-configuration.md

## Step (6) Enable Configuration and Test in Browser

Having three config files for each site, with names that follow the standard, makes it super-easy to switch between http and https.

### Step (6.1): Falling Back to Http Only

Note that if something goes wrong with ssl on this site, we can quickly switch it back to
process only http requests with commands such as the following:
```
a2dissite 072-tomh.info-redirect.conf
a2dissite 074-tomh.info-le-ssl.conf
a2ensite 070-tomh.info.conf
service apache2 reload
```

**TODO: Try redirecting https to http, instead of leaving https requests with an error.**

### Step (6.2): Switching Back to Https and Redirection

Once we have ssl working again on the site, we can quickly switch it back to
process https requests and redirect http to https with commands such as the following:
```
a2dissite 050-seeourminds.com.conf
a2ensite 052-seeourminds.com-redirect.conf
a2ensite 054-seeourminds.com-le-ssl.conf
service apache2 reload
```

### Step (6.3) Test in Browser

See how that works for ya!

