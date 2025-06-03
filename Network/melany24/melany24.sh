#!/bin/bash
 if [ "$1" == "" ]
 then
 echo "IP address missing!!"
 echo "Correct synthax is a 3 bytes address: ./melany24.sh 192.168.1"
 else
 for ip in `seq 1 254`; do
 ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
 done
 fi
