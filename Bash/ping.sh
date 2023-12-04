#!/bin/bash
echo "Number of argument typed : $#" #$# return the number of argument 
if [ "$#" -ne 2 ]; then
	echo "Argument shoud be : ./test.sh <startip>  <endip> "
	exit
fi 
start_ip=$1 
end_ip=$2
ping_sweep(){
	for ((i=start_ip;i<=end_ip;i++)); do
		ip=10.0.2.$i 
		echo $ip
		ping -c 1 -W 2  $ip  &>/dev/null 
		if [ $? -eq  0 ]; then 
			echo "$ip Host is up"
		else 
			echo "$ip Host is down"
		fi 
	done 
}
ping_sweep
