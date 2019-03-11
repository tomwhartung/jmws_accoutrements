
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
Coming back to this later, as time permits....

First tried some suggestions from this page:

- (1) https://stackoverflow.com/questions/39845636/the-pip-7-1-0-distribution-was-not-found-and-is-required-by-the-application

Then tried a variety of suggestions from a variety of pages at stackoverflow.
Worked on this off-and-on for a few days!

Ultimately the **second answer** on this page got me past one error...:

- (2) https://stackoverflow.com/questions/16237490/i-screwed-up-the-system-version-of-python-pip-on-ubuntu-12-10

... only to get another error.
The takeaways from that page are to run `pip install -U pip` and to use `hash -r`

This page helped fix the second error:

- (3) https://stackoverflow.com/questions/28210269/importerror-cannot-import-name-main-when-running-pip-version-command-in-windo

The takeaway from that page is to edit `/usr/bin/pip` .

Here are the commands that finally worked:

```
apt purge python-pip
apt purge python3-pip
cd /usr/local/bin
ls -al
rm pip*                       ## Per (1)
apt-get install python-pip    ## Per (2)
which pip
pip install -U pip            ## Error
hash -r                       ## Didn't help
cd /usr/bin
cat pip
l RCS
mkdir RCS
ci -l pip
vi pip                        ## Edit per (3)
pip install -U pip            ## Per (2)
cd
which pip
hash -r                       ## Per (2)
which pip
cat pip3
pip3 install Django==1.11.16
python3 -c "import django; print(django.get_version())"
### 1.11.16
```

#### 3. Ensure it runs

Visit:

- http://127.0.0.1:8001/
- http://127.0.0.1:8001/v

#### 4. SeeOurMinds.com and Postgresql

Need to install postgresql.

Reference used - but only minimally:
- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

As root:
```
apt-get install postgresql           ## "postgresql is already the newest version"
apt-get install postgresql-contrib   ## "postgresql-contrib is already the newest version"
pip3 install psycopg2                ## "Successfully installed psycopg2-2.7.7"
```

**Note: Get the following message running `seeourminds.com/Site/bin/run.sh`:**

```
/usr/local/lib/python3.6/dist-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
```

As root:
```
pip install psycopg2-binary  ## Using pip instead of pip3, to see what happens
```

**Note: Got the following message:**

```
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
```

**Note: Still get the above message when running `seeourminds.com/Site/bin/run.sh`.**

Trying pip3 as root:
```
pip3 install psycopg2-binary
```

**This stops the message above from appearing when running `seeourminds.com/Site/bin/run.sh`.**

