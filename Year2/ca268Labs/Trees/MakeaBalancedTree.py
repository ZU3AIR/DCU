#   Arrange a list so that when added to a tree will cause the tree to be completely balanced
#
def make_list(lst):
	notlast = sorted(lst)
	last = []
	last2 = []
	last.append(notlast.pop(len(lst)//2))
	if len(notlast) > 0:
		last2.append(notlast[:len(lst)//2])
		last2.append(notlast[len(lst)//2:])
		
		while len(last) != len(lst):
			
			if last2[0] != []:
				last.append(last2[0][len(last2[0])//2])
				a = last2.pop(0)
				last2.append(a[:len(a)//2])
				last2.append(a[len(a)//(2+1):])
			else:
				last2.pop(0)
	
	return last