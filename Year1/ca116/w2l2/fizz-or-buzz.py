#!/usr/bin/env python

value = input()

if value % 15 == 0:
    print "fizz-buzz"

elif value % 5 == 0:
    print "buzz"

elif value % 3 == 0:
    print "fizz"

else:
    print value
