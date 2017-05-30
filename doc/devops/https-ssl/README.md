
# https-ssl/README.md

This file and the other files it refers to describe how to implement https using
apache on port 443 so we can serve pages using ssl.

# Http on `jane`, Https on `barbara` and `ava`

We are using http (i.e., port 80 without ssl) on `jane`, and
using Let's Encrypt certificates on `barbara` and `ava`

There is much more on this topic further down in this file.

# Apache Config File Naming Standard

Each site has four configuration files, but uses only two on any given host.

## File Name Formula

The pattern used for each file name, along with thepurpose and contents of
each file is as follows:

* `0?0-[domain_name].conf` - processes http requests on port 80
  * For `jane` - old versions that we have been using for years
* `0?2-[domain_name]-redirect.conf` - redirects http on port 80 to https on port 443
  * For `barbara` and `ava` - old versions configured to redirect to https
* `0?4-[domain_name]-le-ssl.conf` - configured to handle https/443/ssl requests
  * For `barbara` and `ava` - old versions updated to use the Let's Encrypt certificates
* `0?6-[domain_name]-le-ssl-redirect.conf` - redirects https requests on port 443 to http
  * For `jane` - must click through errors the first time, can get to page but there's no green icon

## File Name Examples

We follow this apache config file naming standard,
using `artsyvisions.com` , `groja.com` , `seeourminds.com` , and `tomh.info` as examples:
```
010-artsyvisions.com.conf
012-artsyvisions.com-redirect.conf
014-artsyvisions.com-le-ssl.conf
016-artsyvisions.com-le-ssl-redirect.conf
020-groja.com.conf
022-groja.com-redirect.conf
024-groja.com-le-ssl.conf
026-groja.com-le-ssl-redirect.conf
050-seeourminds.com.conf
052-seeourminds.com-redirect.conf
054-seeourminds.com-le-ssl.conf
056-seeourminds.com-le-ssl-redirect.conf
070-tomh.info.conf
072-tomh.info-redirect.conf
074-tomh.info-le-ssl.conf
076-tomh.info-le-ssl-redirect.conf
```

## Enabling and Disabling Configuration Files

It can be best to run `a2dissite` first, then run `a2ensite` , because
apache gives an error if we have two active configuration files
referring to code for the same site.

This file naming standard makes it easy to:

* Quickly enable and disable http or https for one or more sites
* Use file name completion to save a ton of typing

**These commands must be run as root, directly or via sudo.**

### Disabling http and Enabling https

**Run commands such as these on `barbara` or `ava` only.**

To disable http and enable https for a single site (tomhartung.com):

```
a2dissite 060-tomhartung.com.conf 066-tomhartung.com-le-ssl-redirect.conf
a2ensite 062-tomhartung.com-redirect.conf 064-tomhartung.com-le-ssl.conf
service apache2 reload
```

### Disabling https and Enabling http

**Run commands such as these on `jane` only.**

To disable https and enable http for a single site ():

```
a2dissite 042-joomoowebsites.com-redirect.conf 044-joomoowebsites.com-le-ssl.conf
a2ensite 040-joomoowebsites.com.conf 046-joomoowebsites.com-le-ssl-redirect.conf
service apache2 reload
```

# Self-Signed vs. Let's Encrypt

## Self-Signed on `jane` - Unused

We implemented self-signed certificates on the development host (jane), but
it turns out that they do not work well, so we reverted back to using http.

## Let's Encrypt on `barbara` and `ava`

We can use the Let's Encrypt certificates on both `barbara` and `ava` with
the following restrictions:

* We must access these sites using one of the following urls (using tomh.info as an example):
  * https://www.groja.com
  * http://www.groja.com - redirects to https://www.groja.com
  * https://groja.com - redirects to https://www.groja.com
  * http://groja.com - redirects to https://www.groja.com
* To access the sites on the backup host (`barbara`) we must either:
  * Change the router configuration to send outside requests to `barbara` rather than `ava`, or
  * Change the /etc/hosts file to send local requests to `barbara` rather than `ava`

# The Difficulties

Or, why we are using http on jane, and https on barbara and ava.

## Self-Signed

I thought the Self-Signed certs would be good for use on the local host.

* This works, but we get an ugly red "Not secure" icon instead of the green lock that we want.
* There's really very little advantage to this, that I can see.

## Let's Encrypt

We are unable to follow the normal development -> backup -> production workflow
because the host must be accessible from the internet for
Let's Encrypt to verify the certificates it creates.

# Lessons Learned

## Redirecting

* Browsers will handle redirecting requests from Http -> Https without complaint
* Browsers object to redirecting requests from Https -> Http, and block access to the site
* Once you confirm the redirection from Https -> Http for the site with the browser, it remembers that

## Using the Self-Signed option on `jane`

This allows access to the site, but the browser does not display the green icon,
so there is little advantage to doing this.

