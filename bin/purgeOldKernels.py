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
import sys      # for accessing command line arguments
from subprocess import call      # for running commands

##
# syntax: print this script's syntax statement
#
def syntax() :
	print( 'purgeOldKernels.py kernelVersion' )
	print( '  Purges the specified version of the kernel.' )

##
# Get the kernel version, which must be supplied via a command line argument
#
def getKernelVersion () :
	kernelVersion = ''
	helpMessage = 'Run "dpkg -l | grep linux-image" and supply the numeric part (e.g., 3.13.0-55).'
	if ( len(sys.argv) == 1 ) :
		syntax()
		print( 'No kernel version specified!' )
		print( helpMessage )
		print( 'Exiting.' )
		exit( 1 )
	elif ( len(sys.argv) == 2 ) :
		if ( sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help' ) :
			syntax()
			print( helpMessage )
			exit( 0 )
		kernelVersion = sys.argv[1]
	else :
		print( 'Too many arguments, try again.' )
		exit( 1 )
	return kernelVersion

##
# Verify user is not trying to delete the kernel currently being used
#

kernelVersion = getKernelVersion()

print( 'Deleting kernel version ' + kernelVersion )

aptGetCommand  = 'apt-get purge '
aptGetCommand += 'linux-headers-' + kernelVersion + ' '
aptGetCommand += 'linux-headers-' + kernelVersion + '-generic '
aptGetCommand += 'linux-image-' + kernelVersion + '-generic '
aptGetCommand += 'linux-image-extra-' + kernelVersion + '-generic'

print( 'aptGetCommand:\n\t' + aptGetCommand )
call( aptGetCommand, shell=True )
