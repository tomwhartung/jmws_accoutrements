
# 6a-https-steps

It's time to get https going on [seeourminds.com](http://seeourminds.com),
and probably all of the other CMS sites.

## Options

Note that there are two options:

1) Self-Signed
2) Let's Encrypt

## Goals

These are the initial goals we were trying to acheive:

1) Set up the Self-Signed option on jane.

2) Set up the Let's Encrypt option on barbara and ava.

3) We would prefer to use the Let's Encrypt option on jane, but
if that is a hassle or not feasible for some reason,
we may want to go with Self-Signed, or maybe even just http.

## Results

For a thorough analysis of the motivations, goals, and results of this effort,
see the file `6b-analysis_of_requirements.md` in this directory.

## References

We found a lot of references to help with this process.
For a list of these, an analysis of each of them, and
details on what steps we got from which ones,
see the `6c-comparing_references-self_signed.md` file in this directory:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6a-https-comparing_references.md

## Process

These are the steps we are following to get the Self-Signed SSL Certificate
configuration working on jane.

All commands must be run as root.

### Step (1): Installation and Setup

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

### Step (2): Generate Certificate

It seems prudent to generate a separate certificate for each site.

This process shows how to generate two certificates and set them up for use on

* `seeourminds.com` on `jane`
* `groja.com` on `jane`

#### Step (2.1): Commands to Run - seeourminds.com

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

#### Step (2.2): Commands to Run - groja.com

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

#### Step (2.3): Check for the Files

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

### Step (3): Apache Configuration

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
  * For an example, see current the version of `050-seeourminds.com.conf` on jane
* `0?4-[domain_name]-ssl.conf` - configured to handle https/443/ssl requests
  * For an example, see current the version of `051-seeourminds.com-ssl.conf` on jane

**The plan is to do this for most sites, if not all of them.**

#### Step (3.1): The New https Config Files

- [ ] Create New Files From Existing Files
```
cd /etc/apache2/sites-available
cp 020-groja.com.conf 024-groja.com-ssl.conf
ci -l 024-groja.com-ssl.conf
cp 050-seeourminds.com.conf 054-seeourminds.com-ssl.conf
ci -l 054-seeourminds.com-ssl.conf
```

#### Step (3.2): Making the changes

- [ ] Edit the config files:
```
vi 024-groja.com-ssl.conf
vi 054-seeourminds.com-ssl.conf
```

Use the `/etc/apache2/sites-available/default-ssl.conf` file as a guide for
making these changes.

- [ ] Change the settings as follows:
  - [ ] Ensure `SSLEngine on` is set
  - [ ] Update the values for `SSLCertificateFile` and `SSLCertificateKeyFile`

Set `SSLCertificateFile` and `SSLCertificateKeyFile` to
point to the files we generated in the previous step.

#### Step (3.3): Enable the config and restart apache:

- [ ] Enable the changes and restart
```
a2ensite 024-groja.com-ssl.conf
a2ensite 054-seeourminds.com-ssl.conf
service apache2 reload
```
- [ ] Test in the browser
Don't worry about the red lock etc., we just need the page to load....

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

