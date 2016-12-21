
# Upgrading Drupal 8.2.2 to 8.2.3

## Purpose

Use drush to upgrade a single minor release.

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

* https://www.drupal.org/node/2550801 - Update using drush

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
bu th 01-before_upgrading_8_2_2_to_8_2_3
```

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
cp  drupal-8.2.3.tar.gz ../unpack
cd ../unpack
tar -xvzf drupal-8.2.3.tar.gz
rm drupal-8.2.3.tar.gz
cd ../drupal-8.2.3/
more core/CHANGELOG.txt
less core/UPDATE.txt
```

## Step (3) Update the Development Host (jane)

Use drush or the **Configuration -> (Development section) Maintenance mode** admin option to put the site into maintenance mode:

```
gotht
drush sset system.maintenance_mode 1
```

### 3.1 Use Drush

This is a minor upgrade, with no changes to any of the settings files, so it's a good chance to try this process.

Run these commands:

```
gotht
composer update
drush pm-update drupal
```

I think you are supposed to run the `composer update` command first, but I ran `drush pm-update drupal` and
fortunately it seemed to work ok.


### 3.2 Check:

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

### 3.3 Put site back online:

Using drush:

```
gotht
drush sset system.maintenance_mode 0 drush cr
```

### 3.4 Test, and backup and commit code if ok

If able to access site and it looks ok, backup the db:

```
bu th 02-after_updating_8_2_2_to_8_2_3
```

and commit the code:

```
gothd
git status
git add --all
git commit -m 'Upgraded to the new release, 8.2.3 .' ; gpom
git status
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
bu th 03-cleared_cache_for_barbara
```

### 4.2 Backup db on barbara

Use these admin options to clear the cache:

* Admin -> Configuration -> Development -> Clear All Caches

Run this command **on barbara** to backup the database:

```
bu th 02-before_restoring_from_jane
```

### 4.3 Restore jane's db on barbara and pull new code

Copy db **from jane** to barbara:

```
toBarbara tomhartung.d8-2016_11_26-jane-03-cleared_cache_for_barbara.sql.gz
```

Restore jane's db **on barbara**:

```
rs -h jane th 03-cleared_cache_for_barbara
```

### 4.4 Pull the code

```
gotht
git pull
```

### 4.5 Test and if it looks good, clear caches and backup the db

Check that the site loads and shows we are running the new version:

* Admin -> Reports -> Available Updates

If it looks ok, clear all caches in admin panel and backup db:

* Admin -> Configuration -> Development -> Clear All Caches

```
bu th 04-upgraded_8_2_2_to_8_2_3
```

## Step (5) Update the Production Host (ava)

[ ] ava

### 5.0 Process

Follow same process as we did for barbara, except that on ava:

* **Be sure to put the site in maintenance mode first!!**
* We are now pushing files from barbara to ava (instead of from jane to barbara)

### 5.1 Copy db from jane to ava

Copy db **from jane** to ava:

```
gobu
toAva tomhartung.d8-2016_11_26-jane-03-cleared_cache_for_barbara.sql.gz
```

### 5.2 Put in maintenance mode, clear caches, and backup db

Put in maintenance mode and clear caches:

* Admin -> Configuration -> (Development) Maintenance Mode -> Check the box
* Admin -> Configuration -> (Development) Performance -> Clear Caches

Backup db:

```
bu th 02-maintenance_mode_8_1_7
```

Restore jane's db **on ava**:

```
rs -h jane -d 2016_11_26 th 03-cleared_cache_for_barbara
```

### 5.4 Pull the code

```
gotht
git pull
```

### 5.5 Test and if it looks good, clear caches and backup the db

Check that the site loads and that we are running the new version.

* Admin -> Reports -> Available Updates

Clear caches and backup db:

* Admin -> Configuration -> (Development) Performance -> Clear Caches

```
bu th 03-upgraded_8_2_2_to_8_2_3
tarHome
```

