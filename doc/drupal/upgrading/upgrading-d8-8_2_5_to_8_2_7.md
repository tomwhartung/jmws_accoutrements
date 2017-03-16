
# Upgrading Drupal 8.2.5 to 8.2.7

## Purpose

Use drush to upgrade the site two minor releases.

## References

**For complete instructions on how to upgrade over several releases, see upgrading-d8-8.1.7_to_8.2.2.md**

Drupal 8 Reference:

* https://www.drupal.org/docs/8/update/update-procedure-in-drupal-8

Looks identical to:

* https://www.drupal.org/node/2700999

**Absolutely always check this out!**

* **https://www.drupal.org/project/drupal/releases**

Release notes for each release:

* **https://www.drupal.org/project/drupal**

**Search the page for `'settings'` to see whether there are changes required to settings.php .**

### Using Drush

In addition to allowing us to do it on the command line, using drush to update the core looks like it is very easy.

* https://www.drupal.org/node/2550801 - Update using drush, covers both Drupal 7 and Drupal 8

* http://www.drush.org/en/master/ - drush docs

For steps to install drush, see the most recent of the files with names matching the pattern
`doc/ubuntu/specific_hosts/2016-*/2-lamp_server-virtual_hosts.txt` in this repo.


## Step (0) - Review Release Notes and Process(es)

When we have missed one or more upgrades, we need to review the release notes for each missed release.

* Release notes: https://www.drupal.org/project/drupal/releases

Review what has changed, specifically determine whether settings.php or other important files need to be updated.

### Review References to Processes:

We are working on simplifying the process used.

* D8 Hybrid Process: https://www.drupal.org/node/2700999
* Using drush: https://www.drupal.org/node/2550801

For upgrading a single minor release we should be able to use drush.

### Check Drush Version Compatibility

For drupal 8 we need version 8 or higher of drush.

For jane, we have set up an alias; for more information see the file (in this repo) named
`doc/ubuntu/specific_hosts/2016-jane-2/2-lamp_server-virtual_hosts.txt` .

```
which drush               ## /usr/bin/drush
/usr/bin/drush --version  ## drush version 5.10.0
alias drush               ## alias drush='~/.config/composer/vendor/drush/drush/drush'
drush --version           ## Drush Version   :  8.1.7
```

On 2017-03-18 we got the following warning:

```
drush --version
## Directory /home/tomh/.drush/cache/default exists, but is not writable. Please check directory permissions.   [error]
##  Drush Version   :  8.1.7
```

and ran the following commands to correct this situation:

```
cd
l .drush/cache/default/
ll .drush/cache/default/
sudo chmod 777 .drush/cache/default/
sudo chmod 777 .drush/cache/default/5.10.0-commandfiles-0-c1a656412ed37d74bebf6ae174b009d8.cache
ll .drush/cache/default/
ll .drush/cache/
sudo chmod 777 .drush/cache/
ll .drush/cache/
```

Just hoping that works out ok!

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

* Admin -> Configuration -> Development -> Performance -> Clear All Caches

```
bu th 01-before_upgrading_8_2_5_to_8_2_7
```

## Step (2) Download, Unpack, and Review the New

Do this on the development host only:

- [x] jane

### Note!  Skipping this step!

**We are going to try using drush to update the site, so we are skipping to Step (3)!**

### NOT using drush? Then Download and Review

Use the links on the admin panel or find the file(s) on drupal.org .

* Admin -> Reports -> Available Updates

See the Release notes or just use the download link.

Download (or copy) the file(s) into `/var/www/tomhartung.com/downloads` and unpack the tar file into the `../unpack` directory:

```
cd /var/www/tomhartung.com/downloads
mkdir ../unpack
cp  drupal-8.2.7.tar.gz ../unpack
cd ../unpack
tar -xvzf drupal-8_2.7.tar.gz
rm drupal-8_2.7.tar.gz
cd ../drupal-8.2.7/
more core/CHANGELOG.txt
less core/UPDATE.txt
```

## Step (3) Update the Development Host (jane)

Reference for possible future reference - fairly extensive look at using drupal and composer:

- https://www.drupal.org/node/2718229

### 3.1 Put site in maintenance mode

Use drush or the **Configuration -> (Development section) Maintenance mode** admin option to put the site into maintenance mode:

