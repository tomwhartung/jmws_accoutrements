
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

Visit http://jane.artsyvisions.com/v

