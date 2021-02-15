#!/bin/sh

num="$1"
i=1
echo $num
while [ $num != 1 ] 
do
    if [ $((num % 2)) -eq 0 ]
    then
        num=$((num / 2))
        echo $num
    else
        num=$((num * 3 + 1))
        echo $num
    fi
done
