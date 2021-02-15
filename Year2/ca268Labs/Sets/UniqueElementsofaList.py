def unique_list(list1):
    list2 = []
    for content in list1:
        if content not in list2:
            list2.append(content)
    return list2