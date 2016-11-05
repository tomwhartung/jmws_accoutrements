
# Upgrading Drupal 8.1.7 to 8.2.2

## Purpose

The purpose of this document is to detail a process we can use without doing a lot of preparatory research.

## Lessons Learned

Observations and lessons learned from previous experience with upgrading drupal:

* Use drush, it makes the process much quicker

* Be sure to reference documentation for version 8 of Drupal, NOT version 7

* The standard procedure is to follow the instructions in the copy of UPGRADE.TXT that comes with the source

We are going to start using drush to do this!

## References

**Reviewing all of these references is NOT necessary.**

### The Original Reference

This one has links to other references:

* https://www.drupal.org/node/1494290

Drupal 8 Reference:

* https://www.drupal.org/docs/8/update/update-procedure-in-drupal-8

### List of All Releases

**Absolutely always check this out!**

* **https://www.drupal.org/project/drupal/releases

I actually found out **on this page** they had just released 8.2.2 while I was in the process of upgrading to 8.2.1,
so be sure to check it!

### Release Notes

Release notes for each release:

* **https://www.drupal.org/project/drupal**

**Check the release notes for every version missed, as well as for the current, latest version.**

**Search the page for `'settings'` to see whether there are changes required to settings.php .**

Following is an example of a release notes page that mentions updates to .htaccess, web.config, and settings files:

* https://www.drupal.org/project/drupal/releases/8.1.7

Note that they make it very obvious.

### More References

To use drush or to not use drush?
The answer looks rather obvious to me right now....

#### Using Drush

In addition to allowing us to do it on the command line, using drush to update the core looks like it is very easy.

* https://www.drupal.org/node/2550801 - Update using drush

* http://www.drush.org/en/master/ - drush docs

For steps to install drush, see the most recent of the files with names matching the pattern
`doc/ubuntu/specific_hosts/2016-*/2-lamp_server-virtual_hosts.txt` in this repo.

#### Hybrid Drush/Manual Method

**This just in!**

* https://drupal.org/node/2700999

It is concise, covers both how to do it manually and use drush, and was literally just updated this week!

#### Manual methods:

Of course previous versions of this file in this directory contain many details about previous efforts - hence our interest in drush!

##### UPGRADING.txt

For safety, review the UPGRADING.txt file that comes with the distribution as it may contain last-minute information.

* https://api.drupal.org/api/drupal/core!UPGRADE.txt/8.0.x - UPGRADE.TXT

This looks to be mostly boilerplate, though.

##### Very Manual Method:

This looks very much like what we have been doing:

* https://www.drupal.org/node/570162

##### The D7 Manual Method - With Links

Another, similar (but less complicated - and perhaps less safe) process:

* https://www.drupal.org/node/1494290

Note though that it has links to:

* The D8 method mentioned above at https://www.drupal.org/node/2700999 - updated just this week!

* How to use drush at https://www.drupal.org/node/2550801 - let's give that a try!

* How to update using a patch file at https://www.drupal.org/node/359234 - save that for later!

See what I mean about there being a lot of references?!?
I find confidence in their similarities, though, and want to distill an efficient drush/command-line version from all of these.

## Preparation

There are so many references!  Let's try to focus here people!

### Review Release Notes

When we have missed one or more upgrades, we need to review the release notes for each missed release.

* Release notes: https://www.drupal.org/project/drupal/releases

Review what has changed, specifically determine whether settings.php or other important files need to be updated.

### Review References to Processes:

We are working on simplifying the process used.

* D8 Hybrid Process: https://www.drupal.org/node/2700999
* Using drush: https://www.drupal.org/node/2550801

Specifically we are very interested in using drush.

### Check Drush Version Compatibility

For drupal 8 we need version 8 or higher of drush.

For jane, we have set up an alias; for more information see the file (in this repo) named
`doc/ubuntu/specific_hosts/2016-jane-2/2-lamp_server-virtual_hosts.txt` .

## Step (1) Backup the Old

Do this on all hosts:

- [x] jane
- [x] barbara
- [x] ava

Ensure the code on all hosts matches what is in git:

```
gotht       # cd var/www/tomhartung.com/htdocs/tomhartung.com
git status
git pull
```

Reconcile any differences as appropriate.

Clear the caches and backup the database on all hosts:

```
drush cr    # or Admin -> Configuration -> Development -> Performance -> Clear All Caches
bu th 01-before_upgrading_8_1_7_to_8_2_2
```

