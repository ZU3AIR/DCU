def selection_sort(lst):
    m = 0
    c = 0
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(min_index + 1, len(lst)):
            c += 1
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        m += 3
    return c, m