from math import sqrt


def fid(x):
    return x


def Input(filename, split=str.split, mapt=int):
    with open(filename) as fo:
        if split:
            source = split(fo.read())
        else:
            source = fo.read()
        if mapt:
            return list(map(mapt, source))
        else:
            return source


def split(char):
    return lambda x: x.split(char)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = (x, y)
        self.m = abs(x) + abs(y)

    def __add__(self, c):
        return Point(self.x + c.x, self.y + c.y)

    def __mul__(self, c):
        return self.x * c.x + self.y * c.y

    def length_sq(self):
        return self.x * self.x + self.y * self.y

    def norm(self):
        # normalize vector
        norm = sqrt(self.x * self.x + self.y * self.y)
        return Point(self.x / norm, self.y / norm)

    def __sub__(self, c):
        return Point(self.x - c.x, self.y - c.y)

    def __eq__(self, c):
        return self.x == c.x and self.y == c.y

    def __iter__(self):
        return self.t.__iter__()

    def __repr__(self):
        return "Point" + self.t.__repr__()

    def __hash__(self):
        return hash(self.t)