If unable to use drush, use Admin -> Configuration -> Development -> Performance -> Clear All Caches .

## Step (2) Download, Unpack, and Review the New

Do this on the development host only:

- [x] jane

Use the links on the admin panel or find the file(s) on drupal.org .

* Admin -> Reports -> Available Updates

See the Release notes or just use the download link.

Download (or copy) the file(s) into `/var/www/tomhartung.com/downloads` and unpack the tar file into the `../unpack` directory:

```
cd /var/www/tomhartung.com/downloads
mkdir ../unpack
cp  drupal-8.2.2.tar.gz ../unpack
cd ../unpack
tar -xvzf drupal-8.2.2.tar.gz
rm drupal-8.2.2.tar.gz
cd ../drupal-8.2.2/
```

### **THE CURRENT QUESTION WE WANT TO ANSWER**

Following is a list of all pertinent releases since 8.1.7:

* 8.1.8 - https://www.drupal.org/project/drupal/releases/8.1.8
* 8.1.9 - https://www.drupal.org/project/drupal/releases/8.1.9
* 8.1.10 - https://www.drupal.org/project/drupal/releases/8.1.10
* 8.2.0 - https://www.drupal.org/project/drupal/releases/8.2.0
* 8.2.1 - https://www.drupal.org/project/drupal/releases/8.2.1
* 8.2.2 - https://www.drupal.org/project/drupal/releases/8.2.2

The admin panel lists two releases, 8.1.10 and 8.2.2.

* See Reports -> Available Updates

#### THE QUESTION

**Do I need to process both, or can I just process the one for 8.2.2 ??**

I believe we can skip to 8.2.2 .

I also believe it is important to check all the release notes for updates to files like `settings.php` , etc.

### Results of reviewing all the release notes:

Not seeing anything about updates to the DB or settings.

I want to try skipping going straight to 8.2.2.

## Step (3) Update the Development Host (jane)

Use drush or the **Configuration -> (Development section) Maintenance mode** admin option to put the site into maintenance mode:

```
gotht
drush sset system.maintenance_mode 1
```

### 3.1 Update Drupal Core

Grab fresh clone of site, and replace the core and vendor directories.

#### 3.1.1 Delete the Old Files

```
gothh
cd tmp
git clone git@github.com:tomwhartung/tomhartung.com-d8.git
mv tomhartung.com-d8 tomhartung.com-d8.2.2
mv tomhartung.com-d8.2.2 ..
cd ../tomhartung.com-d8.2.2
rm -fr core vendor
## rm autoload.php composer.* example.gitignore index.php LICENSE.txt
## rm README.txt robots.txt update.php web.config
## rm .csslintrc .editorconfig .eslint* .gitattributes  .htaccess
mv autoload.php composer.* example.gitignore index.php LICENSE.txt ../tmp
mv README.txt robots.txt update.php web.config ../tmp
mv .csslintrc .editorconfig .eslint* .gitattributes  .htaccess ../tmp
```

#### 3.1.2 Add in the New Files

Replace deleted files with the corresponding files from the new release.

Be careful to not overwrite any customizations made to any of the following files!

* `.htaccess`
* `composer.json`
* `robots.txt`
* (etc.)

If desired, you can run git log on these to ensure they have not been changed.
If they have changed, migrate the changes I have made from old to new, or
migrate the changes they made from new to old to make newer.

```
gothh
cp ../downloads/drupal-8.2.2.tar.gz .
tar -xvzf drupal-8.2.2.tar.gz
rm drupal-8.2.2.tar.gz
cd drupal-8.2.2
mv core vendor ../tomhartung.com-d8.2.2
mv autoload.php composer.* example.gitignore index.php LICENSE.txt ../tomhartung.com-d8.2.2
mv README.txt robots.txt update.php web.config ../tomhartung.com-d8.2.2
mv .csslintrc .editorconfig .eslint* .gitattributes  .htaccess ../tomhartung.com-d8.2.2
```


********************
*** You are here ***
********************


#### 3.1.3 Reconcile any changes made to "*settings*" files

At this point in time this part of the process is a bit difficult to codify into specific steps.
It boils down to seeing what, if anything, has changed in *settings* files under the "sites/" directory
Most of these files should be kept locally only, in the gitignored directory (versioned in RCS)

```
   gothh
```

   Run ls and diff commands from this directory to compare:
      old production files under tomhartung.com/sites to the
      newly released versions under drupal-8.1.7/sites ,
      many of which are linked to files in gitignored/sites

