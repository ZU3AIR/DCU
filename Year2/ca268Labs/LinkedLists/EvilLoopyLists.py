def detect_loop(LIST):
    loop = LIST.head
    marker = LIST.head
    while marker != None:
        if marker.next == loop:
            return True
        marker = marker.next
    return False