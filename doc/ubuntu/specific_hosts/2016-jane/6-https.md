
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

### Configuration (1) Self-signed

- (1) https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04
- - contains steps we don't need
- (2) https://www.liquidweb.com/kb/how-to-create-a-self-signed-ssl-certificate-on-ubuntu/
- - looks good
- (3) https://www.liberiangeek.net/2014/10/enable-self-signed-ssl-certificates-apache2-ubuntu-14-04/
- - also looks good, starting to see a pattern here
- (4) https://linuxacademy.com/blog/linux/ubuntu-linux-apache-and-self-signed-certificates/
- - also looks good...
- (5) http://www.techrepublic.com/article/how-to-create-a-self-signed-certificate-to-be-used-for-apache2/
- - we should have more than enough "good" ones by now
- (6) https://www.maketecheasier.com/apache-server-ssl-support/
- - very minimal
- (7) https://www.linode.com/docs/security/ssl/create-a-self-signed-certificate-on-debian-and-ubuntu
- - very very minimal

### Configuration (2) Let's encrypt

- (1) https://www.howtoforge.com/tutorial/install-apache-with-php-and-mysql-on-ubuntu-16-04-lamp/#-enable-the-ssl-website-in-apache
- (2) https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
- (3) https://help.ubuntu.com/lts/serverguide/httpd.html#https-configuration

## Process

### Configuration (1) Self-Signed on jane

#### Step 1.1: Setup

#### Step 1.1.1: Apache Module Setup

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

#### Step 1.1.2: Install `openssl` if needed

As root:
```
dpkg-query --list '*openssl*'
```

We have it so no worries.

#### Step 1.2: Generate Certificate

Seeing some different examples in the various references.

#### Step 1.2.1: Comparing the references

Let's compare the references:

(1) digitalocean.com:
- `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt`
(2) liquidweb.com:
- `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt`
(3) liberiangeek.net:
- `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/server.key -out /etc/apache2/ssl/server.crt`
(4) linuxacademy.com:
- `openssl req -new > my.cert.csr` - generates the "Certificate Request" file.
- `openssl rsa -in privkey.pem -out my.new.key`
- `openssl x509 -in my.cert.csr -out my.new.cert -req -signkey my.new.key -days 3650`
- `cp my.new.cert /etc/ssl/certs/server.crt`
- `cp my.new.key /etc/ssl/private/server.key`
(5) techrepublic.com:
- `openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt`
- `cp server.crt /etc/apache2/ssl/server.crt`
- `cp server.key /etc/apache2/ssl/server.key`

Wow they are all different!  Hmmm!!

#### Step 1.2.2: Running the command:

We have a winner! The digitalocean one looks best!

That page also has a good explantion of each parameter.

As root:
```
l ssl/certs/apa* ssl/private/apa*   # No such file or directory - just checking!
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

Output (and answers given to prompts).

** NOTE: they want the Fully Qualified Domain Name (FQDN) or
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
$ l ssl/certs/apa* ssl/private/apa*
-rw-r--r-- 1 root root 1480 May  8 19:48 ssl/certs/apache-selfsigned.crt
-rw-r--r-- 1 root root 1704 May  8 19:48 ssl/private/apache-selfsigned.key
```









### Configuration (2) Let's encrypt

References (1) and (2) do not agree, and reference (3) is very minimal.

- (1) -last updated 3/29/2017
- (2) -posted 4/21/2016

Do configuration (1) first then come back to this.