Important files of note:
```
      sites/development.services.yml
      sites/example.settings.php
         New setting:
            $settings['skip_permissions_hardening'] = TRUE;
         Moved over to new version of code
      sites/example.sites.php
      sites/default/default.services.yml
      sites/default/default.settings.php
         Many changes (but not seeing any mentioned in the Release notes?)
      sites/default/settings.local.php
         Included by settings.php (at the very end)
         Not in new releases, so there is NO need to merge it.
      ** Name may be changing in 8.2 to local.settings.php
      ** (apparently this is checked for elsewhere in the code?!?)
      ** References (bug/feature reports):
      **    https://www.drupal.org/node/2419213
      **    https://www.drupal.org/node/1118520
```

6.1 Process for updating sites/default/services.yml when there are new settings:
   gothh
   diff drupal-8.1.7/sites/default/default.services.yml  gitignored/sites/default/default.services.yml
   ###
   ### Notes:
   ###    Currently the version we are using on the dev host differs from that used in production (debug setting)
   ###    No changes need to be made to this file for this upgrade
   ###
6.2 Process for updating sites/default/settings.php when there are new settings:
   gothh
   diff drupal-8.1.7/sites/default/default.settings.php gitignored/sites/default/default.settings.php
   ###
   ### See what changes have been made that I need to migrate to the new settings file
   ###    (which also contains my secret db info and other customizations).
   ### Migrate these changes into the copies of these files that we are using as necessary
   ### Note that the copies of these files that we are using are under htdocs/gitignored/sites/default
   ###
   gothh
   cd gitignored/sites/default
   rd default.settings.php    ## Ensure it is up to date in RCS
   diffBarbara settings*      ## Ensure these files match what is on the new server
   diffJane settings*         ## Ensure these files match what is on the new development host
   diffLauren settings*       ## Ensure any changes on the production host are desired there only
   ###
   ### If any of these files do not match what is on the other hosts
   ### OR
   ### If any of these files do not match what is in RCS on the corresponding local host
   ###   We need to justify why the difference exists or make sure the files match
   ###
6.3 Choose your process:
XXX Option 1) Identify changes made between:
XXX    gitignored/sites/default/default.settings.php and
XXX    gitignored/sites/default/settings.php
XXX and make those changes to the new default.settings.php file to get a new settings.php file
XXX OR
XXX Option 2) Identify changes made between:
XXX    gitignored/sites/default/default.settings.php and
XXX    drupal-8.1.7/sites/default/default.settings.php
XXX and make those to the old settings.php file to get a new settings.php file
XXX OR
    Option 3) as Step 3 of the process in UPDATE.txt recommends:
       Save the version of settings.php currently in production as settings.php-old
       [Also save the version of default.settings.php currently in production as default.settings.php-old]
       Copy the new default.settings.php to settings.php
       Identify the changes made to default.settings.php-old to get what is now settings.php-old
       Apply those changes to the new default.settings.php to get the new settings.php
6.4 Proceeding with Option 3 - details
   gothh
   cd gitignored/sites/default
   cp default.settings.php default.settings.php-old
   cp settings.php settings.php-old
   cd -
   cp drupal-8.1.7/sites/default/default.settings.php gitignored/sites/default/default.settings.php
   cd -
   diff default.settings.php-old settings.php-old      # 54 lines changed: migrate changes to new settings.php
   diff default.settings.php-old default.settings.php  # 104 lines changed: hence the preference for option 3 (ymmv next time!)
   cp default.settings.php settings.php
   vi settings.php
   ###
   ### Manually apply these changes, that were made
   ###    to default.settings.php-old to get settings.php-old
   ### To the current settings.php (which matches the current default.settings.php)
   ###    to get the new settings.php
   ###
   ### Following is a list of changes that need to be ported into the new settings.php :
   ###
   - hash_salt - supply value
   - uncomment code to include settings.local.php
   - cusTOMizations comment
   - settings for trusted host patterns
   - ye olde database config settings
   - install_profile and config_directories settings
7. Update new release tree with links to my gitignored files
   gothh
   cd tomhartung.com-d8.1.7
   cd sites
   rm development.services.yml       # (if necessary)
   ln -s ../../gitignored/sites/development.services.yml .
   mkdir default                     # (if necessary)
   cd default
   l ../../../gitignored/sites/default
