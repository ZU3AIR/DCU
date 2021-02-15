def insertion_sort(lst):
    m = 0
    c = 0
    if len(lst) == 0:
        return

    min_index = 0
    for i in range(1, len(lst)):
        c += 1
        if lst[i] < lst[min_index]:
            min_index = i;

    lst[0], lst[min_index] = lst[min_index], lst[0]
    m += 3

    for todo in range(2, len(lst)):
        store = lst[todo]
        i = todo
        c += 1
        while store < lst[i-1]:
            c += 1
            lst[i] = lst[i-1]
            i -= 1
            m += 1
        m += 2
        lst[i] = store
    return c, m