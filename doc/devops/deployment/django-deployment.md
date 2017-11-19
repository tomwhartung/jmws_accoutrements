
# Django Deployment

Our attempt to keep it simple hit a snag with the static files.  Very clever, django, very clever.

Once we get this process to work we will want to be able to use notes like this to do it quickly in the future.

## References

- Overview: https://docs.djangoproject.com/en/dev/howto/static-files/
- Settings: https://docs.djangoproject.com/en/dev/ref/settings/#static-files
- collectstatic: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/

## Process

This process is for the backup host barbara and the production host ava.

**The main thing is, we need to remember to run collectstatic.**

### Step (1) Sync any changes made to settings.py

Compare the version of settings.py on the development to the versions on barbara and ava.

On the development host jane:

```
goshs
cd gitignored/Site/Site/
diffBarbara settings.py
```

**NOTE: do NOT set DEBUG to True on the backup or production hosts!!**

Migrate any changes made as appropriate.

On the backup host barbara and production host jane:

```
goshs
cd gitignored/Site/Site/
diffBarbara settings.py
rd settings.py          # check in any old changes before making new ones!
vi settings.py
rd settings.py
ci -l settings.py       # when it works! (or wait until next time)
```

### Step (2) Pull code

Not the best way to deploy a site, sure, but I like to keep it simple and if it works, ...!

```
goshs      # /var/www/seeourminds.com/htdocs/seeourminds.com
git pull
```

### Step (3) Run collectstatic.sh

Run the `collectstatic.sh` shell script:

```
gosss      # /var/www/seeourminds.com/htdocs/seeourminds.com/Site
cd bin/
./collectstatic.sh
```

### Step (4) Restart the server

Restart the server.

As tomh (for commands to run as root, see below):
```
sudo service apache2 stop ; sleep 2 ; sudo service apache2 start
```

OR - as root:
```
service apache2 stop ; sleep 2 ; service apache2 start
```

### Step (5) Ensure site looks ok!

Start a tail of the access log file to ensure that we are visiting the site we think we're visiting.

```
tapa   # macro to run tail -f on the apache access.log file
```

Visit the site and ensure it looks good, checking the output of the `tapa` alias to
ensure we are visiting the correct installation of the site.

