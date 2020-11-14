class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, value):
        x = (((value.x - self.x) ** 2) + (value.y - self.y) ** 2) ** 0.5
        return x

    def __str__(self):
        x = "({:.1f}, {:.1f})".format(self.x, self.y)
        return x

class Segment():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        x = ((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)
        return x

    def length(self):
        x = self.p1.distance(self.p2)
        return x

class Circle():
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def overlaps(self, value):
        x = self.radius + value.radius > self.centre.distance(value.centre)
        return x
