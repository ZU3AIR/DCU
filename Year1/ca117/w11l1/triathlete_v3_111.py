class Triathlete(object):

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.t = {}

    def __eq__(self, x):
        return sum(self.t.values()) == sum(x.t.values())

    def __gt__(self, x):
        return sum(self.t.values()) > sum(x.t.values())

    def __lt__(self, x):
        return sum(self.t.values()) < sum(x.t.values())

    def add_time(self, s, time):
        self.t[s] = time

    def get_time(self, s):
        return self.t[s]

    def __str__(self):
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.id, sum(self.t.values()))
