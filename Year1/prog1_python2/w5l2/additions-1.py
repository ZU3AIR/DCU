#!/usr/bin/env python

i = 0
while i < 10:
   j = 0
   s = raw_input()
   while j < len(s) and not s[j] == "+":
      j = j + 1
   print int(s[:j]) + int(s[j + 1:])
   i = i + 1
