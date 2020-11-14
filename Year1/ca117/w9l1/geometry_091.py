class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, ext):
        return (((ext.x - self.x) ** 2) + ((ext.y - self.y) ** 2)) ** 0.5

class Shape(object):

    def __init__(self, pts):
        self.pts = pts

    def sides(self):
        return [self.pts[i].distance(self.pts[i + 1]) if i < (len(self.pts) - 1) else self.pts[i].distance(self.pts[0]) for i in range(len(self.pts))]

    def perimeter(self):
        return sum(self.sides())


class Triangle(Shape):

    def area(self):
        s = self.perimeter() / 2
        a, b, c = self.sides()

        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Square(Shape):

    def area(self):
        a, b, _, _ = self.sides()
        return a * b