```
gotht
drush sset system.maintenance_mode 1
```

### 3.2 Use Drush

This is a minor upgrade, and as far as I can tell, there are no changes to any of the settings files,
so we should be safe running this process.

From the release notes ( https://www.drupal.org/project/drupal/releases/8.2.7 ):

> "No changes have been made to the .htaccess, web.config, robots.txt or default settings.php files in this release,
>  so upgrading custom versions of those files is not necessary."

#### 3.2.1 `composer update`

Getting a count of the number of files changed after each of these commands can be "interesting."

As tomh:

```
gotht
composer update
gs | wc -l       ## **1088**
```

Output received this time:

```
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Removing zendframework/zend-hydrator (1.0.0)
  - Removing composer/installers (v1.0.21)
  - Installing composer/installers (v1.2.0)
    Downloading: 100%

> Drupal\Core\Composer\Composer::vendorTestCodeCleanup
  - Removing wikimedia/composer-merge-plugin (v1.3.1)
  - Installing wikimedia/composer-merge-plugin (v1.4.0)
    Downloading: 100%
. . .
. . .   ## everything looks good...
. . .
> Drupal\Core\Composer\Composer::vendorTestCodeCleanup
  - Installing phpunit/phpunit (4.8.35)
    Downloading: 100%

> Drupal\Core\Composer\Composer::vendorTestCodeCleanup
behat/mink suggests installing behat/mink-selenium2-driver (slow, but JS-enabled driver for any app (requires Selenium2))
behat/mink suggests installing behat/mink-zombie-driver (fast and JS-enabled headless driver for any app (requires node.js))
sebastian/global-state suggests installing ext-uopz (*)
phpunit/phpunit-mock-objects suggests installing ext-soap (*)
phpunit/php-code-coverage suggests installing ext-xdebug (>=2.2.1)
phpunit/phpunit suggests installing phpunit/php-invoker (~1.1)
Writing lock file
Generating autoload files
> Drupal\Core\Composer\Composer::preAutoloadDump
> Drupal\Core\Composer\Composer::ensureHtaccess
```


#### 3.2.2 `drush pm-update drupal`

Getting a count of the number of files changed after each of these commands can be "interesting."

As tomh:

```
drush pm-update drupal
gs | wc -l       ## **925**
```

Output received this time:

```
Update information last refreshed: Thu, 03/16/2017 - 12:19
 Name    Installed Version  Proposed version  Message
 Drupal  8.2.5              8.2.7             SECURITY UPDATE available


Code updates will be made to drupal core.
WARNING:  Updating core will discard any modifications made to Drupal core files, most noteworthy among these are .htaccess and robots.txt.  If you have made any modifications to these files, please back them up before updating so that you can re-create your modifications in the updated version of the file.
Note: Updating core can potentially break your site. It is NOT recommended to update production sites without prior testing.

Do you really want to continue? (y/n): y
Project drupal was updated successfully. Installed version is now 8.2.7.
Backups were saved into the directory /home/tomh/drush-backups/drpal8_tomhartung/20170316181941/drupal.  [ok]
The following updates are pending:

views module :
  8201 -   Rebuild cache to refresh the views config schema.

Do you wish to run all pending updates? (y/n): y
Performing views_update_8201                                                                             [ok]
Cache rebuild complete.                                                                                  [ok]
Finished performing updates.                                                                             [ok]
```

Note that this time the files-changed count output by `gs | wc -l` went down after the second command, from 1088 to 925.
"Interesting!"

### 3.3 Check:

Following is a list of important files to note:

```
sites/development.services.yml
sites/default/default.services.yml
sites/default/default.settings.php
sites/default/settings.local.php   ## Not in new releases, so there is NO need to merge it.
sites/example.settings.php         ## Unsure of this file's importance, best to play it safe
sites/example.sites.php            ## Unsure of this file's importance, best to play it safe
```

Based on the release notes, none of these has changed, but it's easy enough to verify that:

```
gotht
cd ../gitignored/
cd sites/
l
rd development.services.yml
cd default/
l
rd *.*
```

### 3.4 Put site back online and rebuild cache:

**Oops!  Forgot to put the site in maintenance mode this time!!**
**Good thing no one is able to access this host while I do stuff on it!!**

Hoping it will be ok.  ;-)

Using drush:

