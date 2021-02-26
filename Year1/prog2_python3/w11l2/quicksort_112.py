
def quicksort(A, b, c):
   if c <= b:
      return
   x = partition(A, b, c)
   quicksort(A, b, c - 1)
   quicksort(A, x + 1, c)

def partition(A, b, c):
   x = j = b
   while j < c:
      if A[j] <= A[c]:
         A[x], A[j] = A[j], A[x]
         x += 1
      j += 1
   A[x], A[c] = A[c], A[x]
   return x
