import sys

def best_mark(s):
   try:
      f = open(s, "r")
      best_mark = 0
      best_name = ""
      for line in f:
         details = line.split()
         mark = int(details[0])
         name = " ".join(details[1:])
         if mark > best_mark:
            best_mark = mark
            best_name = name

      print ("Best student: {:s}".format(best_name))
      print ("Best mark: {:d}".format(best_mark))
      f.close()
   except(FileNotFoundError):
      print ("The file", s, "could not be opened.")
def main():
   s = sys.argv[1]
   best_mark(s)

if __name__ == "__main__":
   main()
