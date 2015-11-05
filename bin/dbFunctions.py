#!/usr/bin/python3
#
# dbFunctions.py: define syntax, get args, db credentials, etc.
# -------------------------------------------------------------
# Any code that both dbMySqlBackup and dbMySqlRestore can use belongs in a function in this file
#
import os       # for getting values for environment vars
import sys      # for accessing command line arguments

def processArguments( backupOrRestore ) :
	siteArg = ''
	suffixArg = ''
	if ( len(sys.argv) == 2 ) :
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
	print( '  site.com-YYYY_MM_DD-hostname[-suffix].sql.gz' )

