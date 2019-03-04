
# 1-bette.md

Upgrading bette to Ubuntu 18.04.2.

## Notes

1. Tried to upgrade on command line:
   - "New release '18.04.2 LTS' available."
   - "Run 'do-release-upgrade' to upgrade to it."
   But got this error:
  - root@bette:~
  - # do-release-upgrade -d
  - Checking for a new Ubuntu release
  - Please install all available updates for your release before upgrading.
  - root@bette:~

2. Found this post:
   - https://askubuntu.com/questions/1085295/issues-in-upgrade-form-ubuntu-18-04-to-18-10
   - An answer further down says to use the graphical interface "Software Updater" tool
   Decided to try using Software Updater

3. Using Software Updater
   - Release Notes: https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes
   - Details:
     - 9 packages no longer supported
     - 60 packages to be removed
     - 620 new packages to be installed
     - 2094 packages to be upgraded
     - Should take about 3:08 to download, several hours to complete
   - Starting on 2019-03-03 at 12:45 AM
   - Next day, 2019-03-03 at 2:32 PM, in the Installing the upgrades step
     - presented with dropdown, need to choose between gdm3 and lightdm
     - lightdm is faster, gdm3 is more full-featured
     - choosing gdm3
   - See 1-bette-postgreSQL.md
  - Pop-up window says it will replace config file /etc/logrotate.d/apache2
    - See version in RCS


4. To Do After Upgrade
   - Will need to reinstall xscreensaver

