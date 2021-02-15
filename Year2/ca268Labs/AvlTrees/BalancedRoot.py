def is_avl(bst):
    # Determine whether this bst is AVL balanced or not.
    left = bst.height()
    
    root = bst.root
    bst.root = bst.root.left
    
    left = bst.height()
    bst.root = root
    bst.root = bst.root.right
    right = bst.height()
    
    if left > right + 1 or right > left + 1:
        return False
    else:
        return True