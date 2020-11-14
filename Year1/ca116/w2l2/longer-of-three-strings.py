#!/usr/bin/env python

l1 = raw_input()
l2 = raw_input()
l3 = raw_input()

if len(l1) > len(l2) and len(l1) > len(l3):
    print l1
elif len(l2) > len(l3) and len(l2) > len(l1):
    print l2
else:
    print l3
