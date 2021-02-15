def above_average(lst):
    a = [];l = sum(lst)/len(lst)
    for n in lst:
        if n > l:a.append(n)
    return a

print(above_average([1, 2, 3, 4, 5,]))