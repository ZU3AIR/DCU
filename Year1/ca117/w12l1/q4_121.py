import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        words = [letter for letter in line]
        w = []
        w.append(words[0])
        for letter in words[1:]:
            if letter.isupper():
                w.append(" ")
                w.append(letter.lower())
            else:
                w.append(letter)
        print("".join(w))

if __name__ == '__main__':
    main()
