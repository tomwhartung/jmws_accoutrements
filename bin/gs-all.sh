#!/bin/bash
#
# Run git status in all currently active git repos
#
dash_equals='-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
cd /var/www/jmws_accoutrements ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status

cd /var/www/subsites/idMyGadget ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/subsites/resume ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status

cd /var/www/joomoowebsites.com/htdocs/joomoowebsites.com ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_beez3_idMyGadget/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_idMyGadget_for_joomla/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_mod_demo_idMyGadget/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_mod_menu_idMyGadget/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_protostar_idMyGadget/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/joomoowebsites.com/htdocs/customizations/jmws_protostar_tomh_idMyGadget/ ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status

cd /var/www/tomwhartung.com/htdocs/customizations/jmws_idMyGadget_for_wordpress ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/tomwhartung.com/htdocs/customizations/jmws_twentyfifteen_idMyGadget ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status
cd /var/www/tomwhartung.com/htdocs/customizations/jmws_wp_vqsg_ot_idMyGadget ;	printf "\n$dash_equals\n$(pwd):\n" ;	git status

