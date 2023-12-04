#!/bin/bash
echo "Enter path of the file of Name :"
read path
echo "The path is : $path"
for name in $(cat $path); do
	echo "The name is : $name "
done 

