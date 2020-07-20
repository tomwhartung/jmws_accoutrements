
# 5d-groja.md

Updating Groja.com so it is just exactly perfect.

# Fixing Conversions

- [x] Error: `ModuleNotFoundError: No module named 'flask_wtf'`
- [ ] New Conversion: `conversions/avin`
    - [ ] It is now the **Intermittent** instead of the ~~Monthly~~ Newsletter
    - [ ] Keep `conversions/avmn` because many pages on seeourminds.com still use it!

## Fixing the `ModuleNotFoundError` Error

### Install `flask-wtf`

Try just installing `flask-wtf`

```
$ pip install flask-wtf
Collecting flask-wtf
  Downloading Flask_WTF-0.14.3-py2.py3-none-any.whl (13 kB)
Requirement already satisfied: Flask in /usr/local/lib/python3.8/dist-packages (from flask-wtf) (1.1.2)
Requirement already satisfied: itsdangerous in /usr/local/lib/python3.8/dist-packages (from flask-wtf) (1.1.0)
Collecting WTForms
  Downloading WTForms-2.3.1-py2.py3-none-any.whl (169 kB)
     |████████████████████████████████| 169 kB 99 kB/s
Requirement already satisfied: Jinja2>=2.10.1 in /usr/local/lib/python3.8/dist-packages (from Flask->flask-wtf) (2.11.2)
Requirement already satisfied: click>=5.1 in /usr/local/lib/python3.8/dist-packages (from Flask->flask-wtf) (7.1.2)
Requirement already satisfied: Werkzeug>=0.15 in /usr/local/lib/python3.8/dist-packages (from Flask->flask-wtf) (1.0.1)
Requirement already satisfied: MarkupSafe in /usr/local/lib/python3.8/dist-packages (from WTForms->flask-wtf) (1.1.1)
Installing collected packages: WTForms, flask-wtf
Successfully installed WTForms-2.3.1 flask-wtf-0.14.3
$
```

Now getting an exception: `Exception: Install 'email_validator' for email validation support.`

### Install `email_validator`

```
$ pip install email_validator
Collecting email_validator
  Downloading email_validator-1.1.1-py2.py3-none-any.whl (17 kB)
Collecting dnspython>=1.15.0
  Downloading dnspython-2.0.0-py3-none-any.whl (208 kB)
     |████████████████████████████████| 208 kB 51 kB/s
Requirement already satisfied: idna>=2.0.0 in /usr/lib/python3/dist-packages (from email_validator) (2.8)
Installing collected packages: dnspython, email-validator
Successfully installed dnspython-2.0.0 email-validator-1.1.1
$
```

Worked ok after restarting the server, yay!

### Fix the Other Hosts

Run the two commands below on:

- [x] jane
- [x] bette
- [x] barbara

```
pip install flask-wtf
pip install email_validator
```


# Installing Additional Required Packages

Postgres may be needed, or does the site use sqlite?

- [ ] Determine whether site uses postgres, sqlite, or ???
- [ ] Install any additional required packages
- [ ] Fix `avmn` conversion, and others as necessary
- [ ] Check for and remove free spiritual portrait offer, if present

# Review and Content Updates

- [ ] Ensure social media icons link to same accounts as artsyvisions
- [ ] Upgrade MDB to latest version
- [ ] Review conversions
    - [ ] Disable any that are unused
    - [ ] Ensure the remaining conversions work ok
    - [ ] Delete any conversions that are obsolete
    - [ ] Try to prevent spam - got some but not getting it any more
- [ ] Set list price for a spiritual portrait to $500
- [ ] Review about page and update as appropriate
- [ ] Review for anything glaring

