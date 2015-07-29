#!/usr/bin/python
#
# link_customizations.py: hey why not do a version of this in python?
# ---------------------------------------------------------------------
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

def linkLanguageFiles( extension ) :
	print( 'Linking language files for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/language/en-GB'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/language/en-GB'
	languageFiles = listdir( rootedSourceDir )
	### print( 'linkLanguageFiles: rootedSourceDir = ' + rootedSourceDir )
	### print( 'linkLanguageFiles: destinationDir = ' + destinationDir )
	### print( 'languageFiles:' )
	### print( languageFiles )
	for langFile in languageFiles:
		rootedLanguageFile = rootedSourceDir + '/' + langFile
		if( isfile(rootedLanguageFile) ) :
			print( '\tlinking "' + rootedLanguageFile + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedLanguageFile + ' .; cd ' + htdocsDir 
		### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )

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

def linkModuleDirs( extension ) :
	print( 'Linking modules directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/modules'
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

def linkTemplateDirs( extension ) :
	print( 'Linking templates directories for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/templates'
	destinationDir = htdocsDir + '/' + mainSiteDir + '/templates'
	templateDirs = listdir( rootedSourceDir )
	### print( 'linkTemplateDirs test: rootedSourceDir = ' + rootedSourceDir )
	### print( 'linkTemplateDirs test: destinationDir = ' + destinationDir )
	### print( 'templateDirs:' )
	### print( templateDirs )
	for tmplDir in templateDirs:
		rootedTemplateDir = rootedSourceDir + '/' + tmplDir
		if( isdir(rootedTemplateDir) ) :
			print( '\tlinking "' + rootedTemplateDir + "\" to\n\t\t\"" + destinationDir + '"' )
			lnCommand = 'cd ' + destinationDir + '; ln -fs ' + rootedTemplateDir + ' .; cd ' + htdocsDir 
			### print( 'lnCommand: ' + lnCommand )
			call( lnCommand, shell=True )

def linkExtension( extension ) :
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
mainSiteDir = 'joomoowebsites.com'
htdocsDir = getcwd()
exitVal = 0

checkForDirectory( customizationsDir )   # exits if directory not present
checkForDirectory( mainSiteDir )         # exits if directory not present

customizations = listdir( customizationsDir )
customizations.sort()
print( 'Linking the following customizations to the appropriate directories in ' + mainSiteDir + ':' )
print( customizations )

for extension in customizations:
	linkExtension( extension )

exit( exitVal )
