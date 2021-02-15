#!/bin/sh

read a
read b

while [ "$a" != "$b" ]
do
	b="$a"
	read a
done
echo $a