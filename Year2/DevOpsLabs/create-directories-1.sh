#!/bin/sh

arg="$1"

for i in $(seq $arg)
do
	mkdir dir.$i
done