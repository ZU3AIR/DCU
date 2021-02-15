#!/bin/sh

i=1
for v in "$@"
do
	echo "$i. $v"
	i=$(( i + 1 ))
done