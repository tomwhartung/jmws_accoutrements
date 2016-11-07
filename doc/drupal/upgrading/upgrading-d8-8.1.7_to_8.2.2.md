
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

### 3.0 Try Using Drush Next Time

This is where we can supposedly update the site using drush.
After the drush install failed to go as hoped
(for details, see doc/ubuntu/specific_hosts/2016-jane-2/2-lamp_server-virtual_hosts.txt in this repo),
I am mildly suspicious as to whether this will work.

Presumably we can do all this with one command:

```
composer update
drush pm-update drupal
```

Maybe next time re-check out drush docs, find out what they or I or both of us did wrong.
(At this time I am in no mood to be trying to fix others' docs or code or both.)

**I would definitely feel more comfortable with trying that if we were updating to each new release one at a time,
instead of upgrading through several, as we have been doing.**

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

#### 3.1.3 Cleanup

Clean up the new code source directory to enable easy file name completion in the shell"

```
gothh
cd drupal-8.2.2
ls -al
ls -al modules/
rm modules/README.txt
rmdir modules/
ls -al profiles/
rm profiles/README.txt
rmdir profiles/
ls -al themes/
rm themes/README.txt
rmdir themes/
ls -al
```

The only thing remaining should be the sites directory.

### 3.2 Migrate any changes made to the `sites/*` and `sites/default/*` files

At this point in time this part of the process is a bit difficult to codify into specific steps.
It boils down to seeing what, if anything, has changed in the `sites/development.services.yml` and `sites/default/*settings*` files.

**It is hoped that we will begin to update this code more regularly, so we are more familiar and comfortable with all this,
we feel it is safe to use drush, have more confidence in and knowledge about the process, etc.**

#### 3.2.1 Migrate any changes made to the `sites/development.services.yml` file

Most of these files should be kept locally only (i.e., not in git), in the gitignored directory (and versioned in RCS).

Run `ls` and `diff` commands to compare:

* the current production version of `sites/development.services.yml` (linked to the `gitignored` directory) to the
* the newly released version in `drupal-8.2.2/sites`

```
gothh
ls -al gitignored/sites drupal-8.2.2/sites
ls -al gitignored/sites/development.services.yml drupal-8.2.2/sites/development.services.yml
diff gitignored/sites/development.services.yml drupal-8.2.2/sites/development.services.yml
```

##### 3.2.1.1 Updating the "sites/development.services.yml" file

Output from the `diff` commands reveals we have made changes to this file, and it did not change in the current release, so
we need to do the following:

- [X] Use the gitignored version of `sites/development.services.yml`

In other words, no changes are needed for this file.

##### 3.2.1.2 Link `gitignored/sites/development.services.yml` into the updated site code

Link our updated `development.services.yml` file into the new `tomhartung.com-d8.2.2/sites` directory tree.

```
gothh
cd tomhartung.com-d8.2.2/sites
ln -s ../../gitignored/sites/development.services.yml .
```

#### 3.2.2 Migrate any changes made to the `sites/default/default.services.yml` file to `services.yml`

These files should **definitely** be kept locally only, in the gitignored directory (versioned in RCS).

Run `ls` and `diff` commands to compare:

* the current production version of `sites/default/default.services.yml` (linked to the `gitignored` directory) to the
* the newly released version, `drupal-8.2.2/sites/default/default.services.yml`

```
gothh
ls -al gitignored/sites/default drupal-8.2.2/sites/default
ls -al gitignored/sites/default/default.services.yml drupal-8.2.2/sites/default/default.services.yml
diff   gitignored/sites/default/default.services.yml drupal-8.2.2/sites/default/default.services.yml
```

##### 3.2.2.1 Updating the `sites/default/default.services.yml` and `services.yml` files

Output from the `diff` commands reveals that changes have been made in the new release to `sites/default/default.services.yml` , so
we need to do the following:

- [X] Merge the differences between `gitignored/sites/default/default.services.yml` and `drupal-8.2.2/sites/default/default.services.yml`
into **`services.yml`**
- [X] Copy the new version of `default.services.yml` from `drupal-8.2.2/sites/default` to `gitignored/sites/default/default.services.yml`

```
ls -al gitignored/sites/default drupal-8.2.2/sites/default
cd gitignored/sites/default/
rd services.yml
vi services.yml
diff default.services.yml services.yml
cp ../../../drupal-8.2.2/sites/default/default.services.yml .
diff default.services.yml services.yml
rd services.yml default.services.yml
ci -l  services.yml default.services.yml     ## "Updated for drupal 8.2.2"
```


##### 3.2.2.2 Checking the `sites/default/default.services.yml` and `services.yml` files

Ensure that these files match, except for the changes ("CusTOMizations") we have made to them:

```
gothh
diff gitignored/sites/default/default.services.yml gitignored/sites/default/services.yml
```

##### 3.2.2.3 Link `gitignored/sites/default/services.yml` into the updated site code

Link our updated `services.yml` file into the new `tomhartung.com-d8.2.2/sites` directory tree.

```
gothh
cd tomhartung.com-d8.2.2/sites
mkdir default
cd default
ln -s ../../../gitignored/sites/default/services.yml .
```

#### 3.2.3 Migrate any changes made to the `sites/default/default.settings.php` file to `settings.php`

These files should **definitely** be kept locally only, in the gitignored directory (versioned in RCS).

Run `ls` and `diff` commands to compare:

* the production version of `sites/default/default.settings.php` (linked to the `gitignored` directory) to the
* the newly released version, `drupal-8.2.2/sites/default/default.settings.php`

```
gothh
ls -al gitignored/sites/default/default.settings.php drupal-8.2.2/sites/default/default.settings.php
diff   gitignored/sites/default/default.settings.php drupal-8.2.2/sites/default/default.settings.php
```

##### 3.2.3.1 Updating the `sites/default/*settings.php` files

Output from the `diff` commands reveals that changes have been made in the new release to `sites/default/default.settings.php`, so
we need to do the following:

- [X] Merge the differences between `gitignored/sites/default/default.settings.php` and `drupal-8.2.2/sites/default/default.settings.php`
into **`settings.php`**
- [X] Copy the new version of `default.settings.php` from `drupal-8.2.2/sites/default` to `gitignored/sites/default/default.settings.php`

```
cd gitignored/sites/default/
vi settings.php
cp ../../../drupal-8.2.2/sites/default/default.settings.php .
rd default.settings.php
diff default.settings.php settings.php
rd default.settings.php settings.php
ci -l default.settings.php settings.php
```

##### 3.2.3.2 Check the `sites/default/default.settings.php` and `settings.php` files

Ensure that these files match, except for the changes we have made to them:

```
gothh
diff gitignored/sites/default/default.settings.php gitignored/sites/default/settings.php
```

##### 3.2.3.3 Link `gitignored/sites/default/settings.php` into the updated site code

Link our updated `settings.php` file into the new `tomhartung.com-d8.2.2/sites` directory tree.

```
gothh
cd tomhartung.com-d8.2.2/sites/default  ## Directory was created in the last step!
ln -s ../../../gitignored/sites/default/settings.php .
```

#### 3.2.4 Link `settings.local*` files and the `files` directory into the updated site code

Link in the other files and the `files` directory, that we keep on the localhost.

```
gothh
cd tomhartung.com-d8.2.2/sites/default
ln -s ../../../gitignored/sites/default/settings.local* .
ln -s ../../../gitignored/sites/default/files .
ls -al
```

#### 3.2.5 Migrate any changes made to "sites/example.*" files (???)

I am not sure whether we need to be concerned about changes to these files, but
I feel it's worth taking a moment to look for changes anyway.

Run `ls` and `diff` commands to compare:

* the old versions of files matching the pattern `tomhartung.com/sites/example.*` to
* the newly released versions in `drupal-8.2.2/sites`

```
gothh
ls -al gitignored/sites drupal-8.2.2/sites
ls -al tomhartung.com/sites/example.settings.local.php drupal-8.2.2/sites/example.settings.local.php
diff tomhartung.com/sites/example.settings.local.php drupal-8.2.2/sites/example.settings.local.php
ls -al tomhartung.com/sites/example.sites.php  drupal-8.2.2/sites/example.sites.php
diff tomhartung.com/sites/example.sites.php  drupal-8.2.2/sites/example.sites.php
```

##### 3.2.5.1 Updating the "sites/example.*" files

No changes need to be made to these files in this release.

### 3.2.6 Summary:

Following is a list of important files to note:

```
sites/development.services.yml
sites/default/default.services.yml
sites/default/default.settings.php
sites/default/settings.local.php   ## Not in new releases, so there is NO need to merge it.
sites/example.settings.php         ## Unsure of this file's importance, best to play it safe
sites/example.sites.php            ## Unsure of this file's importance, best to play it safe
```

#### 3.2.6.1 Changes made to `settings.php`

Following is a list of the changes that need to be ported into the new settings.php :

- hash_salt - supply value
- uncomment code to include settings.local.php
- cusTOMizations comment
- settings for trusted host patterns
- ye olde database config settings
- install_profile and config_directories settings

**Can we not migrate these changes to `settings.local.php` , and forget about them?

#### 3.2.6.2 A Final Word of Caution:

The name of the `settings.local.php` file may be changing (in 8.2 - NOT!!!) to `local.settings.php` .
References (bug/feature reports):

* https://www.drupal.org/node/2419213
* https://www.drupal.org/node/1118520

I am not sure whether we need to worry about this, but maybe this is checked for elsewhere in the code?!?

### 3.3 Link in the customizations

Link in the customizations that we worked so hard on earlier this year.

```
gothh
cd tomhartung.com-d8.2.2
cd modules/
mkdir jmws
cd jmws/
l ../../../customizations/*/modules/jmws
ln -s ../../../customizations/jmws_idMyGadget_for_drupal-d8/modules/jmws/idmygadget .
cd ../../themes/
mkdir jmws
cd -
l ../../customizations/*/modules/jmws  # these are the customized modules that are available
cd -
l ../../customizations/*/themes/jmws   # these are the customized themes that are available
cd jmws/
l ../../../customizations/*/themes/jmws
ln -s ../../../customizations/jmws_drupal_idMyGadget_stark-d8/themes/jmws/idmygadget_stark .
ln -s ../../../customizations/jmws_drupal_idMyGadget_bartik-d8/themes/jmws/idmygadget_bartik .
```

### 3.3.1 Check the links

Compare to the links in the current directory tree, to make sure we didn't miss anything.

```
gothh
l tomhartung.com/modules/jmws/ tomhartung.com/themes/jmws/
l tomhartung.com-d8.2.2/modules/jmws/ tomhartung.com-d8.2.2/themes/jmws/
```

### 3.4 Optional: Clear caches and backup DB for safety

Ok this is the paranoia will destroy ya part!

But seriously, I have had issues with trying to restore backups and clear caches etc., so
I am thinking it is better to have too many of these backups than not enough.

```
bu th 02-before_updating_8_1_7_to_8_2_2
# Admin -> Configuration -> (Development section) Performance -> Clear All Caches
bu th 03-before_updating-caches_cleared_in_backend
gothh
cd gitignored/sites/default/
tar -cvzf files-03-before_updating-caches_cleared_in_backend.tgz files/
gotht
drush cr
bu th 04-before_updating-all_caches_cleared
gothh
cd gitignored/sites/default/
tar -cvzf files-04-before_updating-all_caches_cleared.tgz files/
```

This step is optional but if you skip it you might jinx it!!  ;-)

