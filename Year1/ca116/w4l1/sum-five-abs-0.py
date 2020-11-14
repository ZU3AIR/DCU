#!/usr/bin/env python

n = input()

if n > 0:
	t = n
else:
	t = (n * -1)

total = t
while n != 0:
   n = input()
   if n > 0:
      total = total + n
   else:
      total = total + (n * -1)
print total 
