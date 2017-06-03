
# 4-configure_apache.md

This file contains details on how to:

* Configure apache to use the Let's Encrypt certificates

# Goal

Update the apache config files to implement
https support using Let's Encrypt option on ava for:

These Static sites:
* artsyvisions.com (Static)
* tomh.info (Static)

These Python (Wsgi) sites:
* groja.com (Flask)
* seeourminds.com (Django)

And these LAMP CMS (php) sites:
* joomoowebsites.com (Joomla)
* tomhartung.com (Drupal)
* tomwhartung.com (WordPress)

# Background

## Apache Config File Naming Standard, Etc.

For details on how we came up with this process, and specifics about
the apache config file naming standard, see the `../README.md` file:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/README.md

## Installation and Certificate Generation

For details on how to install the required software, see `2-certbot_installation.md` (in this directory).

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/lets_encrypt/2-certbot_installation.md

For details on how to generate the required certificates from Let's Encrypt, see `3-generate_certificates.md` (in this directory).

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/lets_encrypt/3-generate_certificates.md

# Process

**All commands must be run as root.**

## Do Only One Site at a Time

**Perform this process for only one site at a time, to allow for quickly testing
it, and possibly backing out of the changes, before moving on to other sites.**

## Optional Preparation Step: Tab Removal

Optionally replace all tab characters with four (4) spaces.
```
vi *.conf
:%s&	&    &g
```
We will be copying these files so now is the perfect time to do this and clean
up any stale comments, etc.

## Step (0): Ensure RCS Is Up-to-Date!

We keep all apache configuration files under version control in RCS.

- [ ] Run the following commands to ensure the latest versions are checked in to RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```
Check in any files that are out-of-sync in RCS.

**This is extremely important because we will be editing these files momentarily.**

## Step (1): Update Apache Config Overview

Now we need to tell apache to use the certificate files we generated.
This entails:

* Renaming a generated file or creating a new config file for processing https requests
* Creating a new config file for redirecting http requests to https

The specific steps to be used in this process depend on what options were
picked when the certificates were generated.

## Step (2): Configuration to Process Https Requests

Use **Step (2) Option (A): Using the Generated Https Config File** when:

* The `certbot` command was run (i.e., **without** the `certonly` option)
* This is the process we use for the Static and LAMP CMS Sites

Use **Step (2) Option (B): Creating a New Config File for Https** when:

* The `certbot certonly` command was run (i.e., **with** the `certonly` option)
* This is the process we use for the Python (Wsgi) Sites

## Step (2) Option (A): Using the Generated Https Config File

This is how we are processing our Static and LAMP CMS sites.

In this case, we need to rename the new file to conform to our naming standard.

### Step (2-A.1) Fix Indentation

The `certbot` command does not indent the directives it adds to the config file,
so it is advisable to do that manually before proceeding any further.

### Step (2-A.2) Rename and Enable the New ssl/https File

Disable the old file, rename the new file to conform to our naming standard, and enable it.

- [ ] The following commands show how to do this for the `artsyvisions.com` site:
```
a2dissite 010-artsyvisions.com-le-ssl.conf
mv 010-artsyvisions.com-le-ssl.conf 014-artsyvisions.com-le-ssl.conf
a2ensite 014-artsyvisions.com-le-ssl.conf
service apache2 reload
```
At this point the site **is capable of handling** both http and https
requests (without redirection), but it will **not successfully handle** the
https requests until we reload the server.

To reload apache and smoke test using https on the site, proceed with Step (3).

## Step (2) Option (B): Creating a New Config File for Https

This is how we are processing our Python (Wsgi) sites.

In this case, we need to:

* Copy the `0?0-[domain_name].conf` file to `0?4-[domain_name]-ssl.conf`
* Edit the `0?4-[domain_name]-ssl.conf` file

### Step (2-B.1) Copy the Existing File and Edit the New File

- [ ] The following commands show how to do this for the `groja.com` site:
```
cp 020-groja.com.conf 024-groja.com-le-ssl.conf
vi 024-groja.com-le-ssl.conf
```

### Step (2-B.2) Changing the Start of the File

- [ ] Replace this line at beginning of the file:
```
<VirtualHost *:80>
```
- [ ] With these lines:
```
<IfModule mod_ssl.c>
    ### <VirtualHost *:80>
    <VirtualHost _default_:443>
```
Note that we are indenting these lines by **four** (4) spaces.

### Step (2-B.3) Changes Near the End of the File

- [ ] Replace this line near the end of the file:
```
</VirtualHost>
```
- [ ] With these lines:
```
    </VirtualHost>
</IfModule>
```
Note that in addition to adding a line, we indented the `</VirtualHost>`
line by **four** (4) spaces.

### Step (2-B.4) Adding the Let's Encrypt Configuration

Add the Let's Encrypt configuration to the new apache config file.

- [ ] Find this line near the end of the file:
```
#Include conf-available/serve-cgi-bin.conf
```
- [ ] Add lines similar to the following, which show how to do this for the `groja.com` site:
```

