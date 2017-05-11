#!/usr/bin/python3
#
# dbMySqlFunctions.py: define syntax, get args, db credentials, etc.
# ------------------------------------------------------------------
# Any code that both dbMySqlBackup and dbMySqlRestore can use should be in a function in this file
#
import os       # for getting values for environment vars
import socket   # for getting the hostName
import sys      # for accessing command line arguments
import time     # for the date string in our backup file name
import getopt   # for processing restore-specific overrides (command line options)

#
#  Process the overrides allowed when we are restoring
#  Note that when restoring we have a few additional options (overrides: e.g., -d and -h)
#
def processRestoreOverrides( ) :
	dateOverride = ''
	hostNameOverride = ''
	try :
		argv = sys.argv[1:]
		opts, args = getopt.getopt( argv, "d:h:", ["date=","hostName="] )
	except getopt.GetoptError :
		fileNameOverrides = [dateOverride, hostNameOverride]
		return fileNameOverrides
	try :
		for opt, arg in opts :
			if( opt in ("-d", "--date") ) :
				dateOverride = arg
				sys.argv.pop(1)   # remove "-d" from arg list
				sys.argv.pop(1)   # remove "YYYY_MM_DD" from arg list
			elif( opt in ("-h", "--hostName") ) :
				hostNameOverride = arg
				sys.argv.pop(1)   # remove "-h" from arg list
				sys.argv.pop(1)   # remove "<hostName>" from arg list
	except :
		pass
	fileNameOverrides = [dateOverride, hostNameOverride]
	return fileNameOverrides

#
#  Process the command line arguments.
#
def processArguments( backupOrRestore ) :
	siteArg = ''
	suffixArg = ''
	if ( len(sys.argv) == 2 ) :
		if ( sys.argv[1] == '--help' ) :
			syntax( backupOrRestore )
			exit( 0 )
		siteArg = sys.argv[1]
	elif ( len(sys.argv) == 3 ) :
		siteArg = sys.argv[1]
		suffixArg = sys.argv[2]
	elif ( backupOrRestore == 'command' ) :   # Really a trivial case (no file name involved)
		siteArg = 'all'                        # TODO: implement in a future iteration
	else :
		syntax( backupOrRestore )
		print( 'Wrong number of args.' )
		print( 'len(sys.argv) =', len(sys.argv) )
		print( 'str(sys.argv) =', str(sys.argv) )
		exit( 1 )
	arguments = [siteArg, suffixArg]
	return arguments

#
#  Display a brief syntax statement, describing the options and purpose of the script
#
def syntax( backupOrRestore ) :
	restoreOptions = ''
	if( backupOrRestore == 'restore' ) :
		restoreOptions = '[-d YYYY_MM_DD] [-h hostName]'
	basename = os.path.basename( sys.argv[0] )
	print( 'Syntax:' )
	print( '  ' + basename + ' [--help] ' + restoreOptions + ' site [suffix]' )
	if( backupOrRestore == 'restore' ) :
		print( '    -d: optionally override today\'s date in fileName (YYYY_MM_DD)' )
		print( '    -h: optionally override current hostName in fileName' )
	print( '    --help: display syntax statement then exit' )
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
def getDbBackupFileBaseName( siteName, suffixArg, dateOverride='', hostNameOverride='' ) :
	if( dateOverride == '' ) :
		dateString = time.strftime( '-%Y_%m_%d-' )
	else :
		dateString = '-' + dateOverride + '-'
	if( hostNameOverride == '' ) :
		hostName = socket.gethostname()
	else :
		hostName = hostNameOverride
	suffixString = ''
	#
	# If we have a suffix, prefix it with a dash, to separate it from the hostname
	#
	if( suffixArg != '' ) :
		suffixString = '-' + suffixArg
	dbBackupFileName = siteName + dateString + hostName + suffixString + '.sql.gz'
	return dbBackupFileName

#
#  Returns the name of the Top Secret DB Credentials file,
#  Hopefully the path is set in the environment, but if not,
#  "point" to the example file which contains information about all this
#
def getDbCredentialsFile() :
	dbCredentialsFileDefault = 'dbMySqlCredentialsEg.py'
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

