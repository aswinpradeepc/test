#!/bin/bash
cd $1
for i in *.txt; do
#	echo $i
	wc -l $i
done
