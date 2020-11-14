class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def distance(self, new_point):
        distance = ((new_point.x - self.x) ** 2 + (new_point.y - self.y) ** 2) ** 0.5
        return distance
