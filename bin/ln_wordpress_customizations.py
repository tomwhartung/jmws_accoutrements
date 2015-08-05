#!/usr/bin/python
#
# link_wordpress_customizations.py: links our customizations, so we can keep them separate from the wordpress code
# ----------------------------------------------------------------------------------------------------------------
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
def linkGitignoredFiles( extension ) :
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
#  Links directories containing libraries (vendor code)
#
def linkLibrariesVendorDirs( extension ) :
	print( 'Linking libraries/vendor directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/libraries/vendor'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/libraries/vendor'
	librariesVendors = listdir( rootedSourceDir )
	### print( 'linkLibrariesVendorDirs test: rootedSourceDir = ' + rootedSourceDir )
	### print( 'linkLibrariesVendorDirs test: destinationDir = ' + destinationDir )
	### print( 'librariesVendors:' )
	### print( librariesVendors )
	for librariesVendorDir in librariesVendors:
		rootedLibrariesVendorDir = rootedSourceDir + '/' + librariesVendorDir
		if( isdir(rootedLibrariesVendorDir) ) :
			print( '\tlinking "' + rootedLibrariesVendorDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLibrariesVendorDir + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )

##
#  Driver function to call other functions to link specific types of customizations
#
def linkCustomization( customization ) :
	print( 'Linking files in the ' + extension + ' extension...' )
	githubRepoDir = customizationsDir + '/'  + extension
	extensionSubdirs = listdir( githubRepoDir )
	extensionSubdirs.sort()
	for subdirectory in extensionSubdirs:
		if ( subdirectory == 'language' ) :
			linkLanguageFiles( extension )
		elif ( subdirectory == 'libraries' ) :
			linkLibrariesVendorDirs( extension )
		elif ( subdirectory == 'modules' ) :
			linkModuleDirs( extension )
		elif ( subdirectory == 'templates' ) :
			linkTemplateDirs( extension )

customizationsDir = 'customizations'
mainSiteDir = 'tomwhartung.com'
htdocsDir = getcwd()
exitVal = 0

checkForDirectory( customizationsDir )   # exits if directory not present
checkForDirectory( mainSiteDir )         # exits if directory not present

customizations = listdir( customizationsDir )
customizations.sort()
print( 'Linking the following customizations to the appropriate directories in ' + mainSiteDir + ':' )
print( customizations )

## for extension in customizations:
	## linkExtension( extension )

exit( exitVal )
