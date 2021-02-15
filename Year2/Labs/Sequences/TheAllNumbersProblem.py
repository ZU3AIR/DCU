def get_evenodd_list():
    oddlist = []
    evenlist = []
    n = input()
    
    while int(n) != -1:
        if int(n) % 2 != 0:
            oddlist.append(int(n))
        if int(n) % 2 == 0:
            evenlist.append(int(n))
        n = input()
    return (oddlist, evenlist)
