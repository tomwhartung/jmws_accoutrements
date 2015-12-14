#!/usr/bin/python3
#
# ln_gitignored_files.py: links the sensitive and private files we are not checking into git
# ------------------------------------------------------------------------------------------
# #####################
# ######## TBD ########
# #####################
#
import os
from os import chdir, getcwd, listdir
from os.path import isfile, isdir, islink
from subprocess import call

##
#  Checks that the specified directory exists, exiting with an error message if it doesn't
#
def checkForDirectory( dirToCheck ) :
	if isdir( dirToCheck ) :
		print( 'Found a ' + dirToCheck + ' directory, cool.' )
	else:
		print( 'Expecting a "' + dirToCheck + '" directory, but it is not here.' )
		print( 'The current directory is: "' + htdocsDir + '"' )
		print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
		exit( 1 )
##
#  Links the gitignored files (e.g., wp-config.php)
#
# #####################
# ######## TBD ########
# #####################
#
def linkGitignoredFiles( customization ) :
	print( 'Linking gitignored files ...' )
	rootedSourceDir = htdocsDir + '/gitignored/'
	destinationDir = htdocsDir + '/' + mainSiteDir
	gitignoredFiles = listdir( rootedSourceDir )
	### print( 'linkLanguageFiles: rootedSourceDir = ' + rootedSourceDir )
	### print( 'linkLanguageFiles: destinationDir = ' + destinationDir )
	### print( 'languageFiles:' )
	### print( languageFiles )
	for ignoredFile in gitignoredFiles :
		rootedLanguageFile = rootedSourceDir + '/' + langFile
		if( isfile(rootedLanguageFile) ) :
			print( '\tlinking "' + rootedLanguageFile + "\" to\n\t\t\"" + destinationDir + '"' )
		###	lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLanguageFile + ' .; cd ' + htdocsDir 
		###	print( 'lnCommand: ' + lnCommand )
		###	call( lnCommand, shell=True )

##
#  Driver function to call other functions to link specific types of customizations
#
# #####################
# ######## TBD ########
# #####################
#
def linkGitignoredFiles( customization ) :
	print( 'Linking files in the ' + customization + ' customization...' )
	wpContentDir = customizationsDir + '/'  + customization + '/' + 'wp-content'
	wpContentSubdirs = listdir( wpContentDir )
	wpContentSubdirs.sort()
	for subdirectory in wpContentSubdirs:
		if ( subdirectory == 'plugins' ) :
			linkPluginsDirs( customization )
		elif ( subdirectory == 'themes' ) :
			linkThemesDirs( customization )

#
# #####################
# ######## TBD ########
# #####################
#
customizationsDir = 'customizations'
mainSiteDir = 'tomwhartung.com'
htdocsDir = getcwd()
exitVal = 0

checkForDirectory( customizationsDir )   # exits if directory not present
checkForDirectory( mainSiteDir )         # exits if directory not present

customizations = listdir( customizationsDir )
customizations.sort()
print( 'NOT Linking the following gitignored files to the appropriate directories in ' + mainSiteDir + ':' )
print( '**************' )
print( '*** FIX ME ***' )
print( '**************' )

###
### #############
### ### TODO: ###
### #############
###
### linkGitignoredFiles( customization ) :


exit( exitVal )