7.1 Optional: double-check for changes if you like!  Paranoia will destroy ya!!
   diff ../../../drupal-8.1.7/sites/default/default.services.yml default.services.yml
   diff ../../../drupal-8.1.7/sites/default/default.settings.php default.settings.php
7.2 Link all of the sites/default/* files into the current directory tree
   rm default.se*      # (if necessary)
   ln -s ../../../gitignored/sites/default/*.* .
   ln -s ../../../gitignored/sites/default/files .
   rm *-old
7.3 Link in the customizations
   gothh
   cd tomhartung.com-d8.1.7
   cd modules/
   mkdir jmws
   cd ../themes/
   mkdir jmws
   cd -
   l ../../customizations/*/modules/jmws  # these are the customized modules that are available
   cd -
   l ../../customizations/*/themes/jmws   # these are the customized themes that are available
   cd jmws/
   l ../../../customizations/*/themes/jmws
   ln -s ../../../customizations/jmws_drupal_idMyGadget_stark-d8/themes/jmws/idmygadget_stark .
   ln -s ../../../customizations/jmws_drupal_idMyGadget_bartik-d8/themes/jmws/idmygadget_bartik .
   cd ../../modules/jmws/
   l ../../../customizations/*/modules/jmws
   ln -s ../../../customizations/jmws_idMyGadget_for_drupal-d8/modules/jmws/idmygadget .
   ###
   ### Check: compare to the links in the current directory tree:
   ###
   gothh
   l tomhartung.com/modules/jmws/ tomhartung.com/themes/jmws/
   l tomhartung.com-d8.1.7/modules/jmws/ tomhartung.com-d8.1.7/themes/jmws/
7.4 Clear caches and backup DB for good measure
   ### Ok I have had issues with trying to restore backups and clear caches etc. so
   ### I am thinking it is better to have too many of these than not enough
   bu th 01-before_updating_8.0.3-8.1.7
   # Admin -> Configuration -> (Development section) Performance -> Clear All Caches
   bu th 02-before_updating-caches_cleared_in_backend
   gothh
   cd gitignored/sites/default/
   tar -cvzf files-02-before_updating-caches_cleared_in_backend.tgz files/
   gotht
   drush cr
   bu th 03-before_updating-all_caches_cleared
   gothh
   cd gitignored/sites/default/
   tar -cvzf files-03-before_updating-all_caches_cleared.tgz files/
7.5 Switch the link and run lnSubsites.py
   gothh
   rm tomhartung.com ; ln -s tomhartung.com-d8.1.7 tomhartung.com
   l   # check link to main site
   lnSubsites.py
   l tomhartung.com/   # check links

8. Visit site to upgrade db as necessary:
   http://bette.tomhartung.com/update.php
   ##
   ## Note: there were 12 pending DB updates found when upgrading from 8.0.3 to 8.1.7
   ##
8.1 Review log for db update errors:
      http://bette.tomhartung.com/admin/reports/dblog
8.2 If able to access site, backup immediately!  Paranoia will destroy ya!
   bu th 04-after_updating_8.0.3-8.1.7
   gothh
   cd gitignored/sites/default/
   tar -cvzf files-04-after_updating_8.0.3-8.1.7.tgz files/
   # Admin -> Configuration -> (Development section) Performance -> Clear All Caches
   bu th 05-after_updating-caches_cleared_in_backend
   gothh
   cd gitignored/sites/default/
   tar -cvzf files-05-after_updating-caches_cleared_in_backend.tgz files/
   gotht
   drush cr
   bu th 06-after_updating-all_caches_cleared
   gothh
   cd gitignored/sites/default/
   tar -cvzf files-06-after_updating-all_caches_cleared.tgz files/
   tarHome
8.3 -> Test!!
9. If the site looks OK, commit code and backup db:
9.1. Commit and push code:
   gothd
   git status
   ga --all
   gc 'Upgraded to the new release, 8.1.7 .' ; gpom
   gs
9.2. Remove from maintenance mode and backup DB:
   As admin -> Configuration -> "Go online."
9.3 Check new settings files into RCS:
   gothh
   cd gitignored/sites
   rd RCS/*,v
   cd default
   mkdir old
   mv settings.php-old settings.php-d8.0.3
   mv default.settings.php-old default.settings.php-d8.0.3
   mv *-d8.0.3 old/
   rd RCS/*,v
   ci -l default.settings.php
   ci -l settings.php
   rd RCS/*,v

New Server!
-----------
[ ] barbara (not yet online!)

Currently these are the goals and concerns:
o  Use already-upgraded copy of db from bette (no extensions installed)
o  Use already-upgraded copy of code from bette (github)
o  ??? Test with idmygadget_bartik  ??? (concern copied from below)
o  ??? Test disabling cache  ??? (concern copied from below)

Process:
1. git pull updated code base and customizations (checked in from bette)
2. Copy gitignored files from bette
3. Backup current copy of db on bette
4. Resture bette's DB on barbara
5. Check and create links as necessary:
5.1 Main link to point to the new code
5.2 Links in the new code to gitignored files and customizations
??? 7. Link gitignored and subsites to the new code
8. Test

Commands:
1. Grab new code base
   gothh
   git clone git@github.com:tomwhartung/tomhartung.com-d8.git
   mv tomhartung.com-d8 tomhartung.com-d8.1.7
   ln -s tomhartung.com-d8.1.7 tomhartung.com
2. Link customizations
   gotht
   mkdir -p  modules/jmws themes/jmws
   cd modules/jmws/
   l ../../../customizations/jmws_idMyGadget_for_drupal-d8/modules/jmws/idmygadget/
   ln -s ../../../customizations/jmws_idMyGadget_for_drupal-d8/modules/jmws/idmygadget .
   cd ../../themes/jmws
   l ../../../customizations/jmws_drupal_idMyGadget_bartik-d8/themes/jmws/idmygadget_bartik/
   ln -s ../../../customizations/jmws_drupal_idMyGadget_bartik-d8/themes/jmws/idmygadget_bartik .
   l ../../../customizations/jmws_drupal_idMyGadget_stark-d8/themes/jmws/idmygadget_stark/
   ln -s ../../../customizations/jmws_drupal_idMyGadget_stark-d8/themes/jmws/idmygadget_stark .

   !!! Test to see if we need these !!!
   ??? # Currently we have some third party modules (for migration) plus my jmws one  ???
   !!! Test to see if we need these !!!
   ??? cd modules
   ??? cp -rp ../../tomhartung.com-d8.0.2/modules/*   .
   !!! Test to see if we need these !!!

3. Copy over db and gitignored files from bette to barbara
3.1 On bette:
   gobu
   bu th 07-for_barbara
   toBarbara tomhartung.d8-2016_07_25-bette-07-for_barbara.sql.gz
   gothh
   tar -cvzf gitignored-2016_07_25-for_barbara.tgz gitignored
   toBarbara gitignored-2016_07_25-for_barbara.tgz
3.2 On barbara:
   gothh
   tar -xvzf gitignored-2016_07_25-for_barbara.tgz
3.3 Create the links
   gotht
   cd sites
   ln -s ../../gitignored/sites/development.services.yml .
   mkdir default
   cd default
   ln -s ../../../gitignored/sites/default/*.* .
   ln -s ../../../gitignored/sites/default/files .
   gothh
   lnSubsites.py
3.3 Restore a copy of the upgraded DB from bette
   rs -h bette th 07-for_barbara
4. Test and if it looks good, back up the db!
   Check that site loads
   Check that Admin -> Reports shows we are running the new version.
   bu th 08-upgraded_to_8.1.7

Production Host:
----------------
[ ] ava

Follow same process as we did for barbara, re-using files when possible
1. Grab new code base
   gothh
   ln -s tomhartung.com-d8.1.7 tomhartung.com
   cd fresh_clone.tmp/
   git clone git@github.com:tomwhartung/tomhartung.com-d8.git
   mv tomhartung.com-d8 tomhartung.com-d8.1.7
   mv fresh_clone.tmp ..
2. Link customizations
   Follow commands run on barbara for step 2 (above).
3. Copy over db and gitignored files from bette to barbara
3.1 Reuse backup of db and gitignored tar file
   On bette:
   gobu
   toJane tomhartung.d8-2016_07_25-bette-07-for_barbara.sql.gz
   gothh
   toJane gitignored-2016_07_25-for_barbara.tgz
3.2 Restore backup of db and unpack gitignored tar file
   On jane:
   gothh
   mv gitignored gitignored-old-8.0.3-delete_me_you_wuss
   tar -xvzf gitignored-2016_07_25-for_barbara.tgz
3.3 Create the links
   Follow commands run on barbara for step 3,3 (above).
4. Test and if it looks good, back up the db!
   bu th 08-upgraded_to_8.1.7
   tarHome



