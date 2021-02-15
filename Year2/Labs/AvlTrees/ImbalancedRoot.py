def rotation_type(bst):
    rotate_type = ""
    ptr = bst.root
    while ptr != None:
        if ptr.left == None and ptr.right == None:
            return rotate_type
        if ptr.left == None:
            rotate_type += "r"
            ptr = ptr.right
        else:
            rotate_type += "l"
            ptr = ptr.left
    return rotate_type