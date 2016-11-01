
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

2016-10-31: Upgrading from 3.6.2 to 3.6.4 .
(Unsure how we got from 3.6.0 to 3.6.2 .)

## Before You Start

Always backup db and ensure code is up-to-date and checked in.

1. On ALL hosts: backup DB and ensure code matches what is in github
   bu jm 01-before_upgrading_3.6.2_to_3.6.4
   gojmj
   git status
   git pull
2. Decide which host to do most of the work on:
   jane - our development server, with a new disk and plenty of memory, should do well

## 2016-10-31: Notes on Upgrading From 3.6.2 to 3.6.4

The Release News page links to this process:

* https://docs.joomla.org/J3.x:Updating_from_an_existing_version

Reviewing past attempts (../upgrading_in_backend_never_works.txt),
I feel like Charley Brown here, and joomla.org is Lucy holding the football.

### Not cool

1. In ../upgrading_in_backend_never_works.txt it says to access: Adminitrator -> Extensions -< Manage -> Install 

2. That page says:
"**Warning:** No installation plugin has been enabled.
At least one must be enabled to be able to use the installer.
Go to the Plugin Manager to enable the plugins."

3. Going to the Plugin Manager confirms that four installation plugins are installed and enabled.

4. Returning to the Adminitrator -> Extensions -< Manage -> Install page, it still displays that warning.  Sheesh fml.

### Observations

Aha! Checking the permissions in Step (1) it says plugins/installer is unwritable - added that to fix_permissions.sh ....

Still seeing the warning message.

Trying to edit the plugins listed (by clicking on their names), three of the four give me an error:

1. Installer - Install from Web: able to open it up, not many options to edit though

2. Installer - Install from Upload: "Error The file packageinstaller.xml could not be found."

3. Installer - Install from Folder: "Error The file folderinstaller.xml could not be found."

4. Installer - Install from URL: "Error The file folderinstaller.xml could not be found."

### The Fix!?!

Downloaded Joomla_3.6.4-Stable-Full_Package.zip and found code in the following directories:

* plugins/installer/folderinstaller/
* plugins/installer/packageinstaller/
* plugins/installer/urlinstaller/

Coped this code into the site directory tree and it fixed the errors!

### Step (1) Standard Preparatory Steps

Looking at the process recommended on joomla.org, presumably we can update using the back end.
That's what it's telling me to do.
We have fallen for that crap before.
If we are going that route, let's at least perform these preparatory steps.

1. Check and fix file permissions
   System Information -> Folder Permissions
   If one or more of these is Unwritable, run these commands and recheck:
```
gojmj
./fix_permissions.sh   # will ask for password to run sudo commands
```
   To get configuration.php to show up as writable, may need to:
   o  ** TEMPORARILY ** break the link and
   o  ** TEMPORARILY ** copy the file from ../gitignored
```
rm configuration.php
cp ../gitignored/configuration.php .
sudo chgrp www-data configuration.php
chmod 775 configuration.php
```
   Recheck in back end:
      System Information -> Folder Permissions

### Steps (2) through (5) Get Frustrated With Joomla Update

#### Step (2) Fixing warnings in Components -> Joomla Update

   Components -> Joomla Update -> Upload & Update tab has two warnings

   2.1. "the php temporary folder is not set"
     Fixed by setting the following values in /etc/php/7.0/apache2/php.ini
       sys_temp_dir = "/tmp"     ;; first try, did not fix warning, but shouldn't hurt
       upload_tmp_dir = "/tmp"   ;; second try, see reference, fixed warning
     Restart apache
     Reference: https://forum.joomla.org/viewtopic.php?t=933658

   2.2. "Maximum PHP file upload size is too small: ... both upload_max_filesize and post_max_size settings of ... php.ini"
     Fixed by setting the following value in /etc/php/7.0/apache2/php.ini
       upload_max_filesize = 8M
     Restart apache

#### Step (3) Clear all caches and check for db schema changes

   Click on System -> Clear Cache
   Click on System -> Clear Expired Cache
      -> Clear Expired Cache (Icon/Button just below heading)
   Check DB Schema: Extensions -> Manage -> Database

#### Step (4) Trying Components -> Joomla Update -> Upload & Update tab

   Because jane is behind two firewalls
   Download file, put in:
     /var/www/joomoowebsites.com/downloads/Joomla_3.6.4-Stable-Update_Package.zip
   Choosing: "Write files directly" in drop-down
   Click: Upload & Install
   Doesn't do anything.

#### Step (5) Trying Components -> Joomla Update -> Live Update tab (default)

Choosing: "Write files directly" in drop-down ....

It tried to do something!  "Message: Download of update package failed."

5.1 Trying more stuff
   Handy tip: sometimes you need to check for upgrades to the upgrade component
      https://www.joomla-monster.com/blog/joomla-templates/5-issues-that-may-appear-while-updating-to-joomla-3-6-1-or-later
   Admin -> Extensions -> Manage -> Update -> Clear Cache
   Admin -> Extensions -> Manage -> Update -> Find Updates
