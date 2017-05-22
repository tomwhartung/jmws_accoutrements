
# 6-https_via_lets_encrypt

After having limited success using a self-signed certificate on jane,
we are going for setting up https using Let's Encrypt on ava.
Jumping straight to production!  I know!!

# Research

For details on how we came up with this process, see the `6*.md` files in
`../2016-jane` , specifically:

```
../2016-jane/6b-analysis_of_requirements.md
../2016-jane/6d-comparing_references-lets_encrypt.md
```

# Goal

Set up https using Let's Encrypt option on ava.

# Results

TBD.

# Process

These are the steps we are following:

**All commands must be run as root.**

## Step (0): Check apache conf files

- [ ] Ensure the current versions of all apache conf files are checked into RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```
- [ ] Check in any files that are not already checked in.

### Step (1): Installation and Setup

- [ ] Ensure everything is up-to-date
```
apt-get update
apt-get upgrade
```

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

I think it's best to generate a separate certificate for each site.

This process focuses on generating a certificate and setting it up for use
on the **seeourminds.com** site on **ava**.

#### Step (2.1): The Command to Run

As root (all on one line!):
```
l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*   # No such file or directory - just checking!
l /etc/ssl/*/seeourminds*                                     # Double checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/seeourminds-selfsigned.key \
    -out /etc/ssl/certs/seeourminds-selfsigned.crt
```

#### Step (2.2): Prompts and Answers

Following are the answers given to the prompts:

**NOTE: they want the Fully Qualified Domain Name (FQDN) or
IP Address in the `Common Name` field!**

Last time we used `10.0.0.113` and it didn't work, so this time we're using the FQDN.

**Getting that right may well be an important key to getting this to work properly.**

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

#### Step (2.3): Check for the Files

As root:
```
$ l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
$ l /etc/ssl/*/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
```

**NOTE: due to permissions, we can see the private only when logged in as root
(we are unable to see it using sudo!).**

### Step (3): Apache Configuration

Now we need to tell apache to use the certificate files we generated.

#### Step (3.1) Try with and without port number

The digitalocean.com reference mentions updating a line with the `ServerName`
**without** the port number.

The liberiangeek.net reference mentions updating a line with the `ServerName`
**with** the port number.

**Try both ways until we get one to work!**

#### Step (3.2): Editing the file

- [ ] Edit the config file:

```
cd /etc/apache2/sites-available
cp 050-seeourminds.com.conf 051-seeourminds.com-ssl.conf
ci -l 051-seeourminds.com-ssl.conf
vi 051-seeourminds.com-ssl.conf
```

- [ ] Make the following changes:

* Ensure `SSLEngine on` is set
* Update the `SSLCertificateFile` and `SSLCertificateKeyFile`
parameters (set them to the files we generated in the previous step).
* Ensure `SSLEngine on` is set

See the `default-ssl.conf` file that we were messing with before for
examples of how to edit the new file.

#### Step (3.3): Enable the config and restart apache:

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

