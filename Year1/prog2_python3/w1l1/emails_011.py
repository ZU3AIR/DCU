import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        i = 0
        while i < len(line) and not line[i] == ".":
            i += 1

        x = i
        while x < len(line) and (line[x] < "0" or line[x] > "9"):
            x += 1

        print(line[:i].capitalize() + " " + line[i + 1:x].capitalize())
if __name__ == '__main__':
    main()
