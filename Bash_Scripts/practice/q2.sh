#!/bin/bash

if [ $# -eq 0 ]; then
	echo "usage ./q2.sh <arg>"
	exit 1
fi
if [ -f $1 ]; then
	echo "the argument given, $1 is a file"
elif [ -d $1 ]; then
	echo "the argument given, $1 is a directory"
fi
exit 0
