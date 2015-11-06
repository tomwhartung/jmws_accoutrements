#!/usr/bin/python3
#
# dbFunctions.py: define syntax, get args, db credentials, etc.
# -------------------------------------------------------------
# Any code that both dbMySqlBackup and dbMySqlRestore can use should be in a function in this file
#
import os       # for getting values for environment vars
import socket   # for getting the hostName
import sys      # for accessing command line arguments
import time     # for the date string in our backup file name


#
#  Process the command line arguments.
#
def processArguments( backupOrRestore ) :
	siteArg = ''
	suffixArg = ''
	if ( len(sys.argv) == 2 ) :
		if ( sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help' ) :
			syntax( backupOrRestore )
			exit( 0 )
		siteArg = sys.argv[1]
	elif ( len(sys.argv) == 3 ) :
		siteArg = sys.argv[1]
		suffixArg = sys.argv[2]
	else :
		syntax( backupOrRestore )
		print( 'Wrong number of args.' )
		exit( 1 )
	arguments = [siteArg, suffixArg]
	return arguments

#
#  Display a brief syntax statement, describing the options and purpose of the script
#
def syntax( backupOrRestore ) :
	basename = os.path.basename( sys.argv[0] )
	print( 'Syntax:' )
	print( '  ' + basename + ' site [suffix]' )
	print( '    site: site name or recognized abbreviation' )
	print( '    suffix: optional string appended to standard backup file name' )
	if( backupOrRestore == 'backup' ) :
		print( 'Saves a copy of database in a file named as follows:' )
	else :
		print( 'Restores a copy of database from a file named as follows:' )
	print( '  siteName-YYYY_MM_DD-hostname[-suffix].sql.gz' )

#
#  Check the environment for a setting for the backup directory
#  If it is not set, use the default
#
def getDbBackupDirectory() :
	dbBackupDirectoryDefault = '.'
	dbBackupDirectoryEnviron = ''
	try :
		dbBackupDirectoryEnviron = os.environ['DB_BACKUP_DIRECTORY']
	except :
		pass
	if( dbBackupDirectoryEnviron == '' ) :
		dbBackupDirectory = dbBackupDirectoryDefault
	else :
		dbBackupDirectory = dbBackupDirectoryEnviron
	return dbBackupDirectory

#
#  Assemble the basename of the backup file, using a variety of identifying components
#
def getDbBackupFileBaseName( siteName, suffixArg ) :
	dateString = time.strftime( '-%Y_%m_%d-' )
	hostName = socket.gethostname()
	suffixString = ''
	#
	# If we have a suffix, prefix it with a dash, to separate it from the hostname
	#
	if( suffixArg != '' ) :
		suffixString = '-' + suffixArg
	dbBackupFileName = siteName + dateString + hostName + suffixString + '.sql.tgz'
	return dbBackupFileName

#
#  Returns the name of the Top Secret DB Credentials file,
#  Hopefully the path is set in the environment, but if not,
#  "point" to the example file which contains information about all this
#
def getDbCredentialsFile() :
	dbCredentialsFileDefault = 'dbCredentialsFileExample.py'
	dbCredentialsFileEnviron = ''
	try :
		dbCredentialsFileEnviron = os.environ['DB_CREDENTIALS_FILE']
	except :
		pass
	if( dbCredentialsFileEnviron == '' ) :
		dbCredentialsFile = dbCredentialsFileDefault
	else :
		dbCredentialsFile = dbCredentialsFileEnviron
	return dbCredentialsFile

#
# If we don't have a password, the -p arg to mysql causes it to prompt them for it
#
def getDbPasswordArg( dbPassword ) :
	if ( dbPassword == '' ) :
		dbPasswordArg = '-p'
	else :
		dbPasswordArg = '--password=' + dbPassword
	return dbPasswordArg

#
# If we don't have a specific user, we know that the root user will always be there
#
def getDbUserArg( dbUser ) :
	dbUserArg = '-u '
	if ( dbUser == '' ) :
		dbUserArg += 'root'
	else :
		dbUserArg += dbUser
		return dbUserArg

