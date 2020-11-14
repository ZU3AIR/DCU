class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      LIST = []
      LIST.append("Name: {}".format(self.name))
      LIST.append("ID: {}".format(self.tid))
      return "\n".join(LIST)
