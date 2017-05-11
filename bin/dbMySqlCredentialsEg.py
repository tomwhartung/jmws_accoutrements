#!/usr/bin/python3
#
# dbMySqlCredentialsEg.py: define arrays of site names, corresponding databases, etc.
# -----------------------------------------------------------------------------------
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
exampleoneAliases   = ['exampleone.com', 'e', 'ex', 'e1', 'ex1']
exampletwoAliases   = ['exampletwo.com', 'e2', 'ex2']
examplethreeAliases = ['examplethree.org', 'e3', 'ex3']

#
# Database Names
#
dbNames['exampleone.com']   = 'joomla_exampleone'
dbNames['exampletwo.com']   = 'wordpress_exampletwo'
dbNames['examplethree.org'] = 'drupal_examplethree'

#
# Database Users
#   If you did not create a user specifically for your db, use 'root'
#
dbUsers['exampleone.com']   = 'joomla'
dbUsers['exampletwo.com']   = 'wordpress'
dbUsers['examplethree.org'] = 'drupal'

#
# Database Passwords
# Please by all means use much stronger passwords!
#
dbPasswords['exampleone.com']   = '123abc'
dbPasswords['exampletwo.com']   = 'password1'
dbPasswords['examplethree.org'] = 'asdfg'

#
# 'all' is a special case, currently implemented for the command script only
# These statements allow running the mysql command as root without specifying a db
# TODO: implement the 'all' option for the backup and restore scripts
#
dbSites = [ 'exampleone.com', 'exampletwo.com', 'examplethree.org']
dbPasswords['all'] = 'r00t'
dbNames['all'] = ''
dbUsers['all'] = 'root'

#
# Find the site specified by siteArg (in dbMySqlBackup or dbMySqlRestore)
#   and use its name to set the global db credential values
#
siteName = siteArg
if( siteArg in exampleoneAliases ) :
	siteName = 'exampleone.com'
elif( siteArg in exampletwoAliases ) :
	siteName = 'exampletwo.com'
elif( siteArg in examplethreeAliases ) :
	siteName = 'examplethree.org'

#
# If things are not working as hoped,
#   uncomment one or more of these lines to see what's going on
#
### print( 'dbData.py: siteArg = ', siteArg )
### print( 'dbData.py: siteName = ', siteName )

