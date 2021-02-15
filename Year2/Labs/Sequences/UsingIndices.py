def get_counts(words):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for word in words:
        counter[len(word)] += 1
    return counter