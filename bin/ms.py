#!/usr/bin/python3
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
from subprocess import call, check_output  # for running commands

import shutil       # for determining whether a command is in user's path
import sys          # for accessing command line arguments

dbName = ''
dbUser = ''
dbPass = ''
site = ''

if ( len(sys.argv) == 1 ) :
	site = ''
elif ( len(sys.argv) == 2 ) :
	siteArg = sys.argv[1]
	site = siteArg

#
# Run the command and process its output
# Reference: https://docs.python.org/dev/library/shutil.html#shutil.which
#
if ( site != '' ) :
	getNameCommand = 'getDbName'
	output = check_output( [getNameCommand, site] )
	print( 'getNameCommand = ', getNameCommand )
	print( 'site = ', site )
	print( 'output = ', output, "\n" )
	getUserCommand = 'getDbUser'
	output = check_output( [getUserCommand, site] )
	print( 'getUserCommand = ', getUserCommand )
	print( 'site = ', site )
	print( 'output = ', output, "\n" )
	getPassCommand = 'getDbPass'
	output = check_output( [getPassCommand, site] )
	print( 'getPassCommand = ', getPassCommand )
	print( 'site = ', site )
	print( 'output = ', output, "\n" )

#
# If we don't have a password, the -p arg to mysql causes it to prompt them for it
#
if ( "$dbPass" == '' ) :
   passwordArg = '-p'
else :
   passwordArg = '--password=' + dbPass

#
# If we don't have a specific user, we know that the root user will always be there
#
if ( dbUser == '' ) :
   dbUser = "root"

print( 'name: ' + dbName )
print( 'user: ' + dbUser )
print( 'pass: ' + dbPass )
print( 'passwordArg: ' + passwordArg )

mysqlCommand = 'mysql -u ' + dbUser + ' ' + passwordArg + ' ' + dbName

call( 'mysql' )
