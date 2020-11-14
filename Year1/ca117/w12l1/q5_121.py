import sys

def mean(n):
    mean = sum(n) / len(n)
    return "{:.1f}".format(mean)

def sorter(t):
    return t[1]

def main():
    d = {}
    for line in sys.stdin:
        line = line.strip().split(":")
        name, total = line[0], line[1]
        total = [int(n)if n is not "X" else 0 for n in total.lstrip().split(",")]
        d[name] = mean(total)
    for k, v in sorted(d.items(), key=sorter, reverse=True):
        print("{}: {}".format(k, v))

if __name__ == '__main__':
    main()
