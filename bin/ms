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
import re           # regex utils for cleaning up raw command output
import shutil       # for determining whether a command is in user's path
import sys          # for accessing command line arguments

from subprocess import call, check_output  # for running commands

dbName = ''
dbUser = ''
dbPass = ''
siteArg = ''

if ( len(sys.argv) == 1 ) :
	siteArg = ''
elif ( len(sys.argv) == 2 ) :
	siteArg = sys.argv[1]

removeQuotesPattern = re.compile( "b*'" )
## debugGetDbCredential = True
debugGetDbCredential = False

def getDbCredential( getCommand, site ) :
	rawOutput = check_output( [getCommand, site] )
	strOutput = str( rawOutput )
	dbCredential = removeQuotesPattern.sub( '', strOutput )
	if ( debugGetDbCredential ) :
		print( 'getDbCredential - getCommand = ', getCommand )
		print( 'getDbCredential - site = ', site )
		print( 'getDbCredential - rawOutput = ', rawOutput )
		print( 'getDbCredential - strOutput = ', strOutput )
		print( 'getDbCredential - dbCredential = ', dbCredential, "\n" )
	return dbCredential
#
# Run the command and process its output
# Reference: https://docs.python.org/dev/library/shutil.html#shutil.which
#
if ( siteArg != '' ) :
	dbName = getDbCredential( 'getDbName', siteArg )
	dbUser = getDbCredential( 'getDbUser', siteArg )
	dbPass = getDbCredential( 'getDbPass', siteArg )

#
# If we don't have a password, the -p arg to mysql causes it to prompt them for it
#
if ( dbPass == '' ) :
   passwordArg = '-p'
else :
   passwordArg = '--password=' + dbPass

#
# If we don't have a specific user, we know that the root user will always be there
#
if ( dbUser == '' ) :
   dbUser = "root"

### print( 'dbName = ', dbName )
### print( 'dbUser = ', dbUser )
### print( 'dbPass = ', dbPass )
### print( 'passwordArg: ', passwordArg )

mysqlCommand = 'mysql -u ' + dbUser + ' ' + passwordArg + ' ' + dbName

print( 'calling mysqlCommand = "', mysqlCommand, '"' )
call( mysqlCommand, shell=True )
