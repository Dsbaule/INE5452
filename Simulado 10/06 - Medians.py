import math

def process_one():
    m1, m2, m3 = [float(x) for x in input().split()]

    try:
        Area = (1/3) * math.sqrt((2 * ((m1**2 * m2**2) + (m2**2 * m3**2) + (m3**2 * m1**2))) - (m1**4 + m2**4 + m3**4))
    except:
        Area = -1

    if Area == 0:
        Area = -1

    print("%.3f" % Area)

try:
    while True:
        process_one()
except EOFError:
    pass