import math

def process_one():
    N = int(input())
    H, C, L = [int(x) for x in input().split()]

    C1 = N * H
    C2 = N * C

    Area = (math.sqrt((C1 ** 2) + (C2 ** 2)) * L)/10000

    print("%.4f" % Area)

try:
    while True:
        process_one()
except EOFError:
    pass