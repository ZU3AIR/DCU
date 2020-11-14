class Triathlete(object):

   def __init__(self, name, tid):
      self.n = name
      self.id = tid

   def __str__(self):
      LIST = []
      LIST.append("Name: {}".format(self))
      LIST.append("ID: {}".format(self))
      return "\n".join(LIST)

class Triathlon(Triathlete):

   def __init__(self):
      self.d = {}

   def add(self, t1):
      self.d[t1.id] = t1

   def lookup(self, t1):
      try:
         return self.d[t1]
      except:
         return None

   def __str__(self):
      LIST = []
      for path in sorted(self.d.values(), key=lambda x: x.n):
         LIST.append("Name: {}".format(path.n))
         LIST.append("ID: {}".format(path.id))
      return "\n".join(LIST)

   def remove(self, t1):
      del self.d[t1]
