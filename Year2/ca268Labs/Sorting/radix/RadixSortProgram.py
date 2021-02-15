def radixsort(lst, n):
    """ this function will sort lst using radixsort up to the required number of passes.
    Note that the first pass we will sort on the least significant bit.
    """
    for p in range(n):
        # Split list in two
        lo = [x for x in lst if x & (1 << p) == 0] # only where that bit is zero
        hi = [x for x in lst if x & (1 << p) != 0] # onlly where that bit is 1
        
        lst = lo + hi # combine the two lists (now sorted by that bit).
    return lst