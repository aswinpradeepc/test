#!/bin/bash
read -p "Enter the string :" s
rvs=$(echo "$s" | rev)
if [ "$rvs" == "$s" ]; then 
    echo "The string \"$s\" is a palindrome" # \" is an escape symbol to consider double quotes as the part of the string itself
    else 
    echo "The string \"$s\" is not a palindrome. " 
fi
