#!/bin/sh

arg="$1"

for i in $(seq $arg)
do
	name=$(printf %06d $i) #googled formula/code
	mkdir dir.$name
done