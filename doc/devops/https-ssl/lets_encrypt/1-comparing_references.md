
# 1-comparing_references.md

This file compares the references we have found for using a certificate from
Let's Encrypt to set up ssl on apache.

# Goal

We can set up Let's Encrypt only on a live server, so ideally I want to
find and use a process that is referenced on multiple sites.

## Requirements of the Process

We need to be able to:

1. Run through the process relatively quickly
2. Be able to quickly find solutions when there's a problem
3. Be able to back out of changes if there's a serious problem
4. Keep track of what we did right for one site so we can quickly do it again for others

# Results

Using Certbot is definitely the best choice.

## About Certbot

From the Certbot github page:

> Certbot, previously the Let's Encrypt Client,
> is EFF's tool to obtain certs from Let's Encrypt, and
> (optionally) auto-enable HTTPS on your server

## Best Reference (Process)

- https://certbot.eff.org/#ubuntuxenial-apache

For additional references, processes, and details learned from looking at the
entire list of sites, see below.

# List of References

These references for setting up the Let's encrypt configuration
are listed in more-or-less the same order as they appeared in my google search results.

- (1) https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
  - Dated 4/21/2016
- (2) https://www.howtoforge.com/tutorial/install-apache-with-php-and-mysql-on-ubuntu-16-04-lamp/#-enable-the-ssl-website-in-apache
  - Dated 3/29/2017
- (3) https://www.vultr.com/docs/setup-lets-encrypt-with-apache-on-ubuntu-16-04
  - Dated 8/24/2016
- (4) https://certbot.eff.org/all-instructions/#ubuntu-16-04-xenial-apache
- (5) http://dev-notes.eu/2017/02/letsencrypt-ubuntu-xenial/
  - Dated 2/25/2017
- (6) https://community.letsencrypt.org/t/help-with-ubuntu-16-04-apache-and-letsencrypt-set-up/17889
  - Dated July, 2016
- (7) https://certbot.eff.org/#ubuntuxenial-apache
- (8) https://certbot.eff.org/
- (9) https://github.com/certbot/certbot
- (10) https://help.ubuntu.com/lts/serverguide/httpd.html#https-configuration

# Best References (Processes)

Following are the results of the comparison.
For more details, see the next section, Comparing the References.

## (1) certbot/certbot -> eff.org/#ubuntuxenial-apache

Following is a link the best process we've found for generating a Let's Encrypt certificate:

- https://certbot.eff.org/#ubuntuxenial-apache

**Ensure the current versions of all apache config files are checked into RCS before running these commands!**

It looks simple enough but we will definitely want to check the apache config file before going live with it.

## (2) digitalocean.com

The digitalocean.com reference breaks things down a bit.

- https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04

It offers commands to do some things more manually and perhaps some additional steps.

**Moreover, check this reference to verify we are done when we think we're done.**

## (3) dev-notes.eu

The dev-notes.eu reference also breaks things down a bit:

- http://dev-notes.eu/2017/02/letsencrypt-ubuntu-xenial/

Consider looking at it if we run into a snag of some sort.

# Comparing the References

## (1) digitalocean.com

- https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
  - Uses `certbot` (and digitalocean.com has cred points for being the best reference for the self-signed option)
  - The digitalocean.com reference was the best one for Configuration (1).

## (2) howtoforge.com

- https://www.howtoforge.com/tutorial/install-apache-with-php-and-mysql-on-ubuntu-16-04-lamp/#-enable-the-ssl-website-in-apache
  - Uses `python-letsencrypt-apache`

## (3) vultr.com

- https://www.vultr.com/docs/setup-lets-encrypt-with-apache-on-ubuntu-16-04
  - Uses letsencrypt repo on github (https://github.com/letsencrypt/letsencrypt)
  - (Other references add a ppa so we get updates via apt-get .)
  - Accessing this repo redirects to certbot repo (https://github.com/certbot/certbot)

## (4) certbot.eff.org - 1

- https://certbot.eff.org/all-instructions/#ubuntu-16-04-xenial-apache
  - EFF certbot page

## (5) dev-notes.eu

- http://dev-notes.eu/2017/02/letsencrypt-ubuntu-xenial/
  - Also references certbot

## (6) community.letsencrypt.org

- https://community.letsencrypt.org/t/help-with-ubuntu-16-04-apache-and-letsencrypt-set-up/17889
  - Forum post in which an expert walks a complete novice through the process

## (7) certbot.eff.org - 2

- https://certbot.eff.org/#ubuntuxenial-apache
  - Another EFF certbot page, NOTE: contains two "tabs," Automated and Advanced

## (8) certbot.eff.org - 3

- https://certbot.eff.org/
  - Interactive guide found via the certbot/certbot/README.rst file on github.
  - Filling in the form (2 dropdown lists) takes us to the (7) certbot.eff.org - 2 reference

## (9) https://github.com/certbot/certbot

- https://github.com/certbot/certbot
  - Excellent!

## (10) help.ubuntu.com

- https://help.ubuntu.com/lts/serverguide/httpd.html#https-configuration
  - So minimal that it's worthless

