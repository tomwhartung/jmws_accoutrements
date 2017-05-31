
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

## Step (2): Generate First Certificate

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

### Step (4): Generating Python (Wsgi) Site Certificates

When we run `certbot` with the `certonly` , it will exit after creating the certificate.
- [ ] Fix any errors and re-run the `certbot` command

If there is difficulty understanding or fixing the error or errors, and we have not yet done a static site,
it helps to do one of those first.

### Step (3): (Static) Site Configuration by `certbot`

If we run `certbot` **without** the `certonly` option, it does the following:
1. Create a new apache configuration file, based on the exiting file, to handle https requests on port 443
   - The name of this file is `[old_file_basename]-le-ssl.conf` (e.g., `070-tomh.info-le-ssl.conf`)
   - Run diff to see what we need to add to our configuration files when doing this manually (e.g., for python (wsgi) sites)
2. Optionally try to update the current configuration to redirect to the new configuration
   - Whether it does this second step depends on your answer to the question below (see Step (1.4.1) immediately below)
   - The bottom line is, it doesn't matter if we do it or certbot does it
3. Run the `a2ensite` command(s) needed to activate the new configuration file(s)

#### Step (1.4.1): (Static) Site Redirect Configuration

If we run `certbot` **without** the `certonly` option, it asks this question:
```
Please choose whether HTTPS access is required or optional.
-------------------------------------------------------------------------------
1: Easy - Allow both HTTP and HTTPS access to these sites
2: Secure - Make all requests redirect to secure HTTPS access
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```
Enter 1 here.  When we are ready, we will set up our own redirection.

### Step (1.5): (LAMP CMS) Site Configuration by `certbot`

As we did for the static sites, we run `certbot` **without** the `certonly`
option, and achieve the same results.

### Step (1.6): Check for the Certificates

- [ ] Run these commands:
```
l /etc/letsencrypt/live/*
more /etc/letsencrypt/live/*/README
```
If the files are there, cool!  If not, look at the output of the commands to
see where they are, or fix any error(s) we got, as necessary.

### Step (1.7): Backup the Certificates

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

## Step (2): Update Apache Config

Now we need to tell apache to use the certificate files we generated.

**Note that we keep all configuration files under version control (in RCS).**

This process depends on what choices were made in previous steps.

### Step (2-A): Using Our Own Redirect Config

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

#### Rename the New ssl/https File

Rename the new file to conform to our naming standard.

- [ ] The following commands show how to do this for the `artsyvisions.com` site:
```
a2dissite 010-artsyvisions.com-le-ssl.conf
mv 010-artsyvisions.com-le-ssl.conf 014-artsyvisions.com-le-ssl.conf
a2ensite 014-artsyvisions.com-le-ssl.conf
service apache2 reload
```

At this point our server handles both http and https requests without redirection.

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

This is how we are doiong our python (wsgi) sites.

In this case, we need to:

* Copy the `0?0-[domain_name].conf` file to `0?4-[domain_name]-ssl.conf`
* Edit the `0?4-[domain_name]-ssl.conf` file

#### Copy Existing File and Edit the New File

- [ ] The following commands show how to do this for the `groja.com` site:
```
cp 020-groja.com.conf 024-groja.com-le-ssl.conf
vi 024-groja.com-le-ssl.conf
```

#### Changing the Start of the File

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

#### Changes Near the End of the File

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

#### Adding the Let's Encrypt Configuration

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
###   https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6a-https-steps.md
###
SSLCertificateFile /etc/letsencrypt/live/groja.com/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/groja.com/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf

```
**All of these lines should be indented by **eight** (8) spaces!**

And yes please add a blank line before the comments and the new setting! Tyvm!!

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

## Step (3) Test in Browser

This is where it would be nice to be able to test this on a non-production host, but
we can implement Let's Encrypt only on hosts connected to the internet!

## Step (4): Check into RCS

When all config files are working, check them into RCS!
Quick before we mess something up!

- [ ] Run the following commands to ensure the latest versions are checked in to RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
ci -l *.conf
```

## Step (5): Automatic Renewal

**TODO: SET THIS UP**

## Step (6): Conclusion

Having three config files for each site, with names that follow the standard,
makes it super-easy to switch between http and https.

For details, see `6a-https-lets_encrypt-activation.md` in this directory.
- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-ava/6a-https-lets_encrypt-activation.md

### Testing

When it runs successfully, `certbot`'s output includes a message such as the following:
```
Congratulations! You have successfully enabled https://tomhartung.com and
https://www.tomhartung.com

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=tomhartung.com
https://www.ssllabs.com/ssltest/analyze.html?d=www.tomhartung.com
```

So we can test the sites with urls such as the following:

- https://www.ssllabs.com/ssltest/analyze.html?d=www.tomhartung.com

