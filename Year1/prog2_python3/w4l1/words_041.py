import sys

def main():
    dic = {}
    lines = sys.stdin.read().strip().lower()
    punc = ".?,"
    for char in lines:
        if char in punc:
            lines = lines.replace(char, "", 1)

    all_words = lines.strip().split()
    for word in all_words:
        dic[word] = all_words.count(word)
    for (k, v) in sorted(dic.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
