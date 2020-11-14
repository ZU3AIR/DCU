#!/usr/bin/env python

n = input()

if n == 11:
    print "th"

elif n == 12:
    print "th"

elif n == 13:
    print "th"

elif n % 10 == 1:
    print "st"

elif n % 10 == 2:
    print "nd"

elif n % 10 == 3:
    print "rd"

else:
    print "th"
