def even_count(LIST):
    total = 0
    pointer = LIST.head
    while pointer != None:
        if pointer.item % 2 == 0:
            total += 1
            pointer = pointer.next
        else:
            pointer = pointer.next
    return total