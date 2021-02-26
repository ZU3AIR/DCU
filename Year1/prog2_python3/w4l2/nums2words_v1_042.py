import sys

dic = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

def main():
    for line in sys.stdin:
        numbers = line.strip().split()
        s = ""
        for number in numbers:
            if number in dic:
                s = s + " " + dic[number]
        print(s.strip())

if __name__ == '__main__':
    main()
