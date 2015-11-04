#!/usr/bin/python3
#
# dbDataExample.py: define arrays of site names, corresponding databases, etc.
# ----------------------------------------------------------------------------
# Example of how to set the values of the db credentials (dbName, dbUser, and dbPass) used by the
#   dbMySqlBackup, dbMySqlRestore, and dbMySqlCommand scripts in this directory
# Note:
#   The purpose of this file is to keep confidential information confidential!!!
#   Your real version of this file should not be checked in to a public repoository!!!
# To Use:
# 1. Copy this file into somewhere in your home directory or a directory where only people
#    who need to access it can access it
# 2. Set the permissions on the file to as restrictive a value as possible
# 3. Fill in the values for your site(s) and their corresponding database(s)
# 4. Set the DB_DATA_FILE environment variable to point to the hidden copy of the file
# 5. Run the scripts specifying one of the aliases (they are there to save typing)
#    Example
#       dbMySqlBackup e    # finds 'e' in exampleoneAliases and backs up exampleone.com db
#       dbMySqlBackup ex2  # finds 'ex2' in exampletwoAliases and backs up exampletwo.com db
#       dbMySqlBackup e3   # finds 'e3' in examplethreeAliases and backs up examplethree.org db
#
dbSites = [ 'exampleone.com', 'exampletwo.com', 'examplethree.org']

exampleoneAliases   = ['exampleone.com', 'e', 'ex', 'e1', 'ex1']
exampletwoAliases   = ['exampletwo.com', 'e2', 'ex2']
examplethreeAliases = ['examplethree.org', 'e3', 'ex3']

#
# Database Names
#
dbNames = {}
dbNames['exampleone.com']   = 'joomla_exampleone'
dbNames['exampletwo.com']   = 'wordpress_exampletwo'
dbNames['examplethree.org'] = 'drupal_examplethree'

#
# Database Users
#   If you did not create a user specifically for your db, use 'root'
#
dbUsers = {}
dbUsers['exampleone.com']   = 'joomla'
dbUsers['exampletwo.com']   = 'wordpress'
dbUsers['examplethree.org'] = 'drupal'

#
# Database Passwords
# Please by all means use much stronger passwords!
#
dbPasswords = {}
dbPasswords['exampleone.com']   = '123abc'
dbPasswords['exampletwo.com']   = '123abc'
dbPasswords['examplethree.org'] = '123abc'

#
# Find the site specified by siteArg (in dbMySqlBackup or dbMySqlRestore)
#   and use its name to set the global db credential values
#
if( siteArg in exampleoneAliases ) :
	siteName = 'exampleone.com'
	dbName = dbNames['exampleone.com']
	dbUser = dbUsers['exampleone.com']
	dbPass = dbPasswords['exampleone.com']
elif( siteArg in exampletwoAliases ) :
	siteName = 'exampletwo.com'
	dbName = dbNames['exampletwo.com']
	dbUser = dbUsers['exampletwo.com']
	dbPass = dbPasswords['exampletwo.com']
elif( siteArg in examplethreeAliases ) :
	siteName = 'examplethree.org'
	dbName = dbNames['examplethree.org']
	dbUser = dbUsers['examplethree.org']
	dbPass = dbPasswords['examplethree.org']

#
# If things are not working as hoped,
#   uncomment one or more of these lines to see what's going on
#
### print( 'dbData.py: topSecretDbFile = ', topSecretDbFile )
### print( 'dbData.py: siteArg = ', siteArg )
### print( 'dbData.py: siteName = ', siteName )
### print( 'dbData.py: dbName = ', dbName )
### print( 'dbData.py: dbUser = ', dbUser )
### print( 'dbData.py: dbPass = ', dbPass )

