#!/usr/bin/env python

s = raw_input()
x = ""
i = 0
while i < len(s):
   x = x + s[len(s) - i - 1]
   i = i + 1

if x == s:
   print "palindrome"
