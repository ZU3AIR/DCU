#
#   Test whether the BST is maximal
#
def is_maximal(bst):
	z = bst.count()
	num = 1
	i = 0
	while num < z:
		num = num + 2 ** (i + 1)
		i += 1
	if num == z and i == bst.height() - 1:
		return True
	return False