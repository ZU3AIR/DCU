import sys
arg = sys.argv[1]
if (len(arg)) % 2 == 0:print(arg[int(len(arg)/2):])
else:print(arg[0] + arg[-1])