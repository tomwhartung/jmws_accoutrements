
# 5-test_and_finish_up.md

This file contains details on how to:

* Test the Let's Encrypt certificates and
* Back everything up, etc.

# Goal

Verify we can use https to access all of these sites:

* artsyvisions.com (Static)
* tomh.info (Static)
* groja.com (Python/Wsgi - Flask)
* seeourminds.com (Python/Wsgi - Django)
* joomoowebsites.com (LAMP CMS - Joomla)
* tomhartung.com (LAMP CMS - Drupal)
* tomwhartung.com (LAMP CMS - WordPress)

# Background

This file details the final steps in this process.

**All of the steps in all of the processes in all of the other files in this
directory must be performed before the steps in this one.**

For an overview of the goals and reasons for doing all this, see the `../README.md` file:

- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/https-ssl/README.md

# Process

**All commands must be run as root.**

## Step (1) Test in Browser

This is where it would be nice to be able to test this on a non-production host, but
we can implement Let's Encrypt only on hosts connected to the internet!

## Step (2): Check into RCS

When all config files are working, check them into RCS!
Quick before we mess something up!

- [ ] Run the following commands to ensure the latest versions are checked in to RCS:
```
cd /etc/apache2/sites-available
rcsdiff *.conf
ci -l *.conf
```

## Step (3): Automatic Renewal

The Let's Encrypt certificates expire after 90 days.

**It is possible, however, to set up a cronjob to renew them automatically.**

### Reference

We will want to refer to this after renewing them manually a few times:

- https://certbot.eff.org/docs/using.html#renewal

### Dry Run

Enter the following command to test certificate renewal:

```
certbot renew --dry-run
```

**Note:** This command will run on `ava` but **not** the backup host `barbara`.

### Renewal Command

Enter the following command within 30 days of the certificates' expiration date:

```
certbot renew
```

**Note:** This command will run on `ava` but **not** the backup host `barbara`.

### Cronjob Setup: TBD

Let's renew them manually a few times before trying to automate this.

**Note:** This cronjob will **not** run on the backup host barbara, because
it is not accessible from the internet without changing the configuration of our modems and routers.

The digitalocean article makes this look to be very easy, check it out:

- https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04#step-3-—-set-up-auto-renewal

## Step (4): Conclusion

Having three config files for each site, with names that follow the standard,
makes it super-easy to switch between http and https.

For details, see `6a-https-lets_encrypt-activation.md` in this directory.
- https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/ubuntu/specific_hosts/2016-ava/6a-https-lets_encrypt-activation.md

### Further Testing

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

