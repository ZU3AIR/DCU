def sumto(a, b):
	if int(a) == int(b):
		return a
	else:
		return a + (sumto((a + 1), b))

print(sumto(4, 10))