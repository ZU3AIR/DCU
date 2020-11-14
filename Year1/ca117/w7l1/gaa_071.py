class Score():

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, extra):
        x = (self.goals * 3 + self.points) > (extra.goals * 3 + extra.points)
        return x

    def less_than(self, extra):
        x = (self.goals * 3 + self.points) < (extra.goals * 3 + extra.points)
        return x

    def equal_to(self, extra):
        x = (self.goals * 3 + self.points) == (extra.goals * 3 + extra.points)
        return x
