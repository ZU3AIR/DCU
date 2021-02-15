def selection_sort(lst):
    lo = 0
    hi = len(lst) - 1
    c = 0
    m = 0
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            c += 1
            if lst[j] < lst[min_index]:
                min_index = j
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                c += 1
            else:
                c += 1
        if max_index == lo:
            max_index = min_index
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        m += 3
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        m += 3
        lo += 1
        hi -= 1
    return c, m