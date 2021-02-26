import sys

def pal(s):
    if s == s[::-1]:
        return True
    else:
        return False

def main():
    for lines in sys.stdin:
        lines = lines.strip().lower()
        for char in lines:
            if char.isalnum() is False:
                lines = lines.replace(char, "")
        print(pal(lines))
if __name__ == '__main__':
    main()
