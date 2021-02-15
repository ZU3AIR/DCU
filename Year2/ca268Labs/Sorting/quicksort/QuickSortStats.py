def partition(lst, lo, hi):
    
    part = lo
    global m, c
    
    while lo < hi:
        
        c += 1
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            c += 1
        c += 1
        while lst[hi] > lst[part]:
            hi -= 1
            c += 1
    
        if lo < hi:
            lst[hi], lst[lo] = lst[lo], lst[hi]
            m += 3
    c += 1
    if lst[part] > lst[hi]:
        m += 3
        lst[part], lst[hi] = lst[hi], lst[part]
    
    return hi

def rec_qsort(lst, lo, hi):

    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    
    global m, c
    m = 0
    c = 0
    rec_qsort(lst, 0, len(lst) - 1)
    
    return c, m