import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1: Point, p2: Point):
    return math.sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))

def angle(p1: Point, p2: Point, p3: Point):
    p12 = dist(p1, p2)
    p13 = dist(p1, p3)
    p23 = dist(p2, p3)
    return math.arccos((p12 ** 2 + p13 ** 2 - p23 ** 2)/(2 * p12 * p13))

def is_convex(p1, p2, p3, p4):
    if angle(p1, p2, p4) < 180 and \
        angle(p2, p1, p3) < 180 and \
            angle(p3, p2, p4) < 180 and \
                angle(p4, p3, p1):
                return True

def process_one():
    A, B, C, D = [float(x) for x in input().split()]

    if A == B == C == D == 0:
        return False

    print("%.5f" % ((C/D) * ((A/2) + B)))

    return True
