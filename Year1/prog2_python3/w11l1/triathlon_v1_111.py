class Triathlete(object):

    def __init__(self, n, id):
        self.name = n
        self.tid = id

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.a = {}

    def add(self, x):
        self.a[x.tid] = x

    def remove(self, x):
        self.a.pop(x)

    def lookup(self, x):
        if x in self.a:
            return self.a[x]
