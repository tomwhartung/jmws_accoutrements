#!/usr/bin/python
#
# link_subsites.py: link subsites, like resume and idMyGadget, into top level dir of this site
# --------------------------------------------------------------------------------------------
#
import os
from os import chdir, getcwd, listdir
from os.path import isfile, isdir, islink
from subprocess import call

def checkForDirectory( dirToCheck ) :
	if isdir( dirToCheck ) :
		print( 'Found a ' + dirToCheck + ' directory, cool.' )
	else:
		print( 'Expecting a "' + dirToCheck + '" directory, but it is not here.' )
		print( 'The current directory is: "' + htdocsDir + '"' )
		print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
		exit( 1 )

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

checkForDirectory( subsitesDir )   # exits if directory not present
checkForDirectory( mainSiteDir )   # exits if directory not present

subsites = listdir( subsitesDir )
subsites.sort()
print( 'Linking the following subsites to ' + mainSiteDir + ':' )
print( subsites )

for subsite in subsites:
	linkSubsite( subsite )

exit( exitVal )
