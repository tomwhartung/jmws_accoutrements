
# 2f-tomwhartung.md

Totally changing everything about tomwhartung.com before moving it to the new server.

# Technical Updates

Switch tomwhartung.com from using WP to using Django and MDB.

- [ ] Get single-page, bare minimum, hello-world type site going
- [ ] Worry about coding after we do the server shuffle

## TomWHartung.com on Django

### References

- Start project
  - https://docs.djangoproject.com/en/3.0/intro/tutorial01/

### Process

Start the project, replace the settings.py file with a link, and copy in some basic files from `artsyvisions.com`:

```
gotwt                   # /var/www/tomwhartung.com/htdocs/tomwhartung.com
django-admin startproject Site
cd Site
python manage.py runserver
```

Access [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in the browser to confirm the installation worked ok,
then kill the server with Ctrl-C.


Replace the settings.py file with a link, and copy in some basic files from `artsyvisions.com`:

```
```

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Content Updates

Update site to contain:

- List of my spiritual portrait books
- List of my spiritual portrait sites
- List of social networking sites where I post spiritual portraits
- Call for help with sales
  - Maybe dedicate a page to this: I am no salesman, can offer commision only, etc.


