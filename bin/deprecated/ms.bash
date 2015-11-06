#!/bin/bash
#
# ms: runs mysql for lazy typists
# -------------------------------
# If a site name or abbreviation is specified and
#   one or more of the following getDb* scripts is in the current PATH,
#     run it to get the site-specific credential tidbit stored in it
# List of confidential, top secret super simple scripts that,
#   when given a site name or abbreviation, can print a relevant credential tidbit to save us typing
#     getDbName
#     getDbPwd
#     getDbUser
# If those scripts are used, these should be in your PATH but NOT checked in to a public repo!!
# (If those scripts are not used, this little interface doesn't help much!!)
#
dbName=''
dbUser=''
dbPass=''

#
# The command "command" checks whether the specified command is in the current user's PATH
# Reference: http://stackoverflow.com/questions/592620/check-if-a-program-exists-from-a-bash-script
#
if [ "$1" != '' ]; then
	site=$1
	command -v getDbName > /dev/null 2>&1
	if [ $? == 0 ]; then
		dbName=$(getDbName $site)
	fi
	command -v getDbUser > /dev/null 2>&1
	if [ $? == 0 ]; then
		dbUser=$(getDbUser $site)
	fi
	command -v getDbPass > /dev/null 2>&1
	if [ $? == 0 ]; then
		dbPass=$(getDbPass $site)
	fi
fi
#
# If we don't have a password, the -p arg to mysql causes it to prompt them for it
#
if [ "$dbPass" == '' ]; then
   passwordArg="-p"
else
   passwordArg="--password=$dbPass"
fi
#
# If we don't have a specific user, we know that the root user will always be there
#
if [ "$dbUser" == '' ]; then
   dbUser="root"
fi

### echo 'name: ' $dbName
### echo 'user: ' $dbUser
### echo 'pass: ' $dbPass
### echo 'passwordArg: ' $passwordArg
### set -x

mysql -u $dbUser $passwordArg $dbName