###
### Adding config to use the Lets Encrypt certificates
### Reference:
###   https://github.com/tomwhartung/jmws_accoutrements/tree/master/doc/devops/https-ssl/lets_encrypt
###
SSLCertificateFile /etc/letsencrypt/live/groja.com/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/groja.com/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf

```
**All of these lines should be indented by **eight** (8) spaces!**

And yes please add a blank line before the comments and the new setting! Tyvm!!

### Step (2-B.5) Enabling the New Configuration File

Enable the new config file.

- [ ] The following command shows how to do this for the `seeourminds.com` site:
```
a2ensite 054-seeourminds.com-le-ssl.conf
```
At this point the site **is capable of handling** both http and https
requests (without redirection), but it will **not successfully handle** the
https requests until we reload the server.

## Step (3): Reload Apache and Smoke Test

### Step (3.1): Reload Apache and Smoke Test

- [ ] Use the following command to reload apache to make the new config file live:
```
service apache2 reload
```
At this point our server should be able to process both http and https
requests (without redirection).

### Step (3.2): Smoke Test the Site

- [ ] Ensure the http configuration still works by accessing the home page (e.g., groja.com) in the browser.
- http://groja.com

- [ ] Smoke test the https configuration by accessing the home page (e.g., groja.com) in the browser.
- https://groja.com

**If the green icon does not appear, open the developer tools window and fix the issue(s).**

## Step (4): Setting up Http -> Https Redirection

Setting up http-to-https redirection is optional, but recommended.
We are doing this for all sites.

**Do not set up redirection until the site shows the green icon for all pages.**

In this case, we need to:

* Create a new file to redirect http requests to https
* De-activate the old, activate the new, and test them

### The `certbot` Alternative

The `certbot` command can update the existing http config file to implement
http-to-https redirection file for us.

I gave this a try, and decided that we should just generate our own.

Note that the http-to-https redirection file that the `certbot` command
generates is a bit more flexible (and hence slightly more complicated, adding
three lines rather than just the one) than the one we create.
Specifically, it processes subdomains properly, while the one we create
effectively redirects **all** requests to the www.* subdomain.

Hence, if at some point we decide to use subdomains, we may need to update
these redirection files.

### Step (4.1): Creating the Redirect Config File

Copy the existing http config file to the new name, and edit it to add the redirection.

- [ ] The following commands show how to do this for the `tomwhartung.com` site:
```
cp 080-tomwhartung.com.conf 082-tomwhartung.com-redirect.conf
vi 082-tomwhartung.com-redirect.conf
```

### Step (4.2) Special Instructions for Python Sites

- [ ] Comment out all WSGI* directives in python config files, as in the following example for the `seeourminds.com` site:
```
###     #
###     # These two lines cause it to run in daemon mode.  I am not seeing a huge benefit but think it's the way to go.
###     # For more comments and a link, see the file 150-wsgi.test.conf in this directory.
###     #
###     WSGIDaemonProcess seeourminds.com processes=2 threads=15 python-path=/var/www/seeourminds.com/htdocs/seeourminds.com/Site
###     WSGIProcessGroup seeourminds.com
###
###     #
###     # This is the key to the whole thing:
###     #
###     WSGIScriptAlias / /var/www/seeourminds.com/htdocs/seeourminds.com/Site/Site/wsgi.py
###     ## WSGIPythonPath /var/www/seeourminds.com/htdocs/seeourminds.com/Site
```
As you can see, I like to make it obvious that these lines are commented out.

**Forgetting this step causes an error when this and the https file are enabled when apache is reloaded.**

### Step (4.3) Add Redirection Config

- [ ] Add lines similar to the following, which show how to do this for the `tomwhartung.com` site:
```

###
### Redirect http requests to https
###
Redirect "/" "https://www.tomwhartung.com/"
```

Add it at the end, just before the line that closes the `VirtualHost` directive, i.e., just before this line:
```
</VirtualHost>
```

### Step (4.4) Switch to Use Redirect and Https Config

Disable the old `0?0-*` config file and enable the new `0?2-*` and `0?4-*` files.

- [ ] The following commands show how to do this for the `seeourminds.com` site:
```
a2dissite 050-seeourminds.com.conf
a2ensite 052-seeourminds.com-redirect.conf
a2ensite 054-seeourminds.com-le-ssl.conf
service apache2 reload
```
**Enable and activate the new configuration for only one site at a time, to
allow for quickly testing it, and backing out of the changes if necessary.**

## Step (5): Test Thoroughly and Finish Up

**It is best to test the configuration thoroughly for each site as soon as
its new configuration files are enabled and apache is reloaded.**

See the next file `5-test_and_finish_up.md` (in this directory).

