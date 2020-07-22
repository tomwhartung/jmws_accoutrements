
# 5d-groja.md

Updating Groja.com so it is just exactly perfect.

# Fixing Conversions

- [x] Fix this error: `ModuleNotFoundError: No module named 'flask_wtf'`
- [x] New conversion: `conversion/avin`
    - [x] It is now the **Intermittent** instead of the ~~Monthly~~ Newsletter
        - [x] Rename all occurrences from the ~~Monthly~~ to the **Intermittent** Newsletter
    - [x] Keep `conversion/avmn` because many pages on seeourminds.com still use it!
    - [x] Remove unused conversions
        - [x] Remove code from `groja.py`
        - [x] Remove templates from `conversion/` and `thanks/` directories
- [x] Test remaining conversions
    - [x] Install any additional required packages
    - [x] Test new `avin` conversion
       - [x] `http://127.0.0.1:5000/conversion/avin`
       - [x] Ensure it updates db
       - [x] Ensure it sends email
    - [x] Test old `avmn` conversion
       - [x] `http://127.0.0.1:5000/conversion/avmn`
    - [x] Test each of these other conversions at least once on ava
       - [x] `http://127.0.0.1:5000/conversion/get_your_portrait`
       - [x] `http://127.0.0.1:5000/conversion/politicians_challenge`
       - [x] `http://127.0.0.1:5000/conversion/seeourminds`
- [ ] Cleanup DB

Details and sub-processes for each of these steps appear below.

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

- [x] bette
- [x] jane
- [x] barbara

```
pip install flask-wtf
pip install email_validator
```

# Testing Conversions

## Checking the Database

References:

- (1) https://www.sqlitetutorial.net/
- (2) https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-show-tables/
- (3) https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-describe-table/
- (4) https://www.sqlitetutorial.net/sqlite-dump/

Interestingly, I am unable to quickly find a reference for "how to install sqlite on ubuntu 20.04 focal fossa".

### Installing Sqlite3

The references above reference Sqlite3, but the command is not available:

```
$ which sqlite3
$ which sqlite
$
```

Also, running `apt-list` shows we need to install `sqlite3` specifically, rather than just `sqlite`:

```
$ apt list 'sqlite'
Listing... Done
sqlite/focal 2.8.17-15fakesync1build1 amd64
$ apt list 'sqlite3'
$ apt install 'sqlite3'
Listing... Done
sqlite3/focal-updates,focal-security 3.31.1-4ubuntu0.1 amd64
sqlite3/focal-updates,focal-security 3.31.1-4ubuntu0.1 i386
$ apt install sqlite3
Reading package lists... Done
Building dependency tree
Reading state information... Done
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  sqlite3
0 upgraded, 1 newly installed, 0 to remove and 4 not upgraded.
Need to get 860 kB of archives.
After this operation, 2,803 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 sqlite3 amd64 3.31.1-4ubuntu0.1 [860 kB]
Fetched 860 kB in 12s (71.4 kB/s)
Selecting previously unselected package sqlite3.
(Reading database ... 235004 files and directories currently installed.)
Preparing to unpack .../sqlite3_3.31.1-4ubuntu0.1_amd64.deb ...
Unpacking sqlite3 (3.31.1-4ubuntu0.1) ...
Setting up sqlite3 (3.31.1-4ubuntu0.1) ...
Processing triggers for man-db (2.9.1-1) ...
$
```

```
$ which sqlite
$ which sqlite3
/usr/bin/sqlite3
$
```

### Examining the Contents of the Db

Following the tutorial in the references above:

```
$ sqlite3 NameEmail.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
NameEmail
sqlite> .table
NameEmail
sqlite> pragma table_info('NameEmail');
0|id|INTEGER|0||1
1|name|TEXT|0||0
2|email|TEXT|0||0
3|site|TEXT|0|'groja.com'|0
4|active|INTEGER|0|1|0
5|date_added|TEXT|0|CURRENT_TIMESTAMP|0
6|date_changed|TEXT|0|CURRENT_TIMESTAMP|0
7|consulting|INTEGER|0|0|0
8|newsletter|INTEGER|0|0|0
9|portrait|INTEGER|0|0|0
sqlite> .output NameEmail-dump.sql
sqlite> .dump
sqlite> .exit
tomh@ava: /var/www/groja.com/htdocs/groja.com/gitignored/db
$ more NameEmail-dump.sql
$
```

