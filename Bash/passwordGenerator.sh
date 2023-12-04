#!/bin/bash
echo "______PASSWORD GENERATOR_______"
echo "Enter the length of passowrd you want : "
read length 
echo "Enter the number of  password you want: "
read number
for i in $(seq 1 $number); do 
    openssl rand -base64  48 | cut  -c1-$length 

done 
