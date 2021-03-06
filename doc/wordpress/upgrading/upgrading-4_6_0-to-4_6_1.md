
# Introduction

The process seems to change about the time I get used to it and acheive a comfortable level of automation and documentation.
Plus we don't run it often enough to be really confident about it or good at it etc.

## TomWHartung.com - WP Upgrading Notes for 2016

The Latest References (from upgrade to 4.3.1):

* https://wordpress.org/support/topic/core-or-plugin-update-could-not-create-directory-httpdocs?replies=27
* http://wordpress.stackexchange.com/questions/141063/when-fs-method-direct-is-chosen

## Log

- [ ] 2016-
- [ ] 2016-xx-xx: 4.6   to 4.x.x
- [ ] 2016-11-01: 4.6   to 4.6.1
- [X] 2016-09-02: 4.4.2 to 4.6
- [X] 2016-02-11: 4.4.1 to 4.4.2
- [X] 2016-01-15: 4.3.1 to 4.4.1

## Step (0) Before Starting, on All Hosts

Backup db on all hosts and ensure code matches what is in github:

- [X] jane
- [X] barbara
- [X] ava

Run these commands on each host listed above:

```
bu tw 01-before_upgrade_4_6_to_4_6_1
gotwt
git pull
git status
```

## Step (1) Setting up Core Update via Admin Panel

To enable using the back end to update the code rather than downloading it, follow these steps.

We need to do this for **only one host:**

* jane on 2016-11-01

### 1.1. Ensure the following line has been added to wp-config.php :

```
define('FS_METHOD','direct');
```

This is one key.

### 1.2. Ensure the web server can write the files by making the following changes:

   Change ownership of all files to www-data, create directory wp-content/upgrade

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

If it looks OK, proceed, else figure out what went wrong.

### 2.3. Change owner of all files back to tomh and change perm of wp-content and all subdirectories of wp-content back to 755

Run commands:

```
gotwt
sudo chown -R tomh:www-data *
sudo chmod 755 wp-content wp-content/*
ls -al wp-content/
```

### 2.4. Check the changes into git:

Run commands:

```
gotwt
git status
git add --all .
git commit -m 'Upgrading from 4.6 to 4.6.1 .' ; git push origin master
```

### 2.5. Backup db on this host, and backup the backup:

Run commands:

```
bu tw 02-after_upgrade_4_6_to_4_6_1
tarHome
```

## Step (3) Updating Plugins

Doing this on **jane**.

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
git commit -m 'Upgraded akismet to version 3.2 .' ; git push origin master
```

### 3.4 Backup the db and backup the backup

Run commands:

```
bu tw 03-after_upgrade_4_6_to_4_6_1
tarHome
```

(Actually I am unsure whether this step is necessary.)

## Step (4) Updating wp core and plugins on barbara and ava:

### 4.1. Make sure database is backed up (in previous section "All Hosts: above)

Run commands:

```
# This should have already been done!
bu tw 01-before_upgrade_4_6_to_4_6_1
```

### 4.2. Open browser window to admin page on barbara:

* Admin panel -> Dashboard -> Updates

#### Warning!

**Copying the database and wp-config.php from host to host, sometimes WP redirects!**

* When it happens, this can be extremely confusing

* Keep an eye on the URL in the browser's address bar!

You may have to edit wp-config.php to ensure you are on barbara!

### 4.3. Update core code on barbara using git pull:

Run commands:

```
gotwt
git pull
```

Should see it pull down all those changes.

### 4.4. Access in Browser and Update DB

Access admin panel in browser.

If there are db updates will see: "Database update required."

* Click "Update Wordpress Database " button: "Your WordPress database has been successfully updated."

* Click "Continue" button

**Did not see any updates to db this time.**

### 4.5. Verify Updated Versions

* Admin panel -> Dashboard -> Updates

Ensure it is running the new versions of core and akismet

Access the site, perform a "Smoke Test."

### 4.6. Backup new copy of db, and backup the backup

Run commands:

```
bu tw 02-after_upgrade_4_6_to_6_6_1
tarHome
```

### 4.7. Repeat process on ava.

1. Backup: should be done

2. Access admin panel in browser

3. Pull the code

4. Reload admin panel in browser
4.1. Update db as necessary

5. Verify updated versions in admin panel

6. Backup db `bu tw 02-after_upgrade_4_6_to_6_6_1`