### Updating the Other Hosts

Install sqlite3 on these other servers:

- [x] bette
- [x] jane
- [x] barbara

```
apt install sqlite3 sqlite3-doc
```

Run the commands below to examine the current state of the DB:

```
$ sqlite3 NameEmail.db
sqlite> .tables
NameEmail
sqlite> .table
NameEmail
sqlite> pragma table_info('NameEmail');
. . .
. . .
. . .
sqlite> .output NameEmail-dump.sql
sqlite> .dump
sqlite> .exit
$ more NameEmail-dump.sql
. . .
. . .
. . .
$
```

## Fixing the `ConnectionRefusedError` Error

Testing the `avin` conversion, I get the following error:

- ConnectionRefusedError: [Errno 111] Connection refused

Reference:

- https://stackoverflow.com/questions/24709800/python-smtplib-why-is-the-connection-refused

### Install `sendmail` **OR NOT**

I am leaving this in here, but note that **installing `postfix` causes `sendmail` to be REMOVED** -- presumably -- see below.

Install sendmail **OR NOT** -- see below:

```
$ apt list sendmail
Listing... Done
sendmail/focal,focal 8.15.2-18 all
$ apt install sendmail
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  liblockfile-bin liblockfile1 libsigsegv2 lockfile-progs m4 procmail sendmail-base sendmail-bin sendmail-cf sensible-mda
Suggested packages:
  m4-doc sendmail-doc rmail logcheck resolvconf sasl2-bin
The following NEW packages will be installed:
  liblockfile-bin liblockfile1 libsigsegv2 lockfile-progs m4 procmail sendmail sendmail-base sendmail-bin sendmail-cf sensible-mda
0 upgraded, 11 newly installed, 0 to remove and 4 not upgraded.
Need to get 1,107 kB of archives.
After this operation, 4,914 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
. . .
. . .
. . .
I am creating a safe, default sendmail.mc for you and you can
run sendmailconfig later if you need to change the defaults.
. . .
. . .
. . .
To enable sendmail SASL2 support at a later date, invoke "/usr/share/sendmail/update_auth"
. . .
. . .
. . .
*** *** *** WARNING *** WARNING *** WARNING *** WARNING *** *** ***

Everything you need to support STARTTLS (encrypted mail transmission
and user authentication via certificates) is installed and configured
but is *NOT* being used.

To enable sendmail to use STARTTLS, you need to:
1) Add this line to /etc/mail/sendmail.mc and optionally
   to /etc/mail/submit.mc:
  include(`/etc/mail/tls/starttls.m4')dnl
2) Run sendmailconfig
3) Restart sendmail
. . .
. . .
. . .
WARNING: local host name (ava) is not qualified; see cf/README: WHO AM I?
WARNING: Group writable directory /var
. . .
. . .
. . .
$ apt install sendmail-doc
. . .
. . .
. . .
$
```

## Fixing Emails

Testing the `avin` conversion, there are no errors and it seems to work ok, but it does not send the emails.

Looking up how to use sendmail on the commandline revealed this reference:

- https://stackoverflow.com/questions/49206701/how-to-send-an-email-using-sendmail-command

I did not install postfix, so that could be the problem.

### Install `postfix`

Install postfix - I am fine with using the default version:

```
$ apt list postfix
Listing... Done
postfix/focal-updates 3.4.13-0ubuntu1 amd64
N: There is 1 additional version. Please use the '-a' switch to see it
root@ava: ~
$ apt list -a postfix
Listing... Done
postfix/focal-updates 3.4.13-0ubuntu1 amd64
postfix/focal 3.4.10-1ubuntu1 amd64
$ apt install postfix
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  liblockfile-bin liblockfile1 libsigsegv2 linux-headers-5.4.0-39 linux-headers-5.4.0-39-generic linux-image-5.4.0-39-generic linux-modules-5.4.0-39-generic
  linux-modules-extra-5.4.0-39-generic lockfile-progs m4 sendmail-base sendmail-cf sensible-mda
