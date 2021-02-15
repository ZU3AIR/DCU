import sys
arg = sys.argv[1]
i = 1
while i < len(arg):
	print(arg[i - 1] + arg[i])
	i += 1