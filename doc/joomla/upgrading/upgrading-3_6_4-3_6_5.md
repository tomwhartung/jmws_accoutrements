
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

### Step (2) Get Frustrated With Joomla Update

Try the Joomla Update component

#### 2.1 First try:

* Components -> Joomla Update -> Live Update tab
* Write files directly (drop-down)
* Install the Update (button)

**GOT ERROR:**

* **Error - Download of update package failed.**

NOT going to try to fix such a VAGUE AND UNINFORMATIVE error message (been there done that!).

Update package URL: clicked to download Joomla_3.6.5-Stable-Update_Package.zip .

#### 2.2 Second try:

* Components -> Joomla Update -> Upload & Update tab
* Browse for file Joomla_3.6.5-Stable-Update_Package.zip (downloaded just now on the Live Update tab)
* Write files directly (drop-down)
* Upload and Install (button)

**NO ERROR BUT NO JOY EITHER - returned to control panel and the red update message!**

```
----------------------------------
--- ABOVE PROCESS DID NOT WORK ---
----- USING MANUAL PROCEDURE -----
----------------------------------
```

Even though they advise against it...


### Step (3) Fall back to manual procedure (as usual)

Starting with this page, it looks familiar and we have had success with it before:

* https://docs.joomla.org/J3.x:Upgrading_from_Joomla_3.4.x_to_3.5

As long as everything is backed up, there should be No Fear Here.

#### 3.1 Overview of preparatory steps (Step (2) above, before Joomla Update frustration set in)

1. Fixed permissions
2. Check DB Schema: Extensions -> Manage -> Database
3. Download one or more files - see the downloads page: https://downloads.joomla.org/

* (0) Joomla_3.6.5-Stable-Update_Package.zip - downloaded in Step (2) (referenced on update page)
* (1) Joomla_3.6.x_to_3.6.5-Stable-Patch_Package.tar.gz - found on https://downloads.joomla.org/cms/joomla3/3-6-5

##### An interesting aside:

Just for grins, tried using the Joomla Update component (see Step (2)) to Upload and Install the:

* Joomla_3.6.x_to_3.6.5-Stable-Patch_Package.tar.gz file

This actually got me a little further: had to re-enter my admin credentials, then got our old friend "Invalid Login."

##### 3.2 Identify what worked before:

Login to admin panel:

*  System -> System Information -> File permissions

Verify all are writable.

Run commands:

```
gojmj
cp ../../downloads/Joomla_3.6.x_to_3.6.5-Stable-Patch_Package.tar.gz .
tar -xvzf Joomla_3.6.x_to_3.6.5-Stable-Patch_Package.tar.gz
rm Joomla_3.6.x_to_3.6.5-Stable-Patch_Package.tar.gz
```

**Forgetting to fix permissions BEFORE updating the DB can cause an issue.**

###### 3.2.1 IMPORTANT: Fix permissions and verify they are ok

Run commands:

```
gojmj
fix_permissions.sh
```

Access admin panel in browser:

*  System -> System Information -> File permissions

Verify all are writable

##### 3.2.2 Check for changes needed for database:

Extensions -> Manage -> Database

* "Warning: Database is not up to date!"

Click on "Fix" button at top of page

* -> Got a bunch of warnings, "Failed deleting xxx.xx"
* Guess we will have to live with the cruft!?!?!?

To see the warnings we got, see ../details/2017_01_02-upgrading-3_6_4-3_6_5.txt (in this repo).

**We have tried to fix those warnings before (e.g. by running fix_permissions.sh) and I think it is OK to ignore them.**

##### 3.2.3 These are the EXACT same warnings!

Note that the warnings we got this time, saved in ../details/2017_01_02-upgrading-3_6_4-3_6_5.txt (in this repo)
match the warnings we got last time, saved in ../details/2016_11_01-upgrading-3_6_2-3_6_4.txt (in this repo).

Moving on!

#### 3.3 Verify we are done

System -> System Information -> Joomla Version: 3.6.5

-> Still a whole lot easier and quicker ( < 1 hr.!) than trying to use Joomla Update in the back end!!!

#### 3.5 Commit the code, backup the database, backup the backup, and fix the link (if necessary)

Run commands:

```
gojmj
git add --all
git status
git commit -m 'Upgraded to 3.6.5.'
git push origin master
bu jm 02-after_upgrading_3_6_4_to_3_6_5
tarHome   # Backing up the backup
```

Fix the link to configuration.php (if necessary):

```
diff configuration.php ../gitignored/configuration.php
rm configuration.php ; ln -s ../gitignored/configuration.php .
```

**** ***** ******
*** YOU ARE HERE
**** ***** ******


### Step (4) Upgrading backup host:

New backup host is barbara.

#### 4.1. Backup and restore

Copy current DB from jane to barbara and ava, by running these commands **on jane:**

```
gobu
ls -altr
toBarbara joomoowebsites.com-2017_01_02-jane-02-after_upgrading_3_6_4_to_3_6_5.sql.gz
toAva joomoowebsites.com-2017_01_02-jane-02-after_upgrading_3_6_4_to_3_6_5.sql.gz
```

Restore copy of current DB from jane on barbara, by running these commands **on barbara:**

```
bu jm  01-before_upgrading_3_6_4_to_3_6_5          # IF NOT DONE ALREADY, DO IT NOW
rs -h jane -d 2017_01_02 jm 02-after_upgrading_3_6_4_to_3_6_5
```

#### 4.2. Pull the code and fix the permissions

Run commands:

```
gojmj
git pull
fix_permissions.sh  # Does checking this file in pose a security risk?  I don't see how, but...
```

#### 4.3. Test in broswer

Test front end in browser

* Check a few menu options

* Check articles with images

Test back end in browser

* System -> System Information -> System Information (check Joomla version)

* System -> System Information -> Folder Permissions (Unwritable configuration.php is ok)

* Extensions -> Manage -> Database (check schema version)

#### 4.4. Backup DB and backup the backup

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

