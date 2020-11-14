#!/usr/bin/env python

n = input()
t = 0
y = 0

if n > 0:
	t = t + n
else:
	y = y + n
pos = t
neg = y
while n != 0:
	n = input()
	if n > 0:
		pos = pos + n
	else:
		neg = neg + n

print neg , pos
