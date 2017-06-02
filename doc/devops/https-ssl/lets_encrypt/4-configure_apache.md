
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

## Optional Preparation Step: Tab Removal

Optionally replace all tab characters with four (4) spaces.
```
vi *.conf
:%s&	&    &g
```

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

### Step (2-A.1) Rename and Enable the New ssl/https File

Disable the old file, rename the new file to conform to our naming standard, and enable it.

- [ ] The following commands show how to do this for the `artsyvisions.com` site:
```
a2dissite 010-artsyvisions.com-le-ssl.conf
mv 010-artsyvisions.com-le-ssl.conf 014-artsyvisions.com-le-ssl.conf
a2ensite 014-artsyvisions.com-le-ssl.conf
service apache2 reload
```

At this point our server handles both http and https requests without redirection.

To set up redirection (**highly recommended**), skip to Step (3).

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

To set up redirection (**highly recommended**), proceed with Step (3).


## Step (3): Setting up Http -> Https Redirection

The `certbot` command can generate the http-to-https redirection file for us.
I gave this a try, and decided that we should just geneate our own.

Note that the http-to-https redirection file that the `certbot` command
generates is a bit more flexible (and hence slightly more complicated, adding
three lines rather than just the one) than the one we create.
Specifically, it processes subdomains properly, while the one we create
effectively redirects **all** requests to the www.* subdomain.

**Hence, if at some point we decide to use subdomains, we will need to update
these files.**

### Step (3-A): Using Our Own Redirect Config

Do this step when `certbot`:

- [ ] Generates a new file for https/ssl (e.g., `070-tomh.info-le-ssl.conf`)
  * This corresponds to running `certbot` **without** the `certonly` option
- [ ] Does **not** update the existing config to redirect http requests to https
  * This corresponds to answering `1. Easy` to the Easy/Secure question
    (i.e., `Please choose whether HTTPS access is required or optional.`)

This is how we are doing our Static and LAMP CMS sites.

In this case, we need to:

* Rename the new file to conform to our naming standard
* Create a new file to redirect http requests to https
* Activate and test them


#### Create the New http->https Redirection File

Copy the existing http config file to the new name, and edit it to add the redirection.

- [ ] The following commands show how to do this for the `artsyvisions.com` site:
```
cp 010-artsyvisions.com.conf 012-artsyvisions.com-redirect.conf
vi 012-artsyvisions.com-redirect.conf
a2dissite 010-artsyvisions.com.conf
a2ensite 012-artsyvisions.com-redirect.conf
a2ensite 014-artsyvisions.com-le-ssl.conf   # (should already be enabled)
service apache2 reload
```

#### Add Redirection Config

- [ ] Add lines similar to the following, which show how to do this for the `groja.com` site:
```

###
### Redirect http requests to https
###
Redirect "/" "https://www.artsyvisions.com/"
```

Add it at the end, just before the line that closes the `VirtualHost` directive, i.e., just before this line:
```
</VirtualHost>
```

**Skip to Step (3) Test in Browser, below.**

### Step (2-B): Updating the Files Manually

Do this step when running `certbot` with the `certonly` option set.




#### Create and Edit New Redirection File for Http

Copy the existing http config file and edit the new file.

- [ ] The following commands show how to do this for the `groja.com` site:
```
cp 020-groja.com.conf 022-groja.com-redirect.conf
vi 022-groja.com-redirect.conf
```

#### Add Redirection Config

- [ ] Add lines similar to the following, which show how to do this for the `groja.com` site:
```

###
### Redirect http requests to https
###
Redirect "/" "https://www.groja.com/"
```

Add it at the end, just before the line that closes the `VirtualHost` directive, i.e., just before this line:
```
</VirtualHost>
```

#### Switch to Use Redirect and Https Config

Disable the old config file and enable the new ones.

- [ ] The following commands show how to do this for the `seeourminds.com` site:
```
a2dissite 050-seeourminds.com.conf
a2ensite 052-seeourminds.com-redirect.conf
a2ensite 054-seeourminds.com-le-ssl.conf
service apache2 reload
```

