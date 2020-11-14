#!/usr/bin/env python

n = input()
curr = 0
prev = n

i = 0
while i < 5:
   n = input()
   curr = n
   if n > prev:
      print "higher"
      prev = curr
   elif prev > n:
      print "lower"
      prev = curr
   else:
      print "equal"
      prev = curr
   i = i + 1
