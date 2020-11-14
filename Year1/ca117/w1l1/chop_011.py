#!/usr/bin/env python

import sys

def main():
	for line in sys.stdin:
		chopped = line[1:-1]
		chopped = chopped.strip()
		if len(chopped) > 0:
			print(chopped)
if __name__ == '__main__':
	main()
