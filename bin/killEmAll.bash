#!/bin/bash
#
# killEmAll.bash: kill processes that match the string, without further ado
# -------------------------------------------------------------------------
#
echo "Killing all \"$1\" processes!"
ps -aef | grep $1 | grep -v $$ | awk '{print $2;}' | xargs kill -9 2> /dev/null

