def get_sliced_lists(longlist):
    megalist = []

    list1 = longlist[:-1]
    list2 = longlist[1:-1]
    list3 = longlist[::-1]
    
    megalist.append(list1)
    megalist.append(list2)
    megalist.append(list3)
    
    return megalist
    