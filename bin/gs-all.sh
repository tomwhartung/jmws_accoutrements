#!/bin/bash
#
# Run git status in all currently active git repos
#
cd /var/www/joomoowebsites.com/htdocs/subsites/idMyGadget; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/subsites/resume; printf "\n========\n$(pwd):\n"; git status 

cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_beez3_idMyGadget/ ; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_idMyGadget_for_joomla/ ; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_accoutrements/ ; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_mod_menu_idMyGadget/ ; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_protostar_idMyGadget/ ; printf "\n========\n$(pwd):\n"; git status 
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_tomh_idMyGadget/ ; printf "\n========\n$(pwd):\n"; git status 