### 3.5 Switch the link and run lnSubsites.py

Time to give it a try!

```
gothh
rm tomhartung.com
ln -s tomhartung.com-d8.2.2 tomhartung.com
ls -al            # check link to main site
lnSubsites.py
ls -al tomhartung.com/               # check links
ls -al tomhartung.com/modules/jmws   # check links
ls -al tomhartung.com/themes/jmws    # check links
```

### 3.6 Run `update.php`

Access the following link to update the db as necessary:

* http://jane.tomhartung.com/update.php

Ran 11 updates and returned the following message:

* **comment module**
* - Update #8200
* - entity displays updated: node.article.default, node.article.default, node.page.default.

#### 3.6.1 Review log

Access the following link to check for db update errors:

* http://jane.tomhartung.com/admin/reports/dblog

#### 3.6.2 Take site out of maintenance mode

Run this command:

```
drush sset system.maintenance_mode 0
```

Or use the admin option Configuration -> Development -> Performance -> Maintenance Mode

#### 3.6.3 Check the site

If able to access site, backup immediately!  Paranoia will destroy ya!

```
bu th 05-after_updating_8_1_7_to_8_2_2
gothh
cd gitignored/sites/default/
tar -cvzf files-05-after_updating_8_1_7_to_8_2_2.tgz files/
```