```
gotht
drush sset system.maintenance_mode 0
drush cr   ## Was unable to get this to work this time ...
```

**If the `drush cr` command doesn't work, try clearing the cache from within the admin panel.**

### 3.5 Test, and backup and commit code if ok

Check the version and clear the cache (again - to be safe!) in the admin panel:

* Admin -> Reports -> Available updates
* Admin -> Configuration -> Performance -> Clear all caches

If it's running the new version, and we are able to access site, and everything looks ok, backup the db:

```
bu th 02-after_updating_8_2_5_to_8_2_7
```

and commit the code:

```
gothd
git status
git add --all
git commit -m 'Upgraded to the new release, 8_2_7 .' ; gpom
git status
```

### 3.6 Backup the backups of the db (and everything else in /home/tomh)

```
tarHome
```

## Step (4) Update the Backup Host (barbara)

[X] barbara

Update the development host and copy the code and db to the other hosts (as we like to do with joomla).

### 4.0 Overview of process:

1. Clear cache and backup db on jane
2. Clear cache and backup db on barbara
3. Copy db from jane to barbara, and restore it on barbara
4. Pull updated code base (checked in from jane)
5. Test

### 4.1 Backup db on jane

Clear the cache on jane:

* Admin -> Configuration -> Development -> Clear All Caches

Backup the database on jane:

```
gotht
drush cr   ## I love to be safe!
bu th 03-cleared_cache_for_barbara_and_ava
```

### 4.2 Backup db on barbara

Use these admin options to clear the cache:

* Admin -> Configuration -> Development -> Clear All Caches

**There is no drush on barbara and ava!**

Run this command **on barbara** to backup the database:

```
bu th 02-before_restoring_from_jane
```

### 4.3 Restore jane's db on barbara and pull new code

Copy db **from jane** to barbara:

```
toBarbara tomhartung.d8-2017_03_16-jane-03-cleared_cache_for_barbara_and_ava
```

Restore jane's db **on barbara**:

```
rs -h jane -d 2017_03_16 th 03-cleared_cache_for_barbara_and_ava
```

### 4.4 Pull the code

Want to do this "more or less simultaneously," but ...

**DO NOT PULL CODE UNTIL THE COMMAND TO RESTORE THE DB FROM JANE RUNS SUCCESSFULLY!!**

```
gotht
git pull
```

### 4.5 Test and if it looks good, clear caches, backup the db, and backup the backup

Check that the site loads and shows we are running the new version:

* Admin -> Reports -> Available Updates

If it looks ok, clear all caches in admin panel, backup db, and backup the backup:

* Admin -> Configuration -> Development -> Clear All Caches

```
bu th 04-upgraded_8_2_5_to_8_2_7
tarHome
```

## Step (5) Update the Production Host (ava)

[ ] ava

### 5.0 Process

Follow same process as we did for barbara, except that on ava:

* **Be sure to put the site in maintenance mode first!!**

### 5.1 Copy db from jane to ava

Copy db **from jane** to ava:

```
gobu
toAva tomhartung.d8-2017_03_16-jane-03-cleared_cache_for_barbara_and_ava
```

### 5.2 Put in maintenance mode, clear caches, and backup db

Put in maintenance mode and clear caches:

* Admin -> Configuration -> (Development) Maintenance Mode -> Check the box
* Admin -> Configuration -> (Development) Performance -> Clear Caches

Backup db:

```
bu th 02-maintenance_mode_before_upgrade
```

Restore jane's db **on ava**:

```
rs -h jane -d 2017_03_16 th 03-cleared_cache_for_barbara_and_ava
```

### 5.4 Pull the code

```
gotht
git pull
```

### 5.5 Test and if it looks good ...

1. put in maintenance mode
2. clear all caches
3. backup the db
4. take out of maintenance mode and
5. backup the backup

Check that the site loads and that we are running the new version.

* Admin -> Reports -> Available Updates

Clear caches and backup db:

* Admin -> Configuration -> (Development) Maintenance Mode -> Check the box
* Admin -> Configuration -> (Development) Performance -> Clear Caches
* Backup DB (see below)
* Admin -> Configuration -> (Development) Maintenance Mode -> UNcheck the box
* Backup the backup (see below)

```
bu th 03-maint_mode-upgraded_8_2_5_to_8_2_7
tarHome
```

