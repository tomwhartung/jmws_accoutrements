
# 1-bette-django.md

How to install django after upgrading to 18.04 LTS.

## Reference

- https://stackoverflow.com/questions/41588925/pip-install-django-on-python3-6

## Process

#### 1. Figure out which version

Check version being used on jane by visiting http://jane.artsyvisions.com/v

- Python: 3.5.2
- Django: 1.11.16

#### 2. Install

Check for python3 and pip3, and install django:

As root:
```
which python3    # /usr/bin/python3
python3 -V       # Python 3.6.7
which pip3       # /usr/local/bin/pip3
pip3 install Django==1.11.16
```

First try: got an error.

Trying some suggestions from this page:
- https://stackoverflow.com/questions/39845636/the-pip-7-1-0-distribution-was-not-found-and-is-required-by-the-application

```
apt purge python-pip
apt purge python3-pip
cd /usr/local/bin
ls -al
rm pip*
apt-get install python-pip python3-pip
pip3 install Django==1.11.16
python3 -c "import django; print(django.get_version())"
```

#### 3. Ensure it runs

Visit http://jane.artsyvisions.com/v


#### 4. Add to Launcher

Find xscreensaver icon in dock search tool and add it to the Launcher.

#### 5. Adjust settings as necessary

Check times and other parameters in dialog.

