
# Introduction

The process seems to change about the time I get used to it and acheive a comfortable level of automation and documentation.
Plus we don't run it often enough to be really confident about it or good at it etc.

## TomWHartung.com - WP Upgrading Notes for 2018

The Latest References (from upgrade to 4.3.1):

* https://wordpress.org/support/topic/core-or-plugin-update-could-not-create-directory-httpdocs?replies=27
* http://wordpress.stackexchange.com/questions/141063/when-fs-method-direct-is-chosen

## Log

- [ ] 2017-
- [ ] 2017-XX-XX: 4.9.5 to 4.X.X
- [X] 2017-09-26: 4.7.3 to 4.9.5
- [X] 2017-03-17: 4.7.0 to 4.7.3
- [X] 2016-12-22: 4.6.1 to 4.7.0
- [X] 2016-11-01: 4.6.0 to 4.6.1
- [X] 2016-09-02: 4.4.2 to 4.6
- [X] 2016-02-11: 4.4.1 to 4.4.2
- [X] 2016-01-15: 4.3.1 to 4.4.1

## Step (0) Before Starting, on All Hosts

### Task Description

Backup db on all hosts and ensure code matches what is in github:

- [X] jane
- [X] barbara
- [X] ava

### Commands

Run these commands on each host listed above:

```
bu tw 01-before_upgrading_4_7_3_to_4_9_5
gotwt
git pull
git status
```

## Step (1) Setting up Core Update via Admin Panel

To enable using the back end to update the code rather than downloading it, follow these steps.

We need to do this for **only one host:**

* jane on 2018-05-02

### 1.1. FS_METHOD must be 'direct'

Run the following commands:

```
gotwt
grep FS_METHOD wp-config.php
```

Ensure the following line has been added to wp-config.php :

```
define('FS_METHOD','direct');
```

This is one key.

### 1.2. Ensure the web server can write the files by making the following changes:

- Change ownership of all files to www-data, create directory wp-content/upgrade

Run commands:

```
gotwt
mkdir wp-content/upgrade
sudo chown -R www-data:tomh *
```

This is another key.

Change perms of wp-content/upgrade and any subdirectories of it to 775.

Run commands:

```
sudo chmod -R 775 wp-content/upgrade*
ls -al wp-content/upgrade
```

(Actually I am unsure whether this step is necessary.)

## Step (2) Update WP Core on *jane* Using Admin Panel:

### 2.1. Update in back end:

* Admin -> Dashboard -> Updates

### 2.2. Check in browser for each gadget type:

Access the site: [jane.tomwhartung.com](http://jane.tomwhartung.com)

Access `mobile.php`:

- Chrome -> Browser home icon -> Heading: Development (jane/[mobile](http://jane.tomhartung.com/gitignored//mobile.php))

If it looks OK, proceed, else figure out what went wrong.

### 2.3. Change owner of all files back to tomh and change perm of wp-content and all subdirectories of wp-content back to 755

Run commands:

```
gotwt
sudo chown -R tomh:www-data *
sudo chmod 755 wp-content wp-content/*
ls -al wp-content/
```

The permissions on all files and directories should be `755` and the ownership should be `tomh:www-data` .

### 2.4. Check the changes into git:

Run commands:

```
gotwt
git status
git add --all .
git commit -m 'Upgrading from 4.7.3 to 4.9.5 .' ; git push origin master
```

### 2.5. Backup db on this host, and backup the backup:

Run commands:

```
bu tw 02-after_upgrading_4_7_3_to_4_9_5
tarHome
```

## Step (3) Updating Plugins

Updating akismet (even though we don't use it), on **jane**.

We are able to update plugins using the admin back end, as long as we
change the owner of the files in the WP installation directory tree.

Run commands:

```
gotwt
sudo chown -R www-data:tomh *
```

### 3.1. Update in admin back end

*  Admin -> Plugins -> "update now" link for the plugin

### 3.2. Change perms back to the way they were:

Run commands:

```
gotwt
sudo chown -R tomh:www-data *
```

### 3.3. Commit files to git

Run commands:

```
gotwt
git status
git add wp-content/
git commit -m 'Upgraded akismet to version 4.0.3 .' ; git push origin master
```

### 3.4 Backup the db and backup the backup

Run commands:

```
bu tw 03-after_upgrading_plugins_4_7_3_to_4_9_5
tarHome
```

(Actually I am unsure whether this step is necessary.)

## Step (4) Updating Templates

All templates are up to date, so NOT doing this on **jane**.

We are able to update templates using the admin back end, as long as we
change the owner of the files in the WP installation directory tree.

Run commands:

```
gotwt
sudo chown -R www-data:tomh *
```

### 4.1. Update in admin back end

* Admin -> Dashboard -> Updates
* Click on a single theme or "Select All"
* Click on "Update Themes" Button

### 4.2. Change perms back to the way they were:

Run commands:

```
gotwt
sudo chown -R tomh:www-data *
```

### 4.3. Commit files to git

Run commands:

```
gotwt
git status
git add wp-content/
git commit -m 'Upgraded themes to version 4.9.5 .' ; git push origin master
```

### 4.4 Backup the db and backup the backup

Run commands:

```
bu tw 04-after_upgrading_themes_4_7_3_to_4_9_5
tarHome
```

(Actually I am unsure whether this step is necessary.)

## Step (5) Updating wp core and plugins on barbara:

### 5.1. Make sure database is backed up (in previous section "All Hosts: above)

Run commands:

```
# This should have already been done!
bu tw 01-before_upgrading_4_7_to_4_7_3
```

### 5.2. Open browser window to admin page on barbara:

* Admin panel -> Dashboard -> Updates

#### Note!

Rather than copy the database from one host to another, we upgrade the code and let WP update the DB.

#### Warning!

If you decide to copy the DB from one host to another, sometimes there are issues.

* **Copying the database (and wp-config.php) from host to host, sometimes WP redirects!**
* When it happens, this can be extremely confusing
* Keep an eye on the URL in the browser's address bar!
* You may have to edit wp-config.php to ensure you are on barbara!

**This is why it's easier to pull the new code from github and let WP update the DB.**

### 5.3. Update core code on barbara using git pull:

Run commands:

```
gotwt
git pull
```

Should see it pull down all those changes.

### 5.4. Access in Browser and Update DB

Access admin panel in browser.

If there are db updates will see: "Database update required."

* Click "Update Wordpress Database " button: "Your WordPress database has been successfully updated."

* Click "Continue" button

**There were definitely some updates to db this time.**

### 5.5. Verify Updated Versions

* Admin panel -> Dashboard -> Updates

Ensure it is running the new versions of core and the themes.

Access the site, perform a "Smoke Test."

### 5.6. Backup new copy of db, and backup the backup

Run commands:

```
bu tw 02-after_upgrading_4_7_0_to_4_7_3
tarHome
```

## Step (6) Updating wp core and plugins on ava:

Repeat process used for barabara on ava.

1. Backup: should be done

2. Access admin panel in browser

3. Pull the code

4. Reload admin panel in browser
4.1. Update db as necessary

5. Verify updated versions in admin panel

6. Backup db `bu tw 02-after_upgrading_4_7_0_to_4_7_3`