Use 'apt autoremove' to remove them.
Suggested packages:
  postfix-mysql postfix-pgsql postfix-ldap postfix-pcre postfix-lmdb postfix-sqlite sasl2-bin | dovecot-common resolvconf postfix-cdb postfix-doc
The following packages will be REMOVED:
  sendmail sendmail-bin
The following NEW packages will be installed:
  postfix
0 upgraded, 1 newly installed, 2 to remove and 0 not upgraded.
Need to get 1,198 kB of archives.
After this operation, 2,375 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 postfix amd64 3.4.13-0ubuntu1 [1,198 kB]
Fetched 1,198 kB in 10s (118 kB/s)
Preconfiguring packages ...
(Reading database ... 273018 files and directories currently installed.)
Removing sendmail (8.15.2-18) ...
dpkg: sendmail-bin: dependency problems, but removing anyway as you requested:
 sensible-mda depends on sendmail-bin | mail-transport-agent; however:
  Package sendmail-bin is to be removed.
  Package mail-transport-agent is not installed.
  Package sendmail-bin which provides mail-transport-agent is to be removed.
 sensible-mda depends on sendmail-bin | mail-transport-agent; however:
  Package sendmail-bin is to be removed.
  Package mail-transport-agent is not installed.
  Package sendmail-bin which provides mail-transport-agent is to be removed.

Removing sendmail-bin (8.15.2-18) ...
Selecting previously unselected package postfix.
(Reading database ... 272964 files and directories currently installed.)
Preparing to unpack .../postfix_3.4.13-0ubuntu1_amd64.deb ...
Unpacking postfix (3.4.13-0ubuntu1) ...
Setting up postfix (3.4.13-0ubuntu1) ...
Adding group `postfix' (GID 135) ...
Done.
Adding system user `postfix' (UID 126) ...
Adding new user `postfix' (UID 126) with group `postfix' ...
Not creating home directory `/var/spool/postfix'.
Creating /etc/postfix/dynamicmaps.cf
Adding group `postdrop' (GID 136) ...
Done.
setting myhostname: ava
setting alias maps
setting alias database
changing /etc/mailname to ava.groja.com
setting myorigin
setting destinations: $myhostname, ava.groja.com, ava, localhost.localdomain, localhost
setting relayhost:
setting mynetworks: 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
setting mailbox_command
setting mailbox_size_limit: 0
setting recipient_delimiter: +
setting inet_interfaces: all
setting inet_protocols: all
WARNING: /etc/aliases exists, but does not have a root alias.

Postfix (main.cf) is now set up with a default configuration.  If you need to
make changes, edit /etc/postfix/main.cf (and others) as needed.  To view
Postfix configuration values, see postconf(1).

After modifying main.cf, be sure to run 'systemctl reload postfix'.

Running newaliases
Created symlink /etc/systemd/system/multi-user.target.wants/postfix.service → /lib/systemd/system/postfix.service.
Processing triggers for ufw (0.36-6) ...
Processing triggers for systemd (245.4-4ubuntu3.1) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for rsyslog (8.2001.0-1ubuntu1) ...
Processing triggers for libc-bin (2.31-0ubuntu9) ...
$
```

Note that the `sendmail` command is still there, even though it was supposedly **REMOVED**:

```
$ which sendmail
/usr/sbin/sendmail
$
```

## Updating the Other Hosts

- [x] Install `sendmail` on these other servers -- **OR NOT**:
- [x] Install `postfix` on these other servers:
    - [x] bette - sendmail was already installed
    - [x] jane
    - [x] barbara

```
## apt install sendmail sendmail-doc    ## **OR NOT**
apt install postfix
###
### For Postfix Configuration
### -> Choose "Internet Site"
### -> Enter [ava|jane|bette|barbara].groja.com - as appropriate
###
```

## Testing the Other Hosts

- [ ] Test one or more of the conversions on each of these other servers:
    - [ ] bette
    - [ ] jane
- [ ] Test **ALL** of these conversions **at least once** on barbara
    - [ ] `http://groja.com/conversion/get_your_portrait`
    - [ ] `http://groja.com/conversion/politicians_challenge`
    - [ ] `http://groja.com/conversion/seeourminds`

## Cleanup DB

Remove unneeded entries:

- [ ] Entries used for testing
- [ ] Entries from evil suck-ass spammers

Reference:

- https://www.sqlitetutorial.net/

