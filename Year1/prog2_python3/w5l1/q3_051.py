import sys

def main():
    lines = sys.stdin.read().strip().split()
    for word in lines:
        only_up = []
        for char in word:
            if char.isupper():
                only_up.append(char)
            else:
                only_up.append("x")
        upper = "".join(only_up)
        upper = upper.split("x")
        print(max(upper, key=len))

if __name__ == '__main__':
    main()
