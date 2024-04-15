#!/bin/bash
read -p "Enter number of elements in the series :" n

num1=0
num2=1
next_num=0


for((i=0; i<n; i++)); do 
echo "$next_num "
num1=$num2
num2=$next_num
next_num=$(($num1+$num2))
done 

echo
