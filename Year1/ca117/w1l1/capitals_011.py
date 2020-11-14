import sys

def cap(s):
	return s.capitalize()

def main():
	for line in sys.stdin:
		capitalize = cap(line.strip()[:-1]) + cap(line.strip()[-1])
		if len(capitalize) > 1:
			print(capitalize)
if __name__ == '__main__':
	main()