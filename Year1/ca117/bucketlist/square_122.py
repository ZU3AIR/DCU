import sys
import math

def trim(a):
    trimmed = []
    for x in a:
        if "\n" in x:
            trimmed.append(x[:-1])
        else:
            trimmed.append(x)
    return trimmed

def distance(a, b, c, d):
    distance = math.sqrt((c - a) ** 2 + (d - b) ** 2)
    return distance

def main():
    lines = sys.stdin.readlines()
    line = trim(lines)

    new_list = []
    i = 0
    while i < len(lines):
        lines[i] = lines[i].split()
        new_list.append(lines[i])
        i = i + 1

    x1 = (new_list[0][0])
    y1 = (new_list[0][1])

    x2 = (new_list[1][0])
    y2 = (new_list[1][1])

    x3 = (new_list[2][0])
    y3 = (new_list[2][1])

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)

    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x2, y2, x3, y3)
    d3 = distance(x3, y3, x1, y1)

    if d1 > d2:
        print(x1 + x2 - x3, y1 + y2 - y3)
    elif d2 > d3:
        print(x2 + x3 - x1, y2 + y3 - y1)
    elif d3 > d1:
        print(x3 + x1 + x2, y3 + y1 - y2)

if __name__ == '__main__':
    main()
