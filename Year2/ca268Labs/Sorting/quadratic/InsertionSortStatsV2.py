def insertion_sort(lst):
    m = 0
    c = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        m += 1
        c += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1]
            i -= 1
            if i != 0:
                c += 1
            m += 1
        lst[i] = tobeinserted
        m += 1
    return c, m