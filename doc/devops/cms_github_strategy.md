
# Jmws Github Repo Strategy
How to keep Jmws extensions and CMS core code in separate github repos and different directory trees.

Includes instructions on how to use the Jmws `ln_*_customizations` scripts to link the extensions into the core code.

## Overview
This describes the source code development, maintenance, and deployment strategy used by JooMoo WebSites LLC.

Installing Jmws code from github can be greatly simplified by following this, or a similar strategy.

It's not complicated, and I have provided tools to help manage it, so if you are interested in using one of our extensions, consider taking a few minutes to grok it.

### Terminology
*CMS Core Code* refers to the open source code that comprises a Content Management System, such as Joomla, WordPress, or Drupal.
*CMS Extensions* refers to all packages that one can install in to a Content Management System (CMS).  Extensions include Joomla templates, modules, components, and plugins, and all WordPress themes and plugins, and all Drupal modules and themes.

### Goals
The goals of this strategy are:
* To keep site-specific CMS code separate from CMS extensions used on multiple sites
* To use Unix soft links to integrate the generic CMS extensions into the site-specific CMS code so that the site can use the code

### Purpose
The purpose of this strategy is to use github to:
* Keep versions of all files (except the database and web server) needed to get a site going
* Allow the web master to back out of changes that have unforeseen negative side effects
* Support rapid deployment to multiple host instances (development, test, production, etc.)

### Requirements
Using this strategy requires:
* some sort of Unix(-esque) shell command line access to the server.  Linux and Mac are excellent, Cygwin is fine, and github's shell should be ok (but I am not familiar with it).
* some familiarity with how to enter commands in a Unix(-esque) shell command window.

### Directory Structure
The parent directory for all site code is htdocs, e.g., /var/www/joomoowebsites.com/htdocs .

Two required directories exist under htdocs:
* customizations - the source for all CMS extensions
* [site-name] - the core CMS source, along with any site-specific media (e.g., joomoowebsites.com)

#### Joomla example:
On my server, the `/var/www/joomoowebsites.com/htdocs/` directory has two subdirectories, customizations and joomoowebsites.com .  These in turn contain subdirectories as follows

|-- customizations/

|-- |-- jmws_idMyGadget_for_joomla/

|-- |-- jmws_mod_demo_idMyGadget/

|-- |-- jmws_mod_menu_idMyGadget/

|-- |-- jmws_protostar_tomh_idMyGadget/

|-- |-- . . .

|-- joomoowebsites.com/   ## This contains the CMS core source and is the Server's DocumentRoot

|-- |-- modules/

|-- |-- templates/

|-- |-- . . .

I use the ln_joomla_customizations to link the customizations into the correct directories in the core code.

#### WordPress example:
On my server, the `/var/www/tomwhartung.com/htdocs/` directory has two subdirectories, customizations and tomwhartung.com .  These in turn contain subdirectories as follows:

|-- customizations/

|-- |-- jmws_idMyGadget_for_wordpress/

|-- |-- jmws_wp_twentyfifteen_idMyGadget/

|-- |-- . . .

|-- tomwhartung.com/   ## This contains the CMS core source and is the Server's DocumentRoot

|-- |-- wp-content/plugins

|-- |-- wp-content/themes/

|-- |-- . . .

I use the ln_wordpress_customizations to link the customizations into the correct directories in the core code.

#### Drupal example:
On my server, the `/var/www/tomhartung.com/htdocs/` directory has two subdirectories, customizations and tomhartung.com .  These in turn contain subdirectories as follows:

|-- customizations/

|-- |-- jmws_idMyGadget_for_drupal/

|-- |-- jmws_drupal_stark_idMyGadget/

|-- |-- . . .

|-- tomwhartung.com/   ## This contains the CMS core source and is the Server's DocumentRoot

|-- |-- sites/all/modules

|-- |-- sites/all/themes/

|-- |-- . . .

I use the ln_drupal_customizations to link the customizations into the correct directories in the core code.

### Downloading
Use `git clone` to download the source, getting the URI for the code from the repo's main page.

``` 
git clone github@...
``` 

You can download the zip file, but using git clone makes it easy to keep the code up to date.

If you are unfamiliar with git, there is plenty of documentation on the net about it.

### Setup
Change directories into the htdocs directory and run the appropriate ln_*_customizations script to link the customizations into the site code.

If something is wrong, the script should display an intelligible error messages, if it doesn't let me know!

#### Joomla Example
For example, to link the joomla customizations in the `customizations` directory to the site code in the `joomla-example.com` directory:

``` 
cd /var/www/joomla-example.com/htdocs/
ln_joomla_customizations joomla-example.com
ls -al joomla-example.com/modules     ## should see links to any customizations that contain a module
ls -al joomla-example.com/templates   ## should see links to any customizations that contain a template
``` 

Lazy typists should be able to use file name completion on the joomla-example.com directory, making this very easy.

#### WordPress Example
For example, to link the wordpress customizations in the `customizations` directory to the site code in the `wordpress-example.com` directory:

``` 
cd /var/www/wordpress-example.com/htdocs/
ln_wordpress_customizations wordpress-example.com
ls -al wordpress-example.com/wp-content/plugins    ## should see links to any customizations that contain a plugin
ls -al wordpress-example.com/wp-content/themes     ## should see links to any customizations that contain a theme
``` 

Lazy typists should be able to use file name completion on the wordpress-example.com directory, making this very easy.

#### Drupal Example
For example, to link the drupal customizations in the `customizations` directory to the site code in the `drupal-example.com` directory:

```
cd /var/www/drupal-example.com/htdocs/
ln_drupal_customizations drupal-example.com
ls -al drupal-example.com/wp-content/plugins    ## should see links to any customizations that contain a plugin
ls -al drupal-example.com/wp-content/themes     ## should see links to any customizations that contain a theme

```

Lazy typists should be able to use file name completion on the drupal-example.com directory, making this very easy.

### Deployment: Keeping Up-to-Date
Use `git pull` to update the source: getting the URI for the code from the repo's main page.

``` 
git pull
``` 

### Checking CMS Core Code Into Git
Upgrading your site to a new version of the CMS Core code is easier when you check the code into github.

The specifics of this technique vary for the different CMSes, and you may have your own ideas as to what the best way to do it is, so I will not go into details here.

This does however make it easier to deploy updates made to a local site, once the local site is working ok.  It also helps when adding images and other media.

