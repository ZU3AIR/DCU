#!/usr/bin/env python

x1 = input()
y1 = input()
r1 = input()
x2 = input()
y2 = input()
r2 = input()

distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
sum_radi = r1 + r2

if distance < sum_radi:
    print "yes"
else:
    print "no"
