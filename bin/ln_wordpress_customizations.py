#!/usr/bin/python3
#
# ln_wordpress_customizations.py: links our customizations, so we can keep them separate from the wordpress code
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
#  Links directories containing plugins
#
def lnPluginsDirs( customization ) :
	print( 'Linking wp-content/plugins directories for customization ' + customization + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + customization + '/wp-content/plugins'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/wp-content/plugins'
	wpContentPlugins = listdir( rootedSourceDir )
##	print( 'lnPluginsDirs: rootedSourceDir = ' + rootedSourceDir )
##	print( 'lnPluginsDirs: destinationDir = ' + destinationDir )
##	print( 'lnPluginsDirs: wpContentPlugins = ', end="" )
##	print( wpContentPlugins )
	for themeDir in wpContentPlugins :
		rootedThemeDir = rootedSourceDir + '/' + themeDir
		if( isdir(rootedThemeDir) ) :
			print( '\tlinking "' + rootedThemeDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = "    cd " + destinationDir + ";\n    ln -fs " + rootedThemeDir + " .;\n    cd " + htdocsDir 
			print( "lnCommand:\n" + lnCommand )
			call( lnCommand, shell=True )

##
#  Links directories containing themes
#
def lnThemesDirs( customization ) :
	print( 'Linking wp-content/themes directories for customization ' + customization + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + customization + '/wp-content/themes'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/wp-content/themes'
	wpContentThemes = listdir( rootedSourceDir )
##	print( 'lnThemesDirs: rootedSourceDir = ' + rootedSourceDir )
##	print( 'lnThemesDirs: destinationDir = ' + destinationDir )
##	print( 'lnThemesDirs: wpContentThemes = ', end="" )
##	print( wpContentThemes )
	for themeDir in wpContentThemes :
		rootedThemeDir = rootedSourceDir + '/' + themeDir
		if( isdir(rootedThemeDir) ) :
			print( '\tlinking "' + rootedThemeDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = "    cd " + destinationDir + ";\n    ln -fs " + rootedThemeDir + " .;\n    cd " + htdocsDir 
			print( "lnCommand:\n" + lnCommand )
			call( lnCommand, shell=True )

##
#  Driver function to call other functions to link specific types of customizations
#
def lnCustomization( customization ) :
	print( 'Linking files in the ' + customization + ' customization...' )
	wpContentDir = customizationsDir + '/'  + customization + '/' + 'wp-content'
	wpContentSubdirs = listdir( wpContentDir )
	wpContentSubdirs.sort()
	for subdirectory in wpContentSubdirs:
		if ( subdirectory == 'plugins' ) :
			lnPluginsDirs( customization )
		elif ( subdirectory == 'themes' ) :
			lnThemesDirs( customization )

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

for customization in customizations:
	lnCustomization( customization )

exit( exitVal )
