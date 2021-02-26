import sys

def main():
    dic = {}
    lines = sys.stdin.read().strip().lower()
    punc = ".?,-"
    for char in lines:
        if char in punc:
            lines = lines.replace(char, "", 1)

    all_words = lines.strip().split()
    for word in all_words:
        if len(word) > 3 and all_words.count(word) >= 3:
            dic[word] = all_words.count(word)

    max_word_width = len(max(dic.keys(), key=len))
    max_number_width = len(str(max(dic.values())))

    for (k, v) in sorted(dic.items()):
       print("{:>{:d}s} : {:{:d}d}".format(k, max_word_width, v, max_number_width))

if __name__ == '__main__':
    main()
