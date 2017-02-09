
# Django Deployment

Our attempt to keep it simple hit a snag with the static files.  Very clever, django, very clever.

Once we get this process to work we will want to be able to use notes like this to do it quickly in the future.

## References

- Overview: https://docs.djangoproject.com/en/dev/howto/static-files/
- Settings: https://docs.djangoproject.com/en/dev/ref/settings/#static-files
- collectstatic: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/

## Process

I am thinking we just need to remember to run collectstatic!  Let's give it a try, and see if it works!

### Run collectstatic

These are the super-paranoid baby steps I am taking the first time.  Hopefully this works, and next time will be a breeze!

```
goshs      # /var/www/seeourminds.com/htdocs/seeourminds.com
cd Site/
l          # manage.py should be in this directory
l static/
python3 manage.py collectstatic
l static/  # should see the new versions of any files
```

If it doesn't look just exactly perfect, try restarting the server.

```
sudo service apache2 stop ; sleep 2 ; sudo service apache2 start

```


