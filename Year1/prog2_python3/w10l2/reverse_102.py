def reverse_list(x):
    if len(x) == 0:
        return []
    else:
        return [x[-1]] + reverse_list(x[:-1])
