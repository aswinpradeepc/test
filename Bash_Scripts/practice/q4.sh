#!/bin/bash
if [ ! -d $1 ]; then
	echo "argument should be a directory"
	exit 1
fi
ls -l $1 | awk '{print $5, $9}' | sort -rn | head -n5
#du -h $1 | sort -rn | head -n5
