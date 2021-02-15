def sum_to_k(l, k):
    val = []
    x = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == k:
                val.append(l[i])
                val.append(l[j])
    for t in val: 
        if t not in x: 
            x.append(t)
    z = 1
    while z < len(x):
        print(x[z - 1], x[z])
        z += 2
sum_to_k([1, 6, 7, 8, 9, 10, 2, 3, 4, 5], 13)