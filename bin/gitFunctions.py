#!/usr/bin/python3
#
# gitFunctions.py: functions used by more than one of the git* scripts in this directory
# --------------------------------------------------------------------------------------
#
import sys      # for accessing command line arguments
from subprocess import call      # for running commands

##
# Use the command line argument (or lack thereof) to derive the git command we want to run
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

##
#  Change directories into the given directory and run the given command, running output through egrep and sed
#
def runGitCommand( customizationsParentDir, gitRepo, gitCommand ) :
			print( '-----------------------------------------------------------------' )
			print( gitRepo, '-', gitCommand )
			gitRepoDir = customizationsParentDir + '/' + gitRepo
			fullCommand = 'cd ' + gitRepoDir + '; ' + gitCommand + ' | egrep -v "^\b*$" | sed "s&^&' + gitRepo + ': &"'
			call( fullCommand, shell=True )

