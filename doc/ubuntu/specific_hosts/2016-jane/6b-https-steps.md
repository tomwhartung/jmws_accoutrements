
# 6-https

It's time to get https going on seeourminds.com , and maybe others.

## Options

Note that there are two options:

1) Self-Signed
2) Let's Encrypt

## Goals

1) Set up the Self-Signed option on jane.

2) Set up the Let's Encrypt option on barbara and ava.

3) We would prefer to use the Let's Encrypt option on jane, but
if that is a hassle or not feasible for some reason,
we may want to go with Self-Signed, or maybe even just http.

## References

We found a lot of references to help with this process.
For a list of these, an analysis of each of them, and
details on what steps we got from which ones,
see the `6a-https-comparing_references.md` file in this directory:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-jane/6a-https-comparing_references.md

## Process

These are the steps we are following to get the Self-Signed SSL Certificate
configuration working on jane.

All commands must be run as root.

### Step 1.1: Installation and Setup

[ ] Ensure ssl is installed and enabled.
```
apache2ctl -M | grep ssl
```

[ ] If the module is not already enabled, enable it and restart apache:
```
a2enmod ssl
apache2ctl -M | grep ssl
service apache2 restart
```

[ ] Install `openssl` if needed
```
dpkg-query --list '*openssl*'
```

We have it so no worries.

### Step 1.2: Generate Certificate

One reason we are starting over is, none of the references really address
doing this in an environment that uses virtual hosts the way we do
(over six of them).

**It's clear we need to generate a separate certificate for each site.**

This process focuses on generating a certificate and setting it up for use
on the **seeourminds.com** site.

#### Step 1.2.1: The Command to Run

As root (all on one line!):
```
l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*   # No such file or directory - just checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/seeourminds-selfsigned.key \
    -out /etc/ssl/certs/seeourminds-selfsigned.crt
```

#### Step 1.2.2: Prompts and Answers

Following are the answers given to the prompts:

**NOTE: they want the Fully Qualified Domain Name (FQDN) or
IP Address in the `Common Name` field!**

Last time we used `10.0.0.113` and it didn't work, so this time we're using the FQDN.

**Getting that right may well be an important key to getting this to work properly.**

```
. . .
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:Denver
Organization Name (eg, company) [Internet Widgits Pty Ltd]:JooMoo WebSites LLC
Organizational Unit Name (eg, section) []:HQ
Common Name (e.g. server FQDN or YOUR name) []:jane.seeourminds.com
Email Address []:mark_as_spam@tomhartung.com
```

#### Step 1.2.3: Check for the Files

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

#### Step 1.3: Configuration

Now we need to tell apache to use the certificate files we generated.

##### Step 1.3.1: Comparing the references

First, let's do our due diligence and compare the references:

###### (1) digitalocean.com:

Mentions changing the parameters mentioned below under "Essential Config"
and adding a `ServerName` .

Also contains a lot of configuration that the others do not have,
that should help make it more secure.

Includes links to where they got the additional configuration, in case
we want to do more research.

###### (2) liquidweb.com:

Mentions updating the "Essential config" mentioned below and also mentions
adding this line, which I think we need:

```
ServerName kb.thebestfakedomainnameintheworld.com:443
```

Our version for this host:

```
ServerName jane.seeourminds.com:443
```

###### (3) liberiangeek.net:

Also mentions updating the "Essential config" mentioned below, as well as
adding the ServerName line, but no other additional config.

```
ServerName kb.thebestfakedomainnameintheworld.com:443
```

###### (4) linuxacademy.com:

Mentions updating the "Essential config" mentioned below **only.**

###### (5) techrepublic.com:

Like the Linuxacademy.com article, mentions updating the "Essential config"
mentioned below **only.**

Since they all mention these changes, we are calling those changes "Essential."

##### Step 1.3.2: Editing the file

Edit the config file:

```
cd /etc/apache2/sites-available
ci -l default-ssl.conf    # check in to RCS before changing anything!
vi default-ssl.conf
```

###### Essential Config:

We always need to:

* Ensure `SSLEngine on` is set
* Update the `SSLCertificateFile` and `SSLCertificateKeyFile`
parameters (set them to the files we generated in the previous step).

###### Additional config:

We may want to research and test some of the config mentioned in the
digitalocean article.

See the comments in the file to learn exactly how we edited it, and
run `rcsdiff` to see prior versions.

##### Step 1.3.3: Enable the config and restart apache:

As root:

```
a2ensite default-ssl.conf
service apache2 reload
```









### Configuration (2) Let's encrypt

References (1) and (2) do not agree, and reference (3) is very minimal.

- (1) -last updated 3/29/2017
- (2) -posted 4/21/2016

Do configuration (1) first then come back to this.

