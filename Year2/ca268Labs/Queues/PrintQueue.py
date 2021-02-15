from Queue import Queue

def print_queue(_list, f, b):
    if f > b:
        return _list[f:] + _list[:b]
    elif f < b:
        return _list[f:b]