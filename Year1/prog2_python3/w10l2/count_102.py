def count_letters(x):
   if len(x) == 0:
      return 0
    return len(x) + count_letters(x[len(x):])
