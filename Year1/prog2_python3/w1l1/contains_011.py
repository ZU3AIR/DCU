#!/usr/bin/env python3

import sys

def con():
	pass

def main():
# First have to read lines
	lines = sys.stdin.readlines()
# Break lines into two
	for l in lines:
		l = l.strip().lower().split()
		[left, right] = [l[0], l[1]]
		print(len(left), len(right))

# Replacing proccess
	for letter in left:
		print(len(left), len(right))
		if len(left) > len(right):
			print("False")
		elif letter in right:
			new_right = right.replace(letter, "")
			print(new_right)
			print("True")
		else:
			print("False")

if __name__ == '__main__':
	main()
