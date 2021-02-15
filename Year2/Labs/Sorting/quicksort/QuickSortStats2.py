def partition(lst, lo, hi):

    lst[lo],lst[(lo + hi) // 2] = lst[(lo + hi) // 2], lst[lo]
    global c, m
    m += 3
    part = lo
    
    while lo < hi:
        
        c += 1
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            c += 1
        
        while lst[hi] > lst[part]:
            hi -= 1
            c += 1
        
        c += 1
        if lo < hi:
            lst[hi], lst[lo] = lst[lo], lst[hi]
            m += 3

    if lst[part] > lst[hi]:
        lst[part], lst[hi] = lst[hi], lst[part]
        m += 3
    c += 1
        
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    
    global c, m
    m = 0
    c = 0
    rec_qsort(lst, 0, len(lst) - 1)
    
    return c, m