def maximum(x):
   if len(x) == 1:
      return x[0]

   m = maximum(x[:-1])
   if x[-1] > m:
      return x[-1]
   else:
      return m
