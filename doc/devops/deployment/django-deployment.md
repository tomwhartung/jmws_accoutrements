
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

### Step (3) Run collectstatic

These are the super-paranoid baby steps I am taking the first time.  Hopefully this works, and next time will be a breeze!

```
goshs      # /var/www/seeourminds.com/htdocs/seeourminds.com
cd Site/
l          # manage.py should be in this directory
l static/
python3 manage.py collectstatic
l static/  # should see the new versions of any files
```

### Step (4) Restart the server

Restart the server.

```
sudo service apache2 stop ; sleep 2 ; sudo service apache2 start
```

### Step (5) Ensure site looks ok!

Visit the site and ensure it looks good.

