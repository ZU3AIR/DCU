#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and not (s[i] <= "9" and s[i] >= "0"):
   i = i + 1

j = i
while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
   j = j + 1

p = j
while p < len(s) and not (s[p] <= "9" and s[p] >= "0"):
   p = p + 1

l = p
while l < len(s) and (s[l] >= "0" and s[l] <= "9"):
   l = l + 1

if i < len(s):
   print s[p:l], p
