
# self_signed - 1-comparing_references.md

Having found several references, we want to compare them and try to
develop a process that combines the best ideas from all of them.

# Moot at This Time

Having decided to not use self-signed certificates on `jane` or any other
hosts, **this information is irrelevant at this time.**

# List of References

These references for setting up the Self-signed configuration are listed in
more-or-less the same order as they appeared in my google search results.

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

# Results

## Best Reference

By far, the best reference is the first one (digitalocean.com).

## Best Process (Overview)

This high-level process can work for both self-signed certificates and
for those from Let's Encrypt.

The best process is:

1. Generate the certificate.

2. Copy current apache config file, eg.

```
cp 050-seeourminds.com.conf 051-seeourminds.com-ssl.conf
```

3. Add the lines mentioned below to that file.

4. Update the original file (e.g., `050-seeourminds.com.conf`) to redirect to https.

For details, see the file `2-openssl.md` in this directory.

# About the Rest of This File

**The rest of this information is pretty much summarized in `2-openssl.md` .**

So there's no pressing need to read the rest of this,
we are just saving it for possible future reference....

## Configuration (1) Self-Signed on jane

We compare references for the processes that:

1. Generate the certificate
2. Update the apache config

Because those processes are fairly complex and the references are not in total agreement.

### Process 1: Generate Certificate

Seeing some different examples in the various references.

#### Comparing the references

First we do our due diligence and compare the information in the
various references:

##### (1) digitalocean.com:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

##### (2) liquidweb.com:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt
```

##### (3) liberiangeek.net:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/server.key -out /etc/apache2/ssl/server.crt
```

##### (4) linuxacademy.com:

```
openssl req -new > my.cert.csr   # generates the "Certificate Request" file.
openssl rsa -in privkey.pem -out my.new.key
openssl x509 -in my.cert.csr -out my.new.cert -req -signkey my.new.key -days 3650
cp my.new.cert /etc/ssl/certs/server.crt
cp my.new.key /etc/ssl/private/server.key
```

##### (5) techrepublic.com:

```
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
cp server.crt /etc/apache2/ssl/server.crt
cp server.key /etc/apache2/ssl/server.key
```

Wow they are all different!  Hmmm!!

##### Picking and running the command:

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

### Process 2: Apache Configuration

Now we need to tell apache to use the certificate files we generated.

#### Comparing the references

First, let's do our due diligence and compare the references:

##### (1) digitalocean.com:

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

##### (2) liquidweb.com:

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

##### (3) liberiangeek.net:

Also mentions updating the "Essential config" mentioned below, as well as
adding the ServerName line, but no other additional config.

```
ServerName kb.thebestfakedomainnameintheworld.com:443
```

##### (4) linuxacademy.com:

Mentions updating the "Essential config" mentioned below **only.**

##### (5) techrepublic.com:

Like the Linuxacademy.com article, mentions updating the "Essential config"
mentioned below **only.**

Since they all mention these changes, we are calling those changes "Essential."

#### Editing the file

Edit the config file:

```
cd /etc/apache2/sites-available
ci -l default-ssl.conf    # check in to RCS before changing anything!
vi default-ssl.conf
```

##### Essential Config:

We always need to:

* Ensure `SSLEngine on` is set
* Update the `SSLCertificateFile` and `SSLCertificateKeyFile`
parameters (set them to the files we generated in the previous step).

##### Additional config:

We may want to research and test some of the config mentioned in the
digitalocean article.

See the comments in the file to learn exactly how we edited it, and
run `rcsdiff` to see prior versions.

