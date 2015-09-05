
## Installing Jmws Joomla Extensions
Installing one of the Jmws extensions requires the following steps:

1. Downloading the extension code
1. Integrating the code into your site's Joomla! code
1. Installing the extension in Joomla's back end

### How We Do It
The following document (in this repo) outlines our github strategy:

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

This puts the code in its own separate directory tree, with a single directory containing all the customizations on the same directory level as the site code.

### Integrating the Extension Code Into the CMS Core Code
We recommend keeping the extension code and the CMS core code in separate directory trees and using soft links to integrate them, for reasons cited in the [github strategy](https://github.com/tomwhartung/jmws_accoutrements/blob/master/doc/devops/cms_github_strategy.md) document.

In fact, I like this idea so much, I have invested a considerable amount of time automating and documenting it, and so do not even want to think about other techniques.

But feel free to do what feels right and works for you.

### Installing into the Joomla! back end
It is easiest to use Joomla's Discover method to install Jmws extensions.

This is the procedure we used to install a new module recently (on Aug. 28, 2015).

1. Log in to your site's Joomla! back end (administration page)

1. In the Top Menu click on Extensions -> Extension Manager

1. In the Side Menu click on Discover

1. Optional: select the following filters from their dropdowns:
	* Site
	* Module

1. Near top of page click on the Discover button

1. Find the new template or module in the list, otherwise you are doing something wrong or they changed this or something

1. Select the new template or module to install

1. Near top of page click on the Install button


