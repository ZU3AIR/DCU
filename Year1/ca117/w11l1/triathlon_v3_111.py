class Triathlete(object):

   def __init__(self, n, id):
      self.n = n
      self.id = id

   def add_time(self, s, time):
      if s == "cycle":
         self.cycle = time
      if s == "swim":
         self.swim = time
      if s == "run":
         self.run = time

   def get_time(self, s):
      if s == "cycle":
         return self.cycle
      if s == "swim":
         return self.swim
      if s == "run":
         return self.run

   def __eq__(self, x):
      return self.run + self.cycle + self.swim == x.run + x.cycle + x.swim

   def __gt__(self, x):
      return self.run + self.cycle + self.swim > x.run + x.cycle + x.swim

   def __str__(self):
      lst = []
      lst.append("Name: {}".format(self.n))
      lst.append("ID: {}".format(self.id))
      lst.append("Race time: {}".format(self.run + self.cycle + self.swim))
      return "\n".join(lst)

class Triathlon(object):

   def __init__(self):
      self.s = {}

   def add(self, t1):
      self.s[t1.id] = t1

   def lookup(self, t1):
      try:
         return self.s[t1]
      except:
         return None

   def best(self):
      return min(self.s.values())

   def worst(self):
      return max(self.s.values())

   def __str__(self):
      lst = []
      for path in sorted(self.s.values(), key=lambda x: x.n):
         lst.append("Name: {}".format(path.n))
         lst.append("ID: {}".format(path.id))
      return "\n".join(lst)

   def remove(self, t1):
      del self.s[t1]
