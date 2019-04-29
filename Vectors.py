import math


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def normalize(self):
        abs = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        return Vector2(self.x / abs, self.y / abs)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dist(self, other):
        return math.sqrt(math.pow((self.x - other.x), 2) +
                         math.pow((self.y - other.y), 2))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "({x} {y})".format(x=self.x, y=self.y)


