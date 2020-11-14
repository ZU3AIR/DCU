#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and not (s[i] == "."):
   i = i + 1
print s[:i]

j = i + 1
while j < len(s) and s[j] >= "0" and s[j] <= "9":
   j = j + 1

if i < len(s):
   print s[i + 1:j]
