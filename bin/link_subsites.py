#!/usr/bin/python
#
# link_subsites.py: link subsites, like resume and idMyGadget, into top level dir of this site
# --------------------------------------------------------------------------------------------
#
import os
from os import chdir, getcwd, listdir
from os.path import isfile, isdir, islink
from subprocess import call


def linkModuleDirs( extension ) :
	print( 'Linking modules directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + subsitesDir + '/' + extension + '/modules'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/modules'
	moduleDirs = listdir( rootedSourceDir )
	### print( 'linkModuleDirs test: rootedSourceDir = ' + rootedSourceDir )
	### print( 'linkModuleDirs test: destinationDir = ' + destinationDir )
	### print( 'moduleDirs:' )
	### print( moduleDirs )
	for modDir in moduleDirs:
		rootedModuleDir = rootedSourceDir + '/' + modDir
		if( isdir(rootedModuleDir) ) :
			print( '\tlinking "' + rootedModuleDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedModuleDir + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )


def linkSubsite( extension ) :
	print( 'Linking files in the ' + extension + ' extension...' )
	githubRepoDir = subsitesDir + '/'  + extension
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

subsitesDir = 'subsites'
mainSiteDir = 'joomoowebsites.com'
htdocsDir = getcwd()
exitVal = 0

if isdir( subsitesDir ) :
	print( 'Found a ' + subsitesDir + ' directory, cool.' )
else:
	print( 'Expecting a "' + subsitesDir + '" directory, but it is not here.' )
	print( 'The current directory is: "' + htdocsDir + '"' )
	print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
	exit( 1 )

if isdir( mainSiteDir ) :
	print( 'Found a ' + mainSiteDir + ' directory, cool.' )
else:
	print( 'Expecting a "' + mainSiteDir + '" directory, but it is not here.' )
	print( 'The current directory is: "' + htdocsDir + '"' )
	print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
	exit( 1 )

subsites = listdir( subsitesDir )
subsites.sort()
print( 'Linking the following subsites to ' + mainSiteDir + ':' )
print( subsites )

### for extension in subsites:
	### linkSubsite( extension )

## onlyfiles = [ f for f in listdir(currentDir) if isfile(join(currentDir,f)) ]
## print( onlyfiles )

s1 = 'Goodbye world'
print(s1)

exit( exitVal )
