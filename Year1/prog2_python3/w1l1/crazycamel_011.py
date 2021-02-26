import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip().split()
        text = ""
        i = 0
        while i < len(line):
            new_word = line[i][:-1] + line[i][-1].upper()
            text = text + new_word + " "
            i += 1
        print(text.strip())

if __name__ == '__main__':
    main()
