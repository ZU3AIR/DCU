import sys
from math import pi

def main():
    n = sys.argv[1]
    print("{:.{}f}".format(pi, int(n)))

if __name__ == '__main__':
    main()
