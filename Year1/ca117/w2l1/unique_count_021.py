import sys

def tok(a):
    total = 0
    for lis in a:
        total = total + len(lis)
    return total

def main():
    a = []
    lines = sys.stdin.readlines()
    for line in lines:
        l = line.strip().split()
        a.append(l)
    print(tok(a))
if __name__ == '__main__':
    main()
