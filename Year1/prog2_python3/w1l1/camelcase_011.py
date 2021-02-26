import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip().split()
        i = 0
        c = ""
        while i < len(line):
            cap_line = line[i].capitalize()
            c = c + cap_line + " "
            i += 1
        print(c.strip())

if __name__ == '__main__':
    main()
