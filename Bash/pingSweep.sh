#!/bin/bash
echo "Enter the  subnet (ex: 192.132.123): "
read subnet 
for ip in $(seq 1 254); do 
	ping -c 3 $subnet.$ip
	
done 
