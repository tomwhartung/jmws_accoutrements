
## Jmws Content Management Github Repo Strategy


## Overview
This describes the source code development, maintenance, and deployment strategy used by JooMoo WebSites LLC.

Installing Jmws code from github can be greatly simplified by following this, or a similar strategy.

It's not complicated, and I have provided tools to help manage it, so if you are interested in using one of our extensions, consider taking a few minutes to grok it.

### Terminology
*CMS Extensions* refers to all packages that one can install in to a Content Management System (CMS).  Extensions include Joomla templates, modules, components, and plugins, and all WordPress themes and plugins.

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
/var/www/joomoowebsites.com/htdocs/
  |
  + customizations/
  | + jmws_idMyGadget_for_joomla/
  | + jmws_mod_demo_idMyGadget/
  | + jmws_mod_menu_idMyGadget/
  | + jmws_protostar_tomh_idMyGadget/
    + . . .
  |
  + joomoowebsites.com/   ## This contains the CMS core source and is the Server's DocumentRoot
    + modules/
    + templates/
    + . . .

#### WordPress example:
/var/www/tomwhartung.com/htdocs/
  |
  + customizations/
  | + jmws_idMyGadget_for_wordpress/
  | + jmws_wp_twentyfifteen_idMyGadget/
    + . . .
  |
  + tomwhartung.com/   ## This contains the CMS core source and is the Server's DocumentRoot
    + wp-content/plugins
    + wp-content/themes/
    + . . .

### Downloading
Use `git clone` to download the source, getting the URI for the code from the repo's main page.
``` 
git clone github@...
``` 

### Setup
Run the appropriate ln_*_customizations.py script in the htdocs directory to link the customizations into the site code.

For example, to link the joomla customizations in the `customizations` directory to the site code in the `joomla-example.com` directory:
``` 
cd /var/www/joomla-example.com/htdocs/
ln_joomla_customizations joomla-example.com
ls -al joomla-example.com/modules     ## should see links to any customizations that contain a module
ls -al joomla-example.com/templates   ## should see links to any customizations that contain a template
``` 
You should be able to use file name completion on the joomla-example.com directory, easy peasy.

If something is wrong, the script should display an intelligible error messages, if it doesn't let me know!

### Deployment: Keeping Up-to-Date
Use `git pull` to update the source: getting the URI for the code from the repo's main page.
``` 
git pull
``` 

