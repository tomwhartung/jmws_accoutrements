
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
- [X] 2016-11-01: 4.6   to 4.6.1
- [X] 2016-09-02: 4.4.2 to 4.6
- [X] 2016-02-11: 4.4.1 to 4.4.2
- [X] 2016-01-15: 4.3.1 to 4.4.1

## Step (0) Before Starting, on All Hosts

Backup db on all hosts and ensure code matches what is in github:

- [ ] jane
- [ ] barbara
- [ ] ava

Run these commands on each host listed above:

```
bu tw 01-before_upgrade-4_6-to-4_6_1
gotwt
git pull
git status
```

## Step (1) Setting up Core Update via Admin Panel

To enable using the back end to update the code rather than downloading it, follow these steps.

We need to do this for at least one host:

* jane on 2016-11-01

### 2.1. Ensure the following line has been added to wp-config.php :

```
define('FS_METHOD','direct');     # This is one key
```

### 2.2. Ensure the web server can write the files by making the following changes:

   Change ownership of all files to www-data, create directory wp-content/upgrade

Run commands:

```
gotwt
mkdir wp-content/upgrade
sudo chown -R www-data:tomh *          # This is another key
```

Change perms of wp-content/upgrade and any subdirectories of it to 775
Run commands:

```
sudo chmod -R 775 wp-content/upgrade*  # Unsure whether this step is necessary
ls -al wp-content/upgrade
```

## Step (2) Update WP Core on *jane* Using Admin Panel:

1. Update in back end:
   Admin -> Dashboard -> Updates
2. Check in browser for each gadget type:
   If it looks OK, proceed, else figure out what went wrong.
3. Change owner of all files back to tomh and change perm of wp-content and all subdirectories of wp-content back to 755
   gotwt
   sudo chown -R tomh:www-data *
   sudo chmod 755 wp-content wp-content/*
   ls -al wp-content/
4. Check the changes into git:
   gotwt
   git status
   git add --all .
   git commit -m 'Upgrading from 4.4.2_to_4.6.' ; git push origin master
5. Backup db on this host:
   bu tw 02-after_upgrade_4.4.2_to_4.6

Updating plugins on *bette*
---------------------------
[ ] bette:
We are able to update plugins using the admin back end, as long as we
change the owner of the files in the WP installation directory tree.
1. Update in admin back end
   Admin -> Plugins -> "update now" link for the plugin
2. Commit files to git
   gotwt
   git status
   git add wp-content/
   gc 'Upgraded akismet to version 3.1.11 .' ; gpom

Updating wp core and plugins on jane and barbara:
-------------------------------------------------
1. Make sure database is backed up (in previous section "All Hosts: above)
   bu tw 01-before_upgrade_4.4.2_to_4.6    # should have already been done!
2. Open browser window on jane:
-> May have to edit wp-config.php to ensure you are on jane
   Admin panel -> Dashboard -> Updates
3. Update core code on jane using git pull:
   gotwt
   git pull
4. Test in browser
   Load admin panel
   If there are db updates will see: "Database update required."
      Click "Update Wordpress Database " button: "Your WordPress database has been successfully updated."
      Click "Continue" button: looks like we are good to go!
   Admin panel -> Dashboard -> Updates
   Ensure it is running the new versions of core and akismet
5. Backup new copy of db
   bu tw 02-after_upgrade_4.4.2_to_4.6
6. If everything looks ok, repeat process on barbara

Updating themes and installing twentysixteen on all hosts
---------------------------------------------------------
Need to update three themes and want to install one (twentysixteen).
Unsure whether these updates affect the database, so doing it a little differently
Upgrade each theme on bette, then jane and barbara
1. Take backups, update twentyfifteen on bette
   bu tw 03-before_upgrade_themes
   gotwt
   ## upgrade twentyfifteen in admin panel
   Test bette in browser 
   - admin: check version number
   - site: ensure it loads
   gs
   gd
   git add --all
   gc 'Upgraded theme twentyfifteen to version 1.6 .'
   git push origin master
1.1 Pull code on jane, test
   bu tw 03-before_upgrade_themes
   gotwt
   git pull
   Test jane in browser: admin and site
1.2 Pull code on barbara, test
   bu tw 03-before_upgrade_themes
   gotwt
   git pull
   Test barbara in browser: admin and site
2. Follow above process for twentyfourteen
   bu tw 04-before_upgrade_twentyfourteen
   ## upgrade twentyfourteen in admin panel
   Test bette in browser 
   - admin: check version number
   - site: ensure it loads
   gs
   gd
   git add --all
   gc 'Upgraded theme twentyfourteen to version 1.8 .'
   git push origin master
2.1 Pull code on jane, test
   As above
2.2 Pull code on barbara, test
   As above
3. Follow above process for twentythirteen
   bu tw 05-before_upgrade_twentythirteen
   ## upgrade twentythirteen in admin panel
   Test bette in browser 
   - admin: check version number
   - site: ensure it loads
   gs
   gd
   git add --all
   gc 'Upgraded theme twentythirteen to version 2.0 .'
   git push origin master
3.1 Pull code on jane, test
   As above
3.2 Pull code on barbara, test
   As above
4. Install twentysixteen
   bu tw 06-before_add_twentysixteen
   ## install twentysixteen in admin panel
   Test bette in browser 
   - admin: activate theme
   - site: ensure it loads
   gs
   gd
   git add --all
   gc 'Added theme twentysixteen.'
   git push origin master
4.1 Pull code on jane, test
   As above
4.2 Pull code on barbara, test
   As above
   bu tw 07-after_upgrade_all_themes
5. Change the owner of all files back to tomh
   On bette:
      gotwt
      sudo chown -R tomh *
Conclusion:
-----------
Checking the diffs after installing the themes on bette, I can see there
are no database changes.  So we just pull the code.  Note however that
you can never have too many backups of the DB!

