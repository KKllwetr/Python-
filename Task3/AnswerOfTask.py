import math


def Intersect(a=[], b=[]):
    distance = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    r = a[2] + b[2]
    if distance >= r:
        return True
    else:
        return False
