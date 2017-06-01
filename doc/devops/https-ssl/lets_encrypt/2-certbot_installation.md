
# 2-certbot_installation.md

This file describes the process used to set up https using certificates from
Let's Encrypt on `ava` and `barbara`.

Jumping straight to production!  I know!!  We have no other choice!

# Research

For details on how we came up with this process, see the following files:

- `../README.md` ( https://github.com/tomwhartung/jmws_accoutrements/tree/master/doc/devops/https-ssl )
- `1-comparing_references.md` (in this directory)

The best reference is:

- https://certbot.eff.org/#ubuntuxenial-apache

# Goal

Define the process for setting up https using Let's Encrypt option on `ava` and `barbara`.

# Results

Got it to work OK!  Certbot is cool!

# Process

These are the steps we are following:

**All commands must be run as root.**

## Step (0) Optional Preparation Step: Tab Removal

Optionally replace all tab characters with four (4) spaces.
```
vi *.conf
:%s&	&    &g
:wq
```

## Step (1): Check apache conf files

- [ ] Ensure the current versions of all apache conf files are checked into RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```
- [ ] Check in any files that are not already checked in.

## Step (2): Enable Ssl

- [ ] Ensure ssl is installed and enabled.
```
apache2ctl -M | grep ssl
```

- [ ] If the module is not already enabled, enable it and restart apache:
```
a2enmod ssl
apache2ctl -M | grep ssl
service apache2 restart
```

## Step (3): Installation

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

## Step (4): Configure Modems and Routers

Modems and routers must be configured to accept https requests on port 443 and
pass them through to the appropriate host(s).

Specific steps for this process are beyond the scope of this document.

## Next Steps: Generation and Configuration

The next steps are to generate the certificates and configure apache to use them.

For information on how to generate the certificates, see `3-generate_certificates.md` (in this directory).

For information on how to Configure apache, see `4-configure_apache.md` (in this directory).


