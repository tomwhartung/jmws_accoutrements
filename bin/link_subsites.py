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


def linkSubsite( subsite ) :
	print( 'Linking the ' + subsite + ' subsite to ' + mainSiteDir + '...' )
	rootedSubsiteDir = htdocsDir + '/subsites/' + subsite
	lnCommand = 'cd ' + mainSiteDir + '; ln -fs ' + rootedSubsiteDir + ' .; cd ' + htdocsDir 
	print( "lnCommand:\n\t" + lnCommand )
	call( lnCommand, shell=True )

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

for subsite in subsites:
	linkSubsite( subsite )

exit( exitVal )
