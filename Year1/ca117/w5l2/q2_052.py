import sys

def main():
    control = list("aeiou")
    lines = sys.stdin.read().strip().split()
    for word in lines:
        test = []
        for char in word:
            if char.lower() in control:
                test.append(char)
        test2 = []
        for x in test:
            test2.append(x.lower())
        if control == test2:
            print(word)

if __name__ == '__main__':
    main()
