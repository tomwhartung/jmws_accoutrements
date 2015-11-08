#!/usr/bin/python3
#
# gitFunctions.py: functions used by more than one of the git* scripts in this directory
# --------------------------------------------------------------------------------------
#
import sys      # for accessing command line arguments

#
# Use command line argument (or lack thereof) to derive the git command we want to run
#
def processArguments() :
	command = ''
	if ( len(sys.argv) == 1 ) :
		print( 'No command specified, running "git status"' )
		command = 'status'
	elif ( len(sys.argv) == 2 ) :
		command = sys.argv[1]
	else :
		print( 'Too many arguments, try again.' )
		exit( 1 )
	#
	# Translate single-letter abbreviations for common commands (no one likes to type extra letters)
	#
	if ( len(command) == 1 ) :
		if ( command == 'd' ) :
			command = 'diff'
		elif ( command == 'p' ) :
			command = 'pull'
		elif ( command == 's' ) :
			command = 'status'
	gitCommand = 'git ' + command
	return gitCommand

