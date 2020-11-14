import sys

def match(x1, x2):
    k = []
    i = 0
    while i < len(x1):
        if x1[i] == x2[i]:
            k.append(i)
        i = i + 1
    return k

def main():
    line = sys.stdin.readlines()
    x1 = line[0].split()
    x2 = line[1].split()
    print(match(x1, x2))

if __name__ == '__main__':
    main()
