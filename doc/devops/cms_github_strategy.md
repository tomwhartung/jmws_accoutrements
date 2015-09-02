
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
* Allowing the web master to back out of changes that have unforeseen negative side effects
* Support rapid deployment to multiple host instances (development, test, production, etc.)

### Requirements
Using this strategy requires:
* some sort of Unix(-esque) shell command line access to the server.  Linux and Mac are excellent, Cygwin is fine, and github's shell should be ok (but I am not familiar with it).
* some familiarity with how to enter commands in a Unix(-esque) shell command window.

### Directory Structure
The parent directory for all site code is htdocs, e.g., /var/www/joomoowebsites.com/htdocs .

Two required directories exist under htdocs:
* customizations - the source for all CMS extensions
* [site-name] - the core CMS source, along with any site-specific media (e.g., 


git clone github@...

Important:
	They will need to move the code or link it.

Recommended:
	Include instructions on how to link it.
	Update ln_joomla script to work in a more general case.


