
# 6a-https-lets_encrypt-activation

After having limited success using a self-signed certificate on jane,
we are going for setting up https using Let's Encrypt on ava.
Jumping straight to production!  I know!!

# Research

For details on how we came up with this process, see the `6*.md` files in
`../2016-jane` , specifically:

```
../2016-jane/6b-analysis_of_requirements.md
../2016-jane/6d-comparing_references-lets_encrypt.md
```

## "Reference-1"

The term "reference-1" refers to our #1 main reference:

- https://certbot.eff.org/#ubuntuxenial-apache

# Goal

Set up https using Let's Encrypt option on ava.

# Results

TBD.

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

- [ ] Add the certbot ppa and install the program (see reference 1):
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

- [ ] If we are setting up a new server, try to re-use the existing certificates.
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

## Step (6) Enable Configuration


## Step (7) Test in Browser

