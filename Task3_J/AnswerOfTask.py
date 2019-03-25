import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lengthBetweenPoints(self, other):
        return math.sqrt((other.x - self.x) ** 2 +
                         (other.y - self.y) ** 2)

    def __str__(self):
        return str((self.x, self.y))


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def checkIntersection(self, other):
        det = self.a * other.b - other.a * self.b
        if det == 0:
            return
        x = (other.c * self.b - self.c * other.b) / det
        y = (other.c * self.a - self.c * other.a) / det
        return Point(x, y)

    def __str__(self):
        return "%.1fx+%.1fy+%.1fc=0" % (self.a, self.b, self.c)


def getNearest(lines):
    points = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            point = lines[i].checkIntersection(lines[j])
            if point:
                points.append((point, lines[i], lines[j]))

    if len(points) == 0:
        return
    else:
        return min(points, key=lambda m: m[0].lengthBetweenPoints(Point(0, 0)))


def Lines(lines):
    lin = []
    for i in range(len(lines)):
        el = Line(lines[i][0], lines[i][1], lines[i][2])
        lin.append(el)
    return getNearest(lin)
