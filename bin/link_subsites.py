#!/usr/bin/python
#
# link_subsites.py: link subsites, like resume and idMyGadget, into top level dir of this site
# --------------------------------------------------------------------------------------------
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
#  Links the specified subsite directory into the main site directory
#
def linkSubsite( subsite ) :
	print( 'Linking the ' + subsite + ' subsite to ' + mainSiteDir + '...' )
	rootedSubsiteDir = htdocsDir + '/subsites/' + subsite
	lnCommand = 'cd ' + mainSiteDir + '; ln -fs ' + rootedSubsiteDir + ' .; cd ' + htdocsDir 
	print( "lnCommand:\n\t" + lnCommand )
	call( lnCommand, shell=True )

rootDir = '/var/www'
mainSites = ['joomoowebsites.com', 'tomhartung.com', 'tomwhartung.com' ]
subsitesDir = 'subsites'
exitVal = 0

for mainSiteDir in mainSites :
	htdocsDir = rootDir + '/' + mainSiteDir + '/htdocs'
	chdir( htdocsDir )
	printDir = getcwd()
	print( 'printDir: ' + printDir )
	checkForDirectory( subsitesDir )   # exits if directory not present
	checkForDirectory( mainSiteDir )   # exits if directory not present
	subsites = listdir( subsitesDir )
	subsites.sort()
	print( 'Linking the following subsites to ' + mainSiteDir + ':' )
	print( subsites )
	for subsite in subsites :
		linkSubsite( subsite )
	if ( 'idMyGadget' in subsites and 'resume' in subsites ) :   # The resume depends on idMyGadget, so if both are in the list
		print 'linking idMyGadget into parent directory of resume ...';
		lnCommand = 'cd subsites/resume; ln -fs ../idMyGadget . ; cd -'
		print "lnCommand:\n\t" + lnCommand
		call( lnCommand, shell=True )

exit( exitVal )
