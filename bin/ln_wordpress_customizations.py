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
#  Links directories containing plugins
#
def linkPluginsDirs( customization ) :
	print 'linkPluginsDirs: TBD!'

##
#  Links directories containing themes
#
def linkThemesDirs( customization ) :
	print( 'Linking wp-content/themes directories for customization ' + customization + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + customization + '/wp-content/themes'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/wp-content/themes'
	wpContentThemes = listdir( rootedSourceDir )
	print( 'linkThemesDirs test: rootedSourceDir = ' + rootedSourceDir )
	print( 'linkThemesDirs test: destinationDir = ' + destinationDir )
	print( 'wpContentThemes:' )
	print( wpContentThemes )
	for librariesVendorDir in wpContentThemes:
		rootedLibrariesVendorDir = rootedSourceDir + '/' + librariesVendorDir
		if( isdir(rootedLibrariesVendorDir) ) :
			print( '\tlinking "' + rootedLibrariesVendorDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLibrariesVendorDir + ' .; cd ' + htdocsDir 
			print( 'lnCommand: ' + lnCommand )
		### 	call( lnCommand, shell=True )

##
#  Driver function to call other functions to link specific types of customizations
#
def linkCustomization( customization ) :
	print( 'Linking files in the ' + customization + ' customization...' )
	wpContentDir = customizationsDir + '/'  + customization + '/' + 'wp-content'
	wpContentSubdirs = listdir( wpContentDir )
	wpContentSubdirs.sort()
	for subdirectory in wpContentSubdirs:
		if ( subdirectory == 'plugins' ) :
			linkPluginsDirs( customization )
		elif ( subdirectory == 'themes' ) :
			linkThemesDirs( customization )

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

###
### TODO:
###
### linkGitignoredFiles( customization ) :

for customization in customizations:
	linkCustomization( customization )

exit( exitVal )
