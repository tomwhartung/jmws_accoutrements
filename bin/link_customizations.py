#!/usr/bin/python
#
# link_customizations.py: hey why not do a version of this in python?
# ---------------------------------------------------------------------
#
import os
from os import chdir, getcwd, listdir
from os.path import isfile, isdir, islink
from subprocess import call

def linkLanguageFiles( extension ) :
	print( 'Linking language files for extension ' + extension + '...' )
	rootedSourceDir = htdocsDir + '/' + customizationsDir + '/' + extension + '/language/en-GB'
	destinationDir = htdocsDir + '/' + cmsDuJour + '/language/en-GB'
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
	destinationDir = htdocsDir + '/' + cmsDuJour + '/libraries/vendor'
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
	destinationDir = htdocsDir + '/' + cmsDuJour + '/modules'
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
	destinationDir = htdocsDir + '/' + cmsDuJour + '/templates'
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
cmsDuJour = 'joomla'
htdocsDir = getcwd()
### print( 'linkTemplateDirs test: htdocsDir = ' + htdocsDir )
exitVal = 0

if isdir( customizationsDir ) and islink( cmsDuJour ) :
	print( 'Found a ' + customizationsDir + ' dir and a ' + cmsDuJour + ' link, cool.' )
else:
	print( 'Expecting a "' + customizationsDir + '" directory and a "' + cmsDuJour + '" link, but they are not here.' )
	print( 'The current directory is: "' + htdocsDir + '"' )
	print( 'Change to a different directory, preferably one named "htdocs," and try again.' )
	exit( 1 )

customizations = listdir( customizationsDir )
customizations.sort()
print( 'Linking the following customizations to the appropriate directories in ' + cmsDuJour + ':' )
print( customizations )

for extension in customizations:
	linkExtension( extension )

## onlyfiles = [ f for f in listdir(currentDir) if isfile(join(currentDir,f)) ]
## print( onlyfiles )

## s1 = 'Goodbye world'
## print(s1)

exit( exitVal )
