import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        uppercase = 0
        lowercase = 0
        digit = 0
        special = 0

        for char in line.strip():
            if char.isupper():
                uppercase = 1
            elif char.islower():
                lowercase = 1
            elif char.isdigit():
                digit = 1
            elif not char.isalpha():
                special = 1
        print(uppercase + lowercase + digit + special)
if __name__ == '__main__':
    main()
