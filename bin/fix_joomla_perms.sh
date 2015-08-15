#!/bin/bash
#
# fix_joomla_perms.sh: fix file and directory ownerships and permissions for joomla installations
# -----------------------------------------------------------------------------------------------
#
if [ -d 'administrator' -a -d 'components' ]; then
	echo 'If requested, enter your password so we can run sudo to change the owner and group for all files and directories'
else
	echo 'This does not look like a joomla install. Exiting!'
	exit 1
fi

sudo chown -R tomh:www-data .
sudo find * -type d -exec chmod 755  {} \;

#
# This list of directories is from the System -> System Information -> Directory Permissions page/tab.
# Unfortunately (for our automation efforts) the list of all directories is much longer.
#
sudo chmod 664 configuration.php
sudo chmod 775 administrator/components
sudo chmod 775 administrator/language
sudo chmod 775 administrator/language/en-GB
sudo chmod 775 administrator/language/overrides
sudo chmod 775 administrator/manifests/files
sudo chmod 775 administrator/manifests/packages
sudo chmod 775 administrator/manifests/libraries
sudo chmod 775 administrator/modules
sudo chmod 775 administrator/templates
sudo chmod 775 components
sudo chmod 775 images
sudo chmod 775 images/headers
sudo chmod 775 images/joomoowebsites.com
sudo chmod 775 images/banners
sudo chmod 775 images/sampledata
sudo chmod 775 language
sudo chmod 775 language/en-GB
sudo chmod 775 language/overrides
sudo chmod 775 libraries
sudo chmod 775 media
sudo chmod 775 modules
sudo chmod 775 plugins
sudo chmod 775 plugins/extension
sudo chmod 775 plugins/content
sudo chmod 775 plugins/user
sudo chmod 775 plugins/twofactorauth
sudo chmod 775 plugins/finder
sudo chmod 775 plugins/editors-xtd
sudo chmod 775 plugins/search
sudo chmod 775 plugins/quickicon
sudo chmod 775 plugins/system
sudo chmod 775 plugins/authentication
sudo chmod 775 plugins/editors
sudo chmod 775 plugins/captcha
sudo chmod 775 plugins/installer
sudo chmod 775 templates
sudo chmod 775 configuration.php
sudo chmod 775 cache
sudo chmod 775 administrator/cache
sudo chmod 775 logs
sudo chmod 775 tmp
