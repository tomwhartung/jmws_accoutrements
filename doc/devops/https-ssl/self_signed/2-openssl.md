
# self_signed - 2-openssl.md

These are the steps used to generate self signed certificates and use them to
get https going on [seeourminds.com](http://seeourminds.com) on the
development host `jane`.

# Moot at This Time

Having decided to **not** use self-signed certificates on `jane` or any other
hosts, **this information is irrelevant at this time.**

## Why?

For a look at why we decided to **not** use self-signed certificates,
see the file `../README.md`:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/README.md

# References

We found a lot of references to help with this process.
For a list of these, an analysis of each of them, and
details on what steps we got from which ones,
see the `1-comparing_references.md` file in this directory:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/self_signed/1-comparing_references.md

# Process

These are the steps we are following to get the Self-Signed SSL Certificate
configuration working on jane.

All commands must be run as root.

## Step (1): Installation and Setup

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

- [ ] Install `openssl` if needed
```
dpkg-query --list '*openssl*'
```

We have it so no worries.

## Step (2): Generate Certificates

It seems prudent to generate a separate certificate for each site.

This process shows how to generate two certificates and set them up for use on

* `seeourminds.com` on `jane`
* `groja.com` on `jane`

### Step (2.1): Commands to Run - seeourminds.com

All on one line!
```
l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*   # No such file or directory - just checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/seeourminds-selfsigned.key \
    -out /etc/ssl/certs/seeourminds-selfsigned.crt
l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*   # They are there now!
```

Following are the answers given to the prompts:

```
. . .
-----
Country Name (2 letter code) [AU]: US
State or Province Name (full name) [Some-State]: Colorado
Locality Name (eg, city) []: Denver
Organization Name (eg, company) [Internet Widgits Pty Ltd]: JooMoo WebSites LLC
Organizational Unit Name (eg, section) []: HQ
Common Name (e.g. server FQDN or YOUR name) []: jane.seeourminds.com
Email Address []: mark_as_spam@tomhartung.com
```

**One trick seems to be to enter the Fully Qualified Domain Name (FQDN) in
the `Common Name` field!**

We have tried `10.0.0.113` and `localhost` and those don't work, because
we have so many virtual hosts (so don't waste time trying those again).

### Step (2.2): Commands to Run - groja.com

All on one line!
```
l /etc/ssl/certs/groja* /etc/ssl/private/groja*   # No such file or directory - just checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/groja-selfsigned.key \
    -out /etc/ssl/certs/groja-selfsigned.crt
l /etc/ssl/certs/groja* /etc/ssl/private/groja*   # They are there now!
```

Gave it the same answers as those given above for seeourminds.com **EXCEPT** for:
```
the Common Name (e.g. server FQDN or YOUR name) []: jane.groja.com
```

**One trick seems to be to enter the Fully Qualified Domain Name (FQDN) in
the `Common Name` field!**

### Step (2.3): Check for the Files

As root:
```
$ l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
$ l /etc/ssl/*/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
$ l /etc/ssl/*/groj*
-rw-r--r-- 1 root root 1480 May 24 16:33 /etc/ssl/certs/groja-selfsigned.crt
-rw-r--r-- 1 root root 1704 May 24 16:33 /etc/ssl/private/groja-selfsigned.key
```

**NOTE: due to permissions, we can see the private only when logged in as root
(we are unable to see it using sudo!).**

## Step (3): Update the Apache Configuration

Now we need to tell apache to use the certificate files we generated.

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
  * For an example, see current the version of `052-seeourminds.com-redirect.conf` on jane
* `0?4-[domain_name]-ssl.conf` - configured to handle https/443/ssl requests
  * For an example, see current the version of `default-ssl.conf` on jane

**The plan is to do this for most sites, if not all of them.**

### Step (3.0): Replace Tabs in Original Config Files

- [ ] Replace all tab characters with **eight** (8) spaces.
```
vi 020-groja.com.conf
  :%s&	&        &g
  :wq
vi 050-seeourminds.com.conf
  :%s&	&        &g
  :wq
```

### Step (3.1): The New https Config Files

- [ ] Create New Files From Existing Files and check into RCS
```
cd /etc/apache2/sites-available
cp 020-groja.com.conf 024-groja.com-ssl.conf
ci -l 024-groja.com-ssl.conf
cp 050-seeourminds.com.conf 054-seeourminds.com-ssl.conf
ci -l 054-seeourminds.com-ssl.conf
```

### Step (3.2): Making the changes

- [ ] Edit the config files:
```
vi 024-groja.com-ssl.conf
vi 054-seeourminds.com-ssl.conf
```

Change the settings in the `0?4-[domain_name]-ssl.conf` files as described in
the subsequent sections.

Use the `/etc/apache2/sites-available/default-ssl.conf` file as a guide for
making these changes.

#### Step (3.2.1): Changes to the Start of the Files

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

#### Step (3.2.2): Changes Near the End of the File

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

#### Step (3.2.3): Turn on the SSLEngine

- [ ] Find this line near the end of the file:
```
#Include conf-available/serve-cgi-bin.conf
```
- [ ] And add these lines after it:
```

#   SSL Engine Switch:
#   Enable/Disable SSL for this virtual host.
SSLEngine on
```
**All of these lines should be indented by **eight** (8) spaces!**

And yes please add a blank line before the comments and the new setting! Tyvm!!

#### Step (3.2.4): Set `SSLCertificateFile` and `SSLCertificateKeyFile`

Add settings for the `SSLCertificateFile` and `SSLCertificateKeyFile` parameters.
Set them to point to the self-signed certificate files we generated previously.

- [ ] Add these lines after the `SSLEngine on` line just added:
```
#   A self-signed (snakeoil) certificate can be created by installing
#   the ssl-cert package. See
#   /usr/share/doc/apache2/README.Debian.gz for more info.
#   If both key and certificate are stored in the same file, only the
#   SSLCertificateFile directive is needed.
###
### Updating these values to point to the self-signed certificates we have now
### Reference:
###   https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6a-https-steps.md
###
### SSLCertificateFile	/etc/ssl/certs/ssl-cert-snakeoil.pem
### SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
SSLCertificateFile	/etc/ssl/certs/[domain_name]-selfsigned.crt
SSLCertificateKeyFile /etc/ssl/private/[domain_name]-selfsigned.key
```
Be sure to replace `[domain_name]` with `groja` (**no** `.com`) or
`seeourminds` (**without** `.com`) , and
indent the lines by **eight** (8) spaces, as appropriate.

Note that there are additional configuration parameters documented in
`/etc/apache2/sites-available/default-ssl.conf` that we may want to use at some point.

## Step (3.3): Set up Redirection

The `052-seeourminds.com-redirect.conf` config file currently redirects to the
new `054-seeourminds.com-ssl.conf` file.

- [ ] Create `022-groja.com-redirect.conf` and update it as appropriate
```
cp 052-seeourminds.com-redirect.conf 022-groja.com-redirect.conf
vi 022-groja.com-redirect.conf
```

## Step (4): Test the Apache Configuration

See if we made all those changes correctly!

### Step (4.1): Disable the old http config:

- [ ] Disable the current http config files
```
a2dissite 020-groja.com.conf
a2dissite 050-seeourminds.com.conf
```

### Step (4.2): Enable the new config files and restart apache:

- [ ] Enable the changes and restart
```
a2ensite 022-groja.com-redirect.conf
a2ensite 052-seeourminds.com-redirect.conf
a2ensite 024-groja.com-ssl.conf
a2ensite 054-seeourminds.com-ssl.conf
service apache2 reload
```
- [ ] Test in the browser
Depending on the browser, you may have to click through a warning page or two.
Don't worry about the red lock etc., we just need the page to load....

## Step (5): Dealing With Invalid Certificate Warnings

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

### Chrome in particular looks bad

Here is one thing we tried that we may want to undo:

* Paste into Chrome: chrome://flags/#allow-insecure-localhost
* Reference: http://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate

Clicking on the red "Not secure" brings up some information, but
I could not see anything that would make it go away.

Going to Settings -> Advanced -> HTTPS shows a list of certificates, but I do
not see the one we created above.

Another place to look is in the Developer tools under Security, but again....

