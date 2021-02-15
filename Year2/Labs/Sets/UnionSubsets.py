def set_stuff(set1, set2):
    allsets = []
    union = set1.union(set2)
    AsubB = set1.issubset(set2)
    BsubA = set2.issubset(set1)
    allsets.append(union)
    allsets.append(AsubB)
    allsets.append(BsubA)
    return tuple(allsets)