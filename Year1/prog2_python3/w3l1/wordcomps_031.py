import sys

def main():
	lines = sys.stdin.read().strip().split()
	vowels = ""
	for word in lines:
		if "a" in word.lower() and "i" in word.lower() and "o" in word.lower() and "e" in word.lower() and "u" in word.lower():
			vowels = vowels + word + ","
	vowels = vowels.split(",")
#	
	sorted_vowels = min (vowels, key=len)
	print(sorted_vowels[0])
#	print("Words containing 17 letters: {}".format([n for n in lines if len(n) == 17]))
#	print("Words containing 18+ letters: {}".format([n for n in lines if len(n) >= 18]))
#	print("Shortest word containing all vowels: {}".format())

if __name__ == '__main__':
	main()
