
# 6a-https-comparing_references

Having never done this before, it's important we do it right.

Having found several references, we want to compare them and try to
develop a process that combines the best ideas from all of them.

## Options

Note that there are two options:

1) Self-Signed
2) Let's Encrypt

## References

### Configuration (1) Self-signed

- (1) https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04
  - contains steps we don't need
- (2) https://www.liquidweb.com/kb/how-to-create-a-self-signed-ssl-certificate-on-ubuntu/
  - looks good
- (3) https://www.liberiangeek.net/2014/10/enable-self-signed-ssl-certificates-apache2-ubuntu-14-04/
  - also looks good, starting to see a pattern here
- (4) https://linuxacademy.com/blog/linux/ubuntu-linux-apache-and-self-signed-certificates/
  - also looks good...
- (5) http://www.techrepublic.com/article/how-to-create-a-self-signed-certificate-to-be-used-for-apache2/
  - we should have more than enough "good" ones by now
- (6) https://www.maketecheasier.com/apache-server-ssl-support/
  - very minimal and not used
- (7) https://www.linode.com/docs/security/ssl/create-a-self-signed-certificate-on-debian-and-ubuntu
  - very very minimal and essentially useless

### Configuration (2) Let's encrypt

- (1) https://www.howtoforge.com/tutorial/install-apache-with-php-and-mysql-on-ubuntu-16-04-lamp/#-enable-the-ssl-website-in-apache
- (2) https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
- (3) https://help.ubuntu.com/lts/serverguide/httpd.html#https-configuration

## Process

### Configuration (1) Self-Signed on jane

#### Step 1.1: Setup

##### Step 1.1.1: Apache Module Setup

As root:
```
apache2ctl -M | grep ssl
```

If the module is not already enabled, enable it and restart apache:

As root:
```
a2enmod ssl
apache2ctl -M | grep ssl
service apache2 restart
```

##### Step 1.1.2: Install `openssl` if needed

As root:
```
dpkg-query --list '*openssl*'
```

We have it so no worries.

#### Step 1.2: Generate Certificate

Seeing some different examples in the various references.

##### Step 1.2.1: Comparing the references

First we do our due diligence and compare the information in the
various references:

###### (1) digitalocean.com:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

###### (2) liquidweb.com:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt
```

###### (3) liberiangeek.net:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/server.key -out /etc/apache2/ssl/server.crt
```

###### (4) linuxacademy.com:

```
openssl req -new > my.cert.csr   # generates the "Certificate Request" file.
openssl rsa -in privkey.pem -out my.new.key
openssl x509 -in my.cert.csr -out my.new.cert -req -signkey my.new.key -days 3650
cp my.new.cert /etc/ssl/certs/server.crt
cp my.new.key /etc/ssl/private/server.key
```

###### (5) techrepublic.com:

```
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
cp server.crt /etc/apache2/ssl/server.crt
cp server.key /etc/apache2/ssl/server.key
```

Wow they are all different!  Hmmm!!

##### Step 1.2.2: Running the command:

We have a winner! The digitalocean one looks best!

That page also has a good explantion of each parameter.

As root:
```
l ssl/certs/apa* ssl/private/apa*   # No such file or directory - just checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

Output (and answers given to prompts).

**NOTE: they want the Fully Qualified Domain Name (FQDN) or
IP Address in the Common Name field!**

```
crtGenerating a 2048 bit RSA private key
........+++
.................+++
writing new private key to '/etc/ssl/private/apache-selfsigned.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:Denver
Organization Name (eg, company) [Internet Widgits Pty Ltd]:JooMoo WebSites LLC
Organizational Unit Name (eg, section) []:HQ
Common Name (e.g. server FQDN or YOUR name) []:10.0.0.113
Email Address []:mark_as_spam@tomhartung.com
```

And:

```
$ l /etc/ssl/certs/apa* /etc/ssl/private/apa*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/apache-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/apache-selfsigned.key
$ l /etc/ssl/*/apa*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/apache-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/apache-selfsigned.key
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

```
ServerName server_domain_or_IP
```

**NOTE: this example does NOT add the port number!**

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

**NOTE: this example adds the port number!**

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

##### Step 1.3.4: Test

We tried a few different configurations and could not get it to work properly.

At this point we decided to put the reference comparisons in a separate
file (this one) and update the original file with only the essential
commands and tasks we learned while going through this process the first time.


### Configuration (2) Let's Encrypt - TBD

SSL configuration using Let's Encrypt is pending getting the
self-signed certificate to work on jane.

#### Step 2.1: Comparing the references

References (1) and (2) do not agree, and reference (3) is very minimal.

- (1) -last updated 3/29/2017
- (2) -posted 4/21/2016

#### Step 2.2: This is TBD!!

Do configuration (1) first then come back to this.

