#!/bin/bash
read -p "Enter the number to find factorial :" n

factorial(){

if [ $1 -eq 0 ] || [ $1 -eq 1 ]; then
	echo 1
else 
	local fact=$(( $1 * $(factorial $(( $1 - 1 ))) ))
	echo "$fact"
fi
}
result=$(factorial "$n")
echo "Factorial of $n is $result"
