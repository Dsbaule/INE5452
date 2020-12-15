import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.used = False
    
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

def dist(p1: Point, p2: Point):
    return math.sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))

def angle(p1: Point, p2: Point, p3: Point):

    ang = math.degrees(math.atan2(p2.y - p1.y, p2.x - p1.x) - math.atan2(p3.y - p1.y, p3.x - p1.x))
    ang = ang + 360 if ang < 0 else ang
    #print(ang)
    return ang

    p12 = dist(p1, p2)
    p13 = dist(p1, p3)
    p23 = dist(p2, p3)
    return math.acos((p12 ** 2 + p13 ** 2 - p23 ** 2)/(2 * p12 * p13))

def is_convex(p1, p2, p3, p4):
    #print("%d %d %d %d" % (angle(p1, p2, p4), angle(p2, p1, p3), angle(p3, p4, p2),angle(p4, p1, p3)))
    try:
        if angle(p1, p2, p4) < 180 and \
            angle(p2, p3, p1) < 180 and \
                angle(p3, p4, p2) < 180 and \
                    angle(p4, p1, p3) < 180:
                        #print("CONVEX!!!! %d %d %d %d" % (angle(p1, p2, p4), angle(p2, p1, p3), angle(p3, p4, p2),angle(p4, p1, p3)))
                        return True
    except:
        return False
    return False


def line_intersection(p1, p2, p3, p4):

    line1 = [[p1.x, p1.y], [p3.x, p3.y]]
    line2 = [[p2.x, p2.y], [p4.x, p4.y]]

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y)

def area(p1, p2, p3, p4):
    mid = line_intersection(p1, p2, p3, p4)
    ang = angle(mid, p1, p2)
    return ((dist(p1, p3) * dist(p2, p4)) / 2) * math.sin(math.radians(ang))

def permutate(points, n = 0):
    if n > 3:
        return [[]]
    
    permutations = list()

    for point in points:
        if not point.used:
            point.used = True
            for permutation in permutate(points, n + 1):
                permutations.append([point] + permutation)
            point.used = False

    return permutations
            

def process_one():
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = [int(x) for x in input().split()]

    if all(x == 0 for x in [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]):
        return False

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)
    p5 = Point(x5, y5)

    permutations = permutate([p1, p2, p3, p4, p5])

    max_area = 0
    for p1, p2, p3, p4 in permutations:
        if is_convex(p1, p2, p3, p4):
            #print("CALCULATING!!!!!!!!!!")
            #print([p1, p2, p3, p4])
            cur_area = area(p1, p2, p3, p4)
            max_area = max(cur_area, max_area)

    print("%.0f" % max_area)

    return True

while process_one():
    pass