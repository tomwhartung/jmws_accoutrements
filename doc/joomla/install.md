
## Installing Jmws Joomla Extensions
Installing one of the Jmws extensions requires the following steps:

# Downloading the extension code
# Integrating the code into your site's Joomla! code
# Installing the extension in Joomla's back end

### How We Do It
The following document outlines our github strategy:

* [devops/cms_github_strategy.md](https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/cms_github_strategy.md)

Unless you have a specific way of doing this, we recommend taking a look at that document and using similar or even identical techniques.

### Downloading the Extension Code
You can either download the zip file or use git clone to pull the code onto your filesystem.

We recommend using the git clone method, because then it is easier to keep the code up to date.

```
cd [to your site's DocumentRoot directory]
cd ..
mkdir customizations
cd customizations
git clone github@...
```

This puts the code in its own separate directory tree, with all the customizations being on the same directory level as the site code.

### Integrating the Extension Code Into the CMS Core Code
We recommend keeping the extension code and the CMS core code in separate directory trees and using soft links to integrate them, for reasons cited in the document listed above.

In fact, I like this idea so much, I do not even want to think about other techniques, but feel free to do what feels right and works for you.

### Installing into the Joomla! back end
It is easiest to use Joomla's Discover method to install Jmws extensions.

This is the procedure we used to install a new module recently (on Aug. 28, 2015).

# Log in to your site's Joomla! back end (administration page)

# In the Top Menu click on Extensions -> Extension Manager

# In the Side Menu click on Discover

# Optional: select the following filters from their dropdowns:
	** Site
	** Module

# Near top of page click on the Discover button

# Find the new template or module in the list, otherwise you are doing something wrong or they changed this or something

# Select the new template or module to install

# Near top of page click on the Install butto
