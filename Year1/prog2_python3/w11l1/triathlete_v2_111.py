class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

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

   def __str__(self):
      lst = []
      lst.append("Name: {}".format(self.name))
      lst.append("ID: {}".format(self.tid))
      lst.append("Race time: {}".format(self.run + self.cycle + self.swim))
      return "\n".join(lst)
