#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b <= c:
    print "no"
elif a + c <= b:
    print "no"
elif b + c <= a:
    print "no"
else:
    print "yes"
