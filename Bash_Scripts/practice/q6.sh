#!/bin/bash

if [ ! -e $1 ]; then
	echo "a dir named $1 does not exist"
	exit 1
fi

if [ ! -d $1 ]; then
	echo "$1 is not a dir"
	exit 1
fi
echo "number of files $(ls -l $1 | wc -l)"
echo "largest file $(ls -l $1 | awk '{print $5, $9}' | sort -rn | head -n1)"
echo "today's date is $(date)"