#### 3.6.4 Optional: take more backups

We really do not need all of these backups...!
(What we need is more confidence in the process.)

```
# Admin -> Configuration -> (Development section) Performance -> Clear All Caches
bu th 06-after_updating-caches_cleared_in_backend
gothh
cd gitignored/sites/default/
tar -cvzf files-06-after_updating-caches_cleared_in_backend.tgz files/
gotht
drush cr
bu th 07-after_updating-all_caches_cleared
gothh
cd gitignored/sites/default/
tar -cvzf files-07-after_updating-all_caches_cleared.tgz files/
tarHome
```

Paranoia will destroy ya!

#### 3.6.5 Test, and commit and backup

If the site looks OK, commit code and backup db:

```
gothd
git status
git add --all
git commit -m 'Upgraded to the new release, 8.2.2 .' ; gpom
git status
```

## Step (4) Update the Backup Host (barbara)

[X] barbara

Formerly we would update the development host the copy the code and db to the other hosts, as we like to do with joomla.
This is a good technique to use if we get hacked and want to start fresh with a "new" db.

This time let's update the code on barbara and run update.php to update the db, as we like to do with wordpress.

### 4.1 Overview of process:

1. Clear cache and backup db on barbara
2. git pull updated code base and customizations (checked in from jane)
3. Copy updated gitignored files from jane
4. Run update.php to update the db on barbara
5. Test

