#!/bin/bash
if [ $# -eq 0 ]; then
	echo "usage $0 <name>"
	exit 1
fi
# how to check if the input is a number ? 
count=0
sum=0
while [ $count -le $1 ]; do
	count=$(($count + 1))
	sum=$(($sum + $count))
	echo "count $count"
	echo "sum $sum"
	echo
done
