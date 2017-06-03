
# 6-https-lets_encrypt

# Recap

We spent quite a bit of time with this, learning a lot, setting things
up for flexibility, consistency and ease of use in the long term, and
documenting the entire process ad nauseum.

# Reference

For details on the why and how of creating certificates and configuring apache,
see the `doc/devops/https-ssl` directory in this repository.

# Purpose of This File

The process below describes how to install the necessary software needed to
set up https using `certbot` and Let's Encrypt on `barbara`.

It relies on having the certificates and apache configuration files already
created as detailed in the reference mentioned above and currently existing on `barbara` .

# Process

**All commands must be run as root.**

## Step (1): Installation

- [ ] Ensure everything is up-to-date:
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

## Step (2): Copy Certificates

Note that we want to have a separate certificate for each site.

- [ ] If we are setting up a new server, re-use the existing certificates.
- [ ] If we are setting up a new site, see the Reference mentioned above for details on how to generate new certificates, etc.:
  - https://github.com/tomwhartung/jmws_accoutrements/tree/master/doc/devops/https-ssl/lets_encrypt

## Step (3): Update Apache Config

Note that there is an apache config file naming standard, and
each site has four config files.

- [ ] If we are setting up a new server, re-use the existing config files.
- [ ] If we are setting up a new site, see the Reference mentioned above for details on how to create new config files, etc.:
  - https://github.com/tomwhartung/jmws_accoutrements/tree/master/doc/devops/https-ssl/lets_encrypt

## Step (4) Enable Configuration

Having four config files for each site, with names that follow the standard,
makes it super-easy to switch between http and https.

Again, the Reference mentioned above has details on all of this!
For information about this piece of the puzzle specifically, see the README.md file:
- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/README.md

## Step (5) Test in Browser

Testing the ssl configuration on `barbara` requires being able to access
the sites using urls of the form https://www.* .

- [ ] Make `hosts-www_is_barbara` the active `/etc/hosts` file:
```
cd /etc
ls -al hosts*
rm -f hosts
ln -s hosts-www_is_barbara hosts
ls -al hosts*
```
This enables using **https://www.* urls** to access the sites on `barbara` .

