#!/usr/bin/env python

n = input()
curr = 0
prev = n

while n != 0:
   n = input()
   curr = n
   if n != 0:
      if n > prev:
         print "higher"
         prev = curr
      elif prev > n:
         print "lower"
         prev = curr
      else:
         print "equal"
         prev = curr
