
# 6b-https-lets_encrypt-configuration.md

This file contains details on how to:

* Create Let's Encrypt certificates
* Configure apache to use the certificates

# Goal

Create the certificates and update the apache config files to implement
https support using Let's Encrypt option on ava for these two static sites:

* artsyvisions.com (static)
* tomh.info (static)

And these two python (wsgi) sites:

* groja.com (wsgi - flask)
* seeourminds.com (wsgi - django)

# Apache Config File Naming Standard

We follow this apache config file naming standard,
using `artsyvisions.com` , `groja.com` , `seeourminds.com` , and `tomh.info` as examples:
```
010-artsyvisions.com.conf
012-artsyvisions.com-redirect.conf
014-artsyvisions.com-le-ssl.conf
020-groja.com.conf
022-groja.com-redirect.conf
024-groja.com-le-ssl.conf
050-seeourminds.com.conf
052-seeourminds.com-redirect.conf
054-seeourminds.com-le-ssl.conf
070-tomh.info.conf
072-tomh.info-redirect.conf
074-tomh.info-le-ssl.conf
```
With the purpose and contents of each being as follows:

* `0?0-[domain_name].conf` - processes http requests on port 80
  * leave current files as-is
* `0?2-[domain_name]-redirect.conf` - redirects http on port 80 to https on port 443
  * For an example, see current the version of `050-seeourminds.com.conf` on jane
* `0?4-[domain_name]-ssl.conf` - configured to handle https/443/ssl requests
  * For an example, see current the version of `051-seeourminds.com-ssl.conf` on jane

# Background

For details on how we came up with this process,
see `../2016-jane/6b-analysis_of_requirements.md'
and `../2016-jane/6d-comparing_references-lets_encrypt.md' :

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6b-analysis_of_requirements.md
- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6d-comparing_references-lets_encrypt.md

For details on how we installed the required software, see the `6a-https-lets_encrypt-activation.md` file in this directory.

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-ava/6a-https-lets_encrypt-activation.md

# Process

**All commands must be run as root.**

## Step (1): Generate Certificates

The `certbot` command supports generating certificates for multiple sites.

This process focuses on generating a certificate and setting it up for use on:

* artsyvisions.com and www.artsyvisions.com on **ava**
* tomh.info and www.tomh.info on **ava**
* groja.com and www.groja.com on **ava**
* seeourminds.com and www.seeourminds.com on **ava**

It seems prudent to generate a separate certificate for each site.

### Step (1.1): Run `certbot`

When generating the first certificate, `certbot` asks several questions.
It "remembers" certain answers and does not ask these again, so it's important
to get them right.

- [ ] For **static** sites, run this command:
```
certbot --apache
```

- [ ] For **python (wsgi)** sites, run this command:
```
certbot --apache certonly
```

### Step (1.2): Generate First Certificate

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
one of the static or python (wsgi) site listed above (depending on which command we ran).

### Step (1.3): Python (Wsgi) Site Certificate

When we run `certbot` with the `certonly` , it will exit after creating the certificate.
- [ ] Fix any errors and re-run the `certbot` command

If there is difficulty understanding or fixing the error or errors, and we have not yet done a static site,
it helps to do one of those first

### Step (1.4): (Static) Site Configuration by `certbot`

If we run `certbot` **without** the `certonly` option, it does the following:
1. Create a new apache configuration file, based on the exiting file, to handle https requests on port 443
   - The name of this file is `[old_file_basename]-le-ssl.conf` (e.g., `070-tomh.info-le-ssl.conf`)
   - Run diff to see what we need to add to our configuration files when doing this manually (e.g., for python (wsgi) sites)
2. Optionally try to update the current configuration to redirect to the new configuration
   - Whether it does this second step depends on your answer to the question below
3. Run the `a2ensite` command(s) needed to activate the new configuration file(s)

As mentioned in the second task ("2." above), if we run `certbot` **without** the `certonly` option, it asks this question:
```
Please choose whether HTTPS access is required or optional.
-------------------------------------------------------------------------------
1: Easy - Allow both HTTP and HTTPS access to these sites
2: Secure - Make all requests redirect to secure HTTPS access
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```

Our goals are to:
* Have the http requests redirect to https
* Ensure our configuration files conform to our configuration file naming standard
  * Note that the names `certbot` uses for these files (e.g., `070-tomh.info-le-ssl.conf`) do not conform to our standard
Subsequent steps show how to achieve these goals regardless of the choice made here, so, whatevs....

### Step (1.5): Check for the Files

- [ ] Run these commands:
```
l /etc/letsencrypt/live/*
more /etc/letsencrypt/live/*/README
```
If the files are there, cool!  If not, look at the output of the commands to
see where they are, or fix any error(s) we got, as necessary.

### Step (1.6): Backup the Files

- [ ] Run these commands:
```
cd /etc
l letsencrypt/
tar -cvzf letsencrypt-ava-2017_05_24.tgz letsencrypt/
chown tomh:tomh letsencrypt-ava-2017_05_24.tgz
mv letsencrypt-ava-2017_05_24.tgz /usr/local/tar
ls -altr /usr/local/tar
```
I do not see any benefit in writ a script to do this at this time, because
these files should change only maybe once a year.
(Also they are quite easy to generate, assuming it will
let me do that again if need be.)

**Save a copy of this `.tgz` file on a thumb drive,
e.g., `/media/tomh/ext4Thumb/usr_local_tar/` on `barbara` .**

## Step (5): Update Apache Config

Now we need to tell apache to use the certificate files we generated.

**This process depends greatly on what choices were made above.**

### Step (5.1): Updating the Files

Follow the process detailed in Step 3 of `../2016-jane/6a-https-steps.md` :

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6a-https-steps.md

There is no sense duplicating that process here, at this time.

#### Process Overview:

1. Replace tabs with spaces in the `0?0-[domain_name].conf` file
2. Copy the `0?0-[domain_name].conf` file to `0?4-[domain_name]-ssl.conf`
3. Edit the `0?4-[domain_name]-ssl.conf` file

### Step (5.2) Test in Browser

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


As root:

```
a2ensite default-ssl.conf
service apache2 reload
```

### Step (4): Set up Redirection

Edit the `050-seeourminds.com.conf` config file to redirect to the new
`051-seeourminds.com-ssl.conf` file, by adding this line:

```
Redirect "/" "https://jane.seeourminds.com/"
```

Add it after the line that sets the `DocumentRoot`.

### Step (5): Dealing With Invalid Certificate Warnings

Spent a bit of time looking into how to:

1. Avoid the initial warning page
2. Trying to fix the red "Not Secure" warning that appears instead
of the green "Lock" icon I want to see.

This is a bit problematic because:

* Different browsers behave somewhat differently as well.
* We can always set up the apache config to use http on jane and https on ava and barbara
* To get the green icon, we need to get the certificate from let's encrypt (or the like)
* To use the let's encrypt option, the host needs to be accessible via DNS (and not just locally)
  * This last idea is ok on ava, and maybe on barbara, but not on jane

#### Chrome in particular looks bad

Here is one thing we tried that we may want to undo:

* Paste into Chrome: chrome://flags/#allow-insecure-localhost
* Reference: http://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate

Clicking on the red "Not secure" brings up some information, but
I could not see anything that would make it go away.

Going to Settings -> Advanced -> HTTPS shows a list of certificates, but I do
not see the one we created above.

Another place to look is in the Developer tools under Security, but again....

