#!/usr/bin/env python

s = raw_input()

i = 1
while i < len(s) and not (s[i] == s[i - 1]):
   i = i + 1

if i < len(s):
   print s[i - 1] + s[i]
