
# JooMooWebSites.com - Upgrading Notes for 2016

We're always changing this, so this file is mostly to keep track of
what was done the last time or two, in case we find issues, and to
give us a starting point, with appropriate cautions and tips, for
next time.

## Reference:

Always check out the release news:

* https://www.joomla.org/announcements/release-news.html

Sometimes special instructions apply.

## Log

2016-12-22: Upgrading from 3.6.4 to 3.6.5 .
2016-10-31: Upgrading from 3.6.2 to 3.6.4 .

## Before You Start

Always backup db and ensure code is up-to-date and checked in.

1. On ALL hosts: backup DB and ensure code matches what is in github
   bu jm 01-before_upgrading_3_6_4_to_3_6_5
   gojmj
   git status
   git pull
2. Decide which host to do most of the work on:
   jane - our development server, with a new disk and plenty of memory, should do well

## 2016-12-22: Notes on Upgrading From 3.6.4 to 3.6.5

### Deciding on a Process

The Release News page links to this process:

* https://docs.joomla.org/J3.x:Updating_from_an_existing_version

Reviewing past attempts (../upgrading_in_backend_never_works.txt),
I feel like Charley Brown here, and joomla.org is Lucy holding the football.

### Step (1) Standard Preparatory Steps

Looking at the process recommended on joomla.org, presumably we can update using the back end.
That's what it's telling me to do.

We have fallen for that crap before.
If we are going that route, let's at least perform these preparatory steps.

#### 1.1. Check and fix file permissions

Access System Information -> Folder Permissions

If one or more of these is Unwritable, run the following commands and recheck:

```
gojmj
./fix_permissions.sh   # will ask for password to run sudo commands
```

To get configuration.php to show up as writable, try these commands:

```
cd ../gitignored
sudo chgrp www-data configuration.php
chmod 664 configuration.php
```

If that doesn't work, we may need to **TEMPORARILY** break the link and **TEMPORARILY** copy the file from ../gitignored :

```
rm configuration.php
cp ../gitignored/configuration.php .
sudo chgrp www-data configuration.php
chmod 775 configuration.php
```

Recheck in back end:

* System Information -> Folder Permissions

**** ***** ******
*** YOU ARE HERE
**** ***** ******

### Steps (2) through (5) Get Frustrated With Joomla Update

#### Step (2) Fixing warnings in Components -> Joomla Update

Components -> Joomla Update -> Upload & Update tab has two warnings

##### 2.1. "the php temporary folder is not set"

Fixed by setting the following values in /etc/php/7.0/apache2/php.ini

* sys_temp_dir = "/tmp"     ;; first try, did not fix warning, but shouldn't hurt
* upload_tmp_dir = "/tmp"   ;; second try, see reference, fixed warning

Restart apache!

Reference: https://forum.joomla.org/viewtopic.php?t=933658

##### 2.2. "Maximum PHP file upload size is too small: ... both upload_max_filesize and post_max_size settings of ... php.ini"

Fixed by setting the following value in /etc/php/7.0/apache2/php.ini

* upload_max_filesize = 8M

Restart apache!

#### Step (3) Clear all caches and check for db schema changes

* Click on System -> Clear Cache
* Click on System -> Clear Expired Cache
      -> Clear Expired Cache (Icon/Button just below heading)
* Check DB Schema: Extensions -> Manage -> Database

#### Step (4) Trying Components -> Joomla Update -> Upload & Update tab

Because jane is behind two firewalls, download the file in advance, and put it in:

* /var/www/joomoowebsites.com/downloads/Joomla_3.6.4-Stable-Update_Package.zip

Choosing: "Write files directly" in drop-down

* Click: Upload & Install

Doesn't do anything.

#### Step (5) Trying Components -> Joomla Update -> Live Update tab (default)

Choosing: "Write files directly" in drop-down ....

**OMFG! It tried to do something!**

**Bzzt!  "Message: Download of update package failed."**

##### 5.1 Trying more stuff

Handy tip: sometimes you need to check for upgrades to the upgrade component

* Reference: https://www.joomla-monster.com/blog/joomla-templates/5-issues-that-may-appear-while-updating-to-joomla-3-6-1-or-later

* Admin -> Extensions -> Manage -> Update -> Clear Cache

* Admin -> Extensions -> Manage -> Update -> Find Updates

##### 5.2 Found a couple more patch files ...

... at:

* https://downloads.joomla.org/cms/joomla3/3-6-4

(1) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz

(2) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.zip

Try using backend one more time with these guys....

* Admin -> Components -> Joomla Update -> Upload & Update (tab)

###### 5.2.1 Using (1):

This time, an "Are you sure you want to update!" dialog with login box appears!

1. Filled in credentials

2. Got "ERROR: invalid login" error (again)

3. Tried retyping password from scratch, and got it twice

4. Tried in chrome, same result

###### 5.2.2 Using (2):

Again, an "Are you sure you want to update!" dialog with login box appears

1. Got "ERROR: invalid login" error (again)

2. Tried in chrome, same result

