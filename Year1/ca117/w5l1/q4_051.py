import sys

def main():
    lines = sys.stdin.read().strip().split()
# Mean
    total = 0
    for number in lines:
        total = total + int(number)
    mean = total / len(lines)
# Median
    if len(lines) % 2 != 0:
        sorted_lines = sorted(lines)
        median = (sorted_lines[(len(lines)) // 2])

    elif len(lines) % 2 == 0:
        sorted_lines = sorted(lines)
        half = sorted_lines[len(lines) // 2]
        x = sorted_lines[len(lines) // 2 - 1]
        median = (int(half) + int(x)) / 2

    print("Mean: {:.2}".format(float(mean)))
    print("Median: {:.2}".format(float(median)))
if __name__ == '__main__':
    main()
