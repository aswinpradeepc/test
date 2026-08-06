#!/bin/bash

if [ $# -eq 0 ]; then
	echo "usage ./q1 <name>"
	exit 1
fi
if [ $# -gt 1 ]; then
	echo "only 1 argument is accepted"
	exit 1


echo "name $1"