### 4.2 Backup db and pull new code

Use these admin options to clear the cache:

* Admin -> Configuration -> Development -> Clear All Caches

Run these commands **on barbara** to backup the database and pull the new code base:

```
bu th 02-before_updating_8_1_7_to_8_2_2
gothh
cd gitignored/sites/default
tar -cvzf files-02-before_updating-caches_cleared_in_backend.tgz files/
gotht
git pull
```

Note that we should already have a backup from Step (1) above, so this one's kind of redundant, "just in case."

### 4.3. Copy updated gitignored files from jane

Run these commands **on jane** to copy the new files over to barbara.

```
gothh      ## ON JANE!!
cd gitignored/sites/
diffBarbara development.services.yml   ## no changes
cd default/
diffBarbara default.se*                ## should see the changes made upgrading to new release
toBarbara default.se*
diffBarbara services.yml               ## should see the changes we made above
toBarbara services.yml
diffBarbara settings.php               ## should see the changes we made above
toBarbara settings.php
diffBarbara settings.local.php*        ## no changes
```

We run diff commands to be sure we don't accidentally overwrite any local changes we have made.

### 4.4 Run `update.php`

Access the following link to update the db:

* http://barbara.tomhartung.com/update.php

Applied 11 pending updates, and got the message same as we got on jane.

### 4.5 Test and if it looks good, back up the db

Check that the site loads and that Admin -> Reports -> Available Updates shows we are running the new version.

```
bu th 03-upgraded_8_1_7_to_8_2_2
```

### 4.6 Clear caches and backup again, just in case

Clear all caches in admin panel, then run these commands:

```
bu th 04-upgraded_8_1_7_to_8_2_2-cleared_caches
gothh
cd gitignored/sites/default
tar -cvzf files-04-upgraded_8_1_7_to_8_2_2-cleared_caches.tgz files/
tarHome
```

## Step (5) Update the Production Host (ava)

[ ] ava

### 5.1 Process

Follow same process as we did for barbara, except that on ava:

* **be sure to put the site in maintenance mode first!!**

### 5.2 Backup db and pull new code

Clear all caches in admin panel, then run these commands:

```
bu th 02-before_updating_8_1_7_to_8_2_2
gothh
cd gitignored/sites/default
tar -cvzf files-02-before_updating-caches_cleared_in_backend.tgz files/
gotht
git pull
```

Note that we should already have a backup from Step (1) above, so this one's kind of redundant, "just in case."

### 5.3. Copy updated gitignored files from jane

Run these commands **on jane** to copy the new files over to barbara.

```
gothh      ## ON JANE!!
cd gitignored/sites/
diffAva development.services.yml   ## no changes
cd default/
diffAva default.se*                ## should see the changes made upgrading to new release
toAva default.se*
diffAva services.yml               ## should see the changes we made above
toAva services.yml
diffAva settings.php               ## should see the changes we made above
toAva settings.php
diffAva settings.local.php*        ## no changes
```

We run diff commands to be sure we don't accidentally overwrite any local changes we have made.

### 5.4 Run `update.php`

Access the following link to update the db:

* http://ava.tomhartung.com/update.php

Applied 11 pending updates, and got the message same as we got on jane.

### 5.5 Test and if it looks good, back up the db

Check that the site loads and that Admin -> Reports -> Available Updates shows we are running the new version.

```
bu th 03-upgraded_8_1_7_to_8_2_2
gothh
cd gitignored/sites/default
tar -cvzf files-03-upgraded_8_1_7_to_8_2_2.tgz files/
tarHome
```

### 5.6 Clear caches and backup again, just in case

Clear all caches in admin panel, then run these commands:

```
bu th 04-upgraded_8_1_7_to_8_2_2-cleared_caches
gothh
cd gitignored/sites/default
tar -cvzf files-04-upgraded_8_1_7_to_8_2_2-cleared_caches.tgz files/
tarHome
```

