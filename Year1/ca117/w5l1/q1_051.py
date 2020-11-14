import sys

def main():
    line = sys.argv[1]
    word = list(line)
    if len(word) > 1:
        i = 1
        while i < len(word):
            word[i - 1], word[i] = word[i], word[i - 1]
            i += 2
        print("".join(word))
    else:
        print(line)
if __name__ == '__main__':
    main()
