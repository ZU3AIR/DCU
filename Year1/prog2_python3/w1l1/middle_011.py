import sys

def mid(s):
	value = (len(s) // 2 - 1)
	return s[int(value)]

def main():
	for line in sys.stdin:
		if len(line) % 2 == 0:
			middle = mid(line)
			print(middle)
		else:
			print("No middle character!")
if __name__ == '__main__':
	main() 