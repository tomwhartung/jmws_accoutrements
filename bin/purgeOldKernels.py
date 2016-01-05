#!/usr/bin/python3
#
# purgeOldKernels.py: simple script (for now anyway) to save typing when purging old kernels
# ------------------------------------------------------------------------------------------
# There are automatic ways to do this (see first reference) but they sound a little risky to me.
# For now, I just want to do it manually, so I know what's happening, without doing a lot of typing.
# References:
#   https://help.ubuntu.com/community/Lubuntu/Documentation/RemoveOldKernels
#   http://elementaryos.stackexchange.com/questions/95/how-to-remove-old-kernel-versions
#
import sys                    # for accessing command line arguments
import subprocess             # for running a command and processing its output
from subprocess import call   # for running shell commands

##
# syntax: print this script's syntax statement
#
def syntax() :
	print( 'purgeOldKernels.py [-h|-help|--help] kernelVersionToDelete' )
	print( '  E.g.: "purgeOldKernels.py 3.13.0-71"' )
	print( '  Purges the specified version of the kernel.' )

##
#  Print a helpful help message
#
def printHelpMessage() :
	kernelVersionCurrent = getKernelVersionCurrent()
	helpMessage  = '   Run "dpkg -l | grep linux-image" and supply the numeric part (e.g., 3.13.0-55).\n'
	helpMessage += '   Do NOT try to delete the current kernel (' + kernelVersionCurrent + ')!!!'
	print( helpMessage )

##
# Get the kernel version, which must be supplied via a command line argument
#
def getKernelVersionToDelete () :
	kernelVersionToDelete = ''
	if ( len(sys.argv) == 1 ) :
		syntax()
		print( 'No kernel version specified!' )
		printHelpMessage()
		print( 'Exiting.' )
		exit( 1 )
	elif ( len(sys.argv) == 2 ) :
		if ( sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help' ) :
			syntax()
			printHelpMessage()
			exit( 0 )
		kernelVersionToDelete = sys.argv[1]
	else :
		print( 'Too many arguments, try again.' )
		exit( 1 )
	return kernelVersionToDelete

##
# Returns a printable version of the output of the uname -r command
#
def getUnameDashROutput() :
	getUnameProcess = subprocess.Popen( ['uname', '-r'], stdout=subprocess.PIPE )
	unameBytes = getUnameProcess.stdout.read()
	unameOutput = unameBytes.decode('utf-8')
	return unameOutput

##
# Returns a printable version of the output of the uname -r command
#
def getKernelVersionCurrent() :
	unameDashROutput = getUnameDashROutput()
	kernelVersionCurrent = unameDashROutput[0:9]     # TODO: use a regex here!
	return kernelVersionCurrent

##
# Verify user is not trying to delete the kernel currently being used
#
def checkKernelVersion( kernelVersionToDelete ) :
	kernelVersionCurrent = getKernelVersionCurrent()
	foundKernelVersion = kernelVersionCurrent.find( kernelVersionToDelete )
	print( 'kernelVersionCurrent: ' + kernelVersionCurrent )
	print( 'kernelVersionToDelete: ' + kernelVersionToDelete )
	print( 'str(foundKernelVersion): ' + str(foundKernelVersion) )
	if( foundKernelVersion > -1 ) :
		print( '*** ERROR!  You cannot delete the current kernel!' )
		print( '*** Dude, get your shit together and try again!' )
		exit( 9 )

##
#  Main program starts here
#  ------------------------
#
kernelVersionToDelete = getKernelVersionToDelete()
checkKernelVersion( kernelVersionToDelete )

print( 'Deleting kernel version ' + kernelVersionToDelete )

aptGetCommand  = 'apt-get purge '
aptGetCommand += 'linux-headers-' + kernelVersionToDelete + ' '
aptGetCommand += 'linux-headers-' + kernelVersionToDelete + '-generic '
aptGetCommand += 'linux-image-' + kernelVersionToDelete + '-generic '
aptGetCommand += 'linux-image-extra-' + kernelVersionToDelete + '-generic'

print( 'aptGetCommand:\n\t' + aptGetCommand )
### call( aptGetCommand, shell=True )

exit( 0 )
