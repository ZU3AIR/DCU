import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

names = []
badnames = []

for line in open(file1):
	names.append(line)

for line2 in open(file2):
	if line2 in names:
		badnames.append(line2.strip())

badnames.sort()
i = 1
while i <= len(badnames):
	print("{}. {}".format(i, badnames[i - 1]))
	i += 1