5.2 Found a couple more patch files at:
      https://downloads.joomla.org/cms/joomla3/3-6-4
      (1) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
      (2) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.zip
   Try using backend one more time with these guys....
      Admin -> Components -> Joomla Update -> Upload & Update (tab)
5.2.1 Using (1):
   This time, an "Are you sure you want to update!" dialog with login box appears!
     Credentials filled in
     Got "ERROR: invalid login" error (again)
     Tried retyping password from scratch, and got it twice
     Tried in chrome, same result
5.2.2 Using (2):
   Again, an "Are you sure you want to update!" dialog with login box appears
     Got "ERROR: invalid login" error (again)
     Tried in chrome, same result
   Tried uploading from /var/.../joomoowebsites.com/tmp , same result
5.2.3 Posted in the forums about all this:
   https://forum.joomla.org/viewtopic.php?f=710&t=929038&p=3439721#p3439721

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

6.1 Overview of preparatory steps (Steps 1-3 above, before Joomla Update frustration set in)
   Fixed permissions
   Fixed warnings on joomla update page
   Check DB Schema: Extensions -> Manage -> Database
   Downloaded a few files:
      (0) Joomla_3.6.0-Stable-Update_Package.zip - referenced on update page
      (1) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz - found on downloads page
      (2) Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.zip - found on downloads page
   -> I am thinking (1) is our best bet for this

6.2 A process similar to this has worked before:
   gojmj
   cp ../../downloads/Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz .
   tar -xvzf Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
   rm Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz
   ****************************************************
   ** Oops, should have run fix_permissions.sh here  **
   ** See ammended procedure - 6.4 Try again - below **
   ** (Update: fix_permissions didn't help, oh well) **
   ****************************************************
6.3 Check for changes needed for database:
   Extensions -> Manage -> Database
      "Warning: Database is not up to date!"
   Click on "Fix" button at top of page
   -> Got a bunch of warnings, "Failed deleting xxx.xx"
6.4 Try again, this time be sure to fix permissions
6.4.1 Restore db:
   Command:
```
rs -d 2016_10_31 jm 01-before_upgrading_3.6.2_to_3.6.4
```
6.4.2 Restore code:

Commands:

```
cd ..
l
mv joomoowebsites.com joomoowebsites.com-manual_upgrade_gave_warnings
git clone git@github.com:tomwhartung/joomoowebsites.com.git
cp gitignored/configuration.php joomoowebsites.com 
cp ../downloads/Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz joomoowebsites.com
cd joomoowebsites.com
tar -xvzf Joomla_3.6.x_to_3.6.4-Stable-Patch_Package.tar.gz 
```

6.4.3 Fix permissions and verify they are ok

Command:

```
gojmj
fix_permissions.sh
```
   Relogin to admin panel -> System -> System Information -> File permissions
      Verify all are writable

6.4.4 Check for changes needed for database:
   Extensions -> Manage -> Database
      "Warning: Database is not up to date!"
   Click on "Fix" button at top of page
   +++ STILL got a bunch of "Failed deleting" warnings +++
   +++ Guess we will have to live with the cruft!?!?!? +++
   To see the warnings we got, see ../details/2016_11_01-upgrading-3_6_2-3_6_4.txt
   -> Moving on!
   System -> System Information
      Joomla Version: 3.6.4
   -> Still a whole lot easier and quicker ( < 1 hr.!) than trying to use the back end!!!

6.5 Commit the code, backup the database, backup the backup, and fix the link

Commands:

```
gojmj
git add --all
git status
git commit -m 'Upgraded to 3.6.4.'
git push origin master
bu jm 02-after_upgrading_3.6.2_to_3.6.4
tarHome
diff configuration.php ../gitignored/configuration.php 
rm configuration.php ; ln -s ../gitignored/configuration.php .
```

Upgrading New Production host:
------------------------------
New production host (server) is barbara.
1. Backup current DB and restore final copy of DB from jane:
   bu jm  01-before_upgrading_3.5.1_to_3.6.2          # IF NOT DONE ALREADY, DO IT NOW
   rs -h jane -d 2016_08_29 jm 03-after_upgrading_3.6.0_to_3.6.2
2. Pull the code and fix the permissions
   gojmj
   git pull
   fix_permissions.sh  # Does checking this file in pose a security risk?  I don't see how, but...
3. Ensure configuration.php matches that on jane:
   gojmj
   cd ../gitignored/
   diffJane configuration.php
4. Test in browswer
   Test front end in browser
   - Check a few menu options
   - Check articles with images
   Test back end in browser
   - System -> System Information -> System Information (check Joomla version)
   - System -> System Information -> Folder Permissions (Unwritable configuration.php is ok)
   - Extensions -> Manage -> Database (check schema version)
5. Backup DB and we are done:
   bu j  02-after_upgrade

