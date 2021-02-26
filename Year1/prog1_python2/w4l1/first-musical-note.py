#!/usr/bin/env python

s = raw_input()

x = 0
i = 0
while s[i] != ("f" or "b" or "c" or "d" or "e" or "a" or "g"):
	x = x + 1
	i = i + 1
print s[x]