3. Tried uploading from /var/.../joomoowebsites.com/tmp , same result

##### 5.3 Posted in the forums about all this:

* https://forum.joomla.org/viewtopic.php?f=710&t=929038&p=3439721#p3439721

Ahem.

```
----------------------------------
--- ABOVE PROCESS DID NOT WORK ---
----- USING MANUAL PROCEDURE -----
----------------------------------
```

Even though they advise against it...

#### Step (6) Fall back to manual procedure (as usual)

Starting with this page:

* https://docs.joomla.org/J3.x:Updating_from_an_existing_version

Also we have this one, but is it applicable to 3.6.x???

* https://docs.joomla.org/J3.x:Upgrading_from_Joomla_3.4.x_to_3.5

Not seeing any caveats in that regard.
As long as everything is backed up, there should be No Fear Here.

##### 6.1 Overview of preparatory steps (Steps 1-3 above, before Joomla Update frustration set in)

1. Fixed permissions
2. Fixed warnings on joomla update page
3. Check DB Schema: Extensions -> Manage -> Database
4. Downloaded a few files:

* (0) Joomla_3.6.0-Stable-Update_Package.zip - referenced on update page

* (1) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz - found on downloads page

* (2) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.zip - found on downloads page

-> I am thinking (1) is our best bet for this

##### 6.2 A process similar to this has worked before:

Run commands:

```
gojmj
cp ../../downloads/Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz .
tar -xvzf Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
rm Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
```

This did not work, rats.

* Oops, should have run fix_permissions.sh here
* See ammended procedure - 6.4 Try again - below
* (Update: fix_permissions didn't help, oh well)

##### 6.3 Check for changes needed for database:

Extensions -> Manage -> Database

* "Warning: Database is not up to date!"

Click on "Fix" button at top of page

* -> Got a bunch of warnings, "Failed deleting xxx.xx"

##### 6.4 Try again, this time be sure to fix permissions

###### 6.4.1 Restore db:

Run command:
```
rs -d 2016_10_31 jm 01-before_upgrading_3_6_4_to_3_6_5
```
###### 6.4.2 Restore code:

Run commands:

```
cd ..
l
mv joomoowebsites.com joomoowebsites.com-manual_upgrade_gave_warnings
git clone git@github.com:tomwhartung/joomoowebsites.com.git
lnJoomlaCustomizations
lnSubSites
cp gitignored/configuration.php joomoowebsites.com
cp ../downloads/Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz joomoowebsites.com
cd joomoowebsites.com
tar -xvzf Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
```

###### 6.4.3 Fix permissions and verify they are ok

Run command:

```
gojmj
fix_permissions.sh
```

Relogin to admin panel:

*  System -> System Information -> File permissions

Verify all are writable

###### 6.4.4 Check for changes needed for database:

Admin panel:

* Extensions -> Manage -> Database
* "Warning: Database is not up to date!"

Click on "Fix" button at top of page

* STILL got a bunch of "Failed deleting" warnings
* Guess we will have to live with the cruft!?!?!?

To see the warnings we got, see ../details/2016_11_01-upgrading-3_6_2-3_6_4.txt .
Moving on!

###### 6.4.5 Verify we are done

System -> System Information -> Joomla Version: 3.6.4

-> Still a whole lot easier and quicker ( < 1 hr.!) than trying to use Joomla Update in the back end!!!

##### 6.6 Commit the code, backup the database, backup the backup, and fix the link

Run commands:

```
gojmj
git add --all
git status
git commit -m 'Upgraded to 3.6.4.'
git push origin master
bu jm 02-after_upgrading_3_6_4_to_3_6_5
tarHome
diff configuration.php ../gitignored/configuration.php
rm configuration.php ; ln -s ../gitignored/configuration.php .
```

### Step (7) Upgrading backup host:

New backup host is barbara.

#### 7.1. Backup and restore

Backup current DB and restore final copy of DB from jane:

```
bu jm  01-before_upgrading_3_6_4_to_3_6_5          # IF NOT DONE ALREADY, DO IT NOW
rs -h jane -d 2016_11_01 jm 02-after_upgrading_3_6_4_to_3_6_5
```

#### 7.2. Pull the code and fix the permissions

Run commands:

```
gojmj
git pull
fix_permissions.sh  # Does checking this file in pose a security risk?  I don't see how, but...
```

#### 7.3. Test in broswer

Test front end in browser

* Check a few menu options

* Check articles with images

Test back end in browser

* System -> System Information -> System Information (check Joomla version)

* System -> System Information -> Folder Permissions (Unwritable configuration.php is ok)

* Extensions -> Manage -> Database (check schema version)

#### 7.4. Backup DB and backup the backup

Run commands:

```
bu jm  02-after_upgrading_3_6_4_to_3_6_5
tarHome
```

### Step (8) Upgrading production host:

New production host (server) is ava.

Follow the same process we did on barbara:

1. Backup (should be done) and restore final copy of DB from jane.

2. Pull the code and fix the permissions.

3. Test in browser.

4. Backup DB and we are done!

