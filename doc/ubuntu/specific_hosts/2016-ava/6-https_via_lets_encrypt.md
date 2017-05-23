
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

## "Reference-1"

The term "reference-1" refers to our #1 main reference:

- https://certbot.eff.org/#ubuntuxenial-apache

# Goal

Set up https using Let's Encrypt option on ava.

# Results

TBD.

# Process

These are the steps we are following:

**All commands must be run as root.**

## Step (1): Check apache conf files

- [ ] Ensure the current versions of all apache conf files are checked into RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
```
- [ ] Check in any files that are not already checked in.

-> FYI: noticing that the ssl module is not enabled (yet).

### Step (2): Installation

- [ ] Ensure everything else is up-to-date
```
apt-get update
apt-get upgrade
```

- [ ] Add the certbot ppa and install the program (see reference 1):
```
apt-get install software-properties-common
apt autoremove     # suggested by output of previous command
add-apt-repository ppa:certbot/certbot
apt-get update
apt-get install python-certbot-apache
```

### Step (3): Configure Modems and Routers

Modems and routers must be configured to accept https requests on port 443 and
pass them through to the appropriate host(s).

Specific steps for this process are beyond the scope of this document.

### Step (4): Generate a Certificate

The `certbot` command supports generating a certificate (or certificateS?)
for multiple sites.

This process focuses on generating a certificate and setting it up for use
on the **seeourminds.com** site on **ava**.

#### Step (4.1): Try the All-in-One Command

- [ ] Run the all-in-one command from reference 1:
```
certbot --apache
```
- [ ] Read the terms of service at:
  https://letsencrypt.org/documents/LE-SA-v1.1.1-August-1-2016.pdf
- [ ] Answer the questions (there are far fewer questions than there were for self-signed)
```
Enter email address (...) (Enter 'c' to cancel): lets_encrypt@tomhartung.com
(A)gree/(C)ancel: A
(Y)es/(N)o: Y
Which names would you like to activate HTTPS for?
```

Trying to do just seeourminds.com resulted in an error:
```
Error while running apache2ctl configtest.
Action 'configtest' failed.
The Apache error log may have more information.

AH00526: Syntax error on line 33 of /etc/apache2/sites-enabled/050-seeourminds.com.conf:
Name duplicates previous WSGI daemon definition.

Rolling back to previous server configuration...
Error while running apache2ctl configtest.
Action 'configtest' failed.
The Apache error log may have more information.

AH00526: Syntax error on line 33 of /etc/apache2/sites-enabled/050-seeourminds.com.conf:
Name duplicates previous WSGI daemon definition.


IMPORTANT NOTES:
 - We were unable to install your certificate, however, we
   successfully restored your server to its prior configuration.
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/www.seeourminds.com/fullchain.pem. Your cert
   will expire on 2017-08-20. To obtain a new or tweaked version of
   this certificate in the future, simply run certbot again with the
   "certonly" option. To non-interactively renew *all* of your
   certificates, run "certbot renew"
```

#### Step (4.2): Check for the Files


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


As root:
```
$ l /etc/ssl/certs/seeourminds* /etc/ssl/private/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
$ l /etc/ssl/*/seeourminds*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/seeourminds-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/seeourminds-selfsigned.key
```




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

