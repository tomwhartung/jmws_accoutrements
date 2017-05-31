
# 3-generate_certificates.md

This file contains details on how to:

* Create Let's Encrypt certificates for use on `ava` and `barbara`

# Goal

Create the certificates and update the apache config files to implement
https support using Let's Encrypt option on ava for:

These static sites:
* artsyvisions.com (static)
* tomh.info (static)

These python (wsgi) sites:
* groja.com (wsgi - flask)
* seeourminds.com (wsgi - django)

And these LAMP (php) sites:
* joomoowebsites.com (Joomla)
* tomhartung.com (Drupal)
* tomwhartung.com (WordPress)

# Background

## Apache Config File Naming Standard, Etc.

For details on how we came up with this process, and specifics about
the apache config file naming standard, see the `../README.md` file:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/README.md

## `certbot` Installation

For details on how to install the required software, see `2-certbot_installation.md` (in this directory).

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/lets_encrypt/2-certbot_installation.md

# Process

The `certbot` command supports generating certificates for multiple sites.

This process focuses on generating a certificate and setting it up for use on:

* Static sites:
  * artsyvisions.com and www.artsyvisions.com (on ava)
  * tomh.info and www.tomh.info (on ava)
* Python (Wsgi) sites:
  * groja.com and www.groja.com (on ava)
  * seeourminds.com and www.seeourminds.com (on ava)
* LAMP CMS sites:
  * joomoowebsites.com and www.joomoowebsites.com (on ava)
  * tomhartung.com and www.tomhartung.com (on ava)
  * tomwhartung.com and www.tomwhartung.com (on ava)

It seems prudent to generate a separate certificate for each site.

**All commands must be run as root.**

## Step (0): Ensure RCS Is Up-to-Date!

We keep all apache configuration files under version control in RCS.

- [ ] Run the following commands to ensure the latest versions are checked in to RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```

Check in any files that are out-of-sync in RCS.

**This is extremely important when running `certbot` without the `certonly` option,
because `certbot` updates the config files, and we will want to back out of those changes.**

## Step (1): Running `certbot` to Generate Certificates

- [ ] For **static** sites, run this command:
```
certbot --apache
```

- [ ] For **python (wsgi)** sites, run this command:
```
certbot --apache certonly
```

- [ ] For **LAMP CMS** sites, run this command:
```
certbot --apache
```

## Step (2): Generating the First Certificate

When generating the first certificate, `certbot` asks several questions.
It "remembers" certain answers and does not ask these again, so it's important
to get them right.

- [ ] Read the terms of service at:
  https://letsencrypt.org/documents/LE-SA-v1.1.1-August-1-2016.pdf
- [ ] Answer the questions (there are far fewer questions than there were for self-signed)
```
Enter email address (...) (Enter 'c' to cancel): lets_encrypt@tomhartung.com
(A)gree/(C)ancel: A
(Y)es/(N)o: Y
Which names would you like to activate HTTPS for?
```

- [ ] Select the numbers corresponding to the `*.com` and `www.*.com` names for
one of the static or python (wsgi) sites listed above (depending on which command was run).

## Step (3) Option (A): Not Specifying `certonly`

Pick this option when generating certificates for Static and LAMP CMS sites.

### Step (3.1): What it Does

If we run `certbot` **without** the `certonly` option, in
addition to generating the certificates, it does the following:

1. Creates a new apache configuration file, based on the exiting file, to handle https requests on port 443
   - The name of this file is `[old_file_basename]-le-ssl.conf` (e.g., `070-tomh.info-le-ssl.conf`)
2. Optionally tries to update the current configuration to redirect to the new configuration
   - Whether it does this second step depends on your answer to the question below (see Step (3.1) immediately below)
   - Because we have a file naming standard, it's easier to create our own redirection config file
3. Runs the `a2ensite` command(s) needed to activate the new configuration file(s)

This is fine for static and LAMP CMS sites, but note the following:
* We undo any changes `certbot` makes to theconfiguration files generated
* We rename any configuration files generated

These additional steps are necessary to support the file naming standard.

### Step (3.2): Site Redirect Configuration

When we run `certbot` **without** the `certonly` option, it asks this question:
```
Please choose whether HTTPS access is required or optional.
-------------------------------------------------------------------------------
1: Easy - Allow both HTTP and HTTPS access to these sites
2: Secure - Make all requests redirect to secure HTTPS access
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```
Enter 1 here.
Steps to set up our own redirection are in the next file, `4-configure_apache.md`.

### Step (3) Option (B): Using `certonly`

Pick this option when generating certificates for Python (Wsgi) sites.

When we run `certbot` **with** the `certonly` option set, it exits after creating the certificate.
- [ ] If necessary, fix any errors and re-run the `certbot` command

If there is difficulty understanding or fixing the error or errors, and we have not yet done a static site,
it helps to do one of those first.

### Step (4): Check for the Certificates

The certificates are really just special files.

- [ ] Run these commands:
```
l /etc/letsencrypt/live/*
more /etc/letsencrypt/live/*/README
```
If the files are there, great!

If the files are **not** there, look at the output of the commands to
see where they are, or fix any error(s) we got, as necessary.

### Step (5): Backup the Certificates

- [ ] Run these commands:
```
cd /etc
l letsencrypt/
tar -cvzf letsencrypt-ava-2017_05_28.tgz letsencrypt/
chown tomh:tomh letsencrypt-ava-2017_05_28.tgz
mv letsencrypt-ava-2017_05_28.tgz /usr/local/tar
ls -altr /usr/local/tar
```
I do not see any benefit in writing a script to do this at this time, because
these files should change only maybe once a year (when we renew them).
Also they are quite easy to generate - assuming it will
let me do that again if need be.

**Save a copy of this `.tgz` file on a thumb drive,
e.g., `/media/tomh/ext4Thumb/usr_local_tar/` on `barbara` .**

## Step (6): Update Apache Config

For steps on how to update the apache configuation, see the next file `4-configure_apache.md` (in this directory).

