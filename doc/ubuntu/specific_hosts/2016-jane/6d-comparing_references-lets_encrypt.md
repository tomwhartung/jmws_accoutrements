
# 6d-comparing_references-lets_encrypt

This file covers the references we have found for using a certificate from
Let's Encrypt to set up ssl on apache.

## References

### Configuration (2) Let's encrypt

These are listed in more-or-less the same order as they appeared in my google search results.

- (1) https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
  - Dated 4/21/2016
  - Uses `certbot` (and digitalocean.com has cred points for being the best reference for the self-signed option)
  - The digitalocean.com reference was the best one for Configuration (1).
- (2) https://www.howtoforge.com/tutorial/install-apache-with-php-and-mysql-on-ubuntu-16-04-lamp/#-enable-the-ssl-website-in-apache
  - Dated 3/29/2017
  - Uses `python-letsencrypt-apache`
- (3) https://www.vultr.com/docs/setup-lets-encrypt-with-apache-on-ubuntu-16-04
  - Dated 8/24/2016
  - Uses letsencrypt repo on github (https://github.com/letsencrypt/letsencrypt)
  - Accessing this repo redirects to certbot repo (https://github.com/certbot/certbot)
- (4) https://certbot.eff.org/all-instructions/#ubuntu-16-04-xenial-apache
  - EFF certbot page
- (5) http://dev-notes.eu/2017/02/letsencrypt-ubuntu-xenial/
  - Dated 2/25/2017
  - Also references certbot
- (6) https://community.letsencrypt.org/t/help-with-ubuntu-16-04-apache-and-letsencrypt-set-up/17889
  - Dated July, 2016
  - Forum post in which an expert walks a complete novice through the process
- (7) https://certbot.eff.org/#ubuntuxenial-apache
  - Another EFF certbot page, NOTE: contains two "tabs," Automated and Advanced
- (8) https://help.ubuntu.com/lts/serverguide/httpd.html#https-configuration
  - So minimal that it's worthless

## Comparing the references

## Results

Using Certbot certainly seems to be the best choice.

From their github page:

> Certbot, previously the Let's Encrypt Client,
> is EFF's tool to obtain certs from Let's Encrypt, and
> (optionally) auto-enable HTTPS on your server






