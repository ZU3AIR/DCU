#!/bin/sh

for FOD in "$@"	#loops through all
do
	if [ -f $FOD ]	#if file is true
	then
		echo $FOD file
	elif [ -d $FOD ] #if direc is true
	then
		echo $FOD directory
	else
		echo "$FOD does not exist"
	fi
done