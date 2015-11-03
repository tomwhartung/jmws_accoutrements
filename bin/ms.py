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
site = ''

if ( len(sys.argv) == 1 ) :
	site = ''
elif ( len(sys.argv) == 2 ) :
	siteArg = sys.argv[1]
	site = siteArg

removeQuotesPattern = re.compile( "b*'" )

def getDbCredential( getCommand, site ) :
	rawOutput = check_output( [getCommand, site] )
	strOutput = str( rawOutput )
	dbCredential = removeQuotesPattern.sub( '', strOutput )
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
if ( site != '' ) :
	getNameCommand = 'getDbName'
	rawOutput = check_output( [getNameCommand, site] )
	strOutput = str( rawOutput )
	dbName = removeQuotesPattern.sub( '', strOutput )
	print( 'getNameCommand = ', getNameCommand )
	print( 'site = ', site )
	print( 'rawOutput = ', rawOutput )
	print( 'strOutput = ', strOutput )
	print( 'dbName = ', dbName, "\n" )
	## getUserCommand = 'getDbUser'
	## rawOutput = check_output( [getUserCommand, site] )
	## print( 'getUserCommand = ', getUserCommand )
	## print( 'site = ', site )
	## print( 'rawOutput = ', rawOutput, "\n" )
	dbUser = getDbCredential( 'getDbUser', site )
	print( '*** dbUser = ', dbUser )
	getPassCommand = 'getDbPass'
	rawOutput = check_output( [getPassCommand, site] )
	print( 'getPassCommand = ', getPassCommand )
	print( 'site = ', site )
	print( 'rawOutput = ', rawOutput, "\n" )

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

print( 'dbName = ', dbName )
print( 'dbUser = ', dbUser )
print( 'dbPass = ', dbPass )
print( 'passwordArg: ', passwordArg )

mysqlCommand = 'mysql -u ' + dbUser + ' ' + passwordArg + ' ' + dbName

print( 'mysqlCommand = ', mysqlCommand )
## call( mysqlCommand )
