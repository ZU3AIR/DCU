#!/usr/bin/env python

n = input()
prev = 0
curr = 1
i = 0

while i < n:
    if prev < n:
        print prev
        old_curr = curr
        curr = curr + prev
        prev = old_curr
    i = i + 1
