import sys

def main():
    s = sys.argv[1]
    n = sys.argv[2]
    if int(n) > len(s):
        x = int(n) % len(s)
        print(s[x:] + s[:x])
    else:
        print(s[int(n):] + s[:int(n)])

if __name__ == '__main__':
    main()
