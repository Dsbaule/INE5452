import math

PI = 3.141592654

def calc_catet_op(catet_adj, angulo):
    return math.tan((angulo/90) * (PI/2)) * catet_adj

def process_one():
    A, B, C = [float(x) for x in input().split()]
    print("%.2f" % ((C + calc_catet_op(B, A)) * 5))

try:
    while True:
        process_one()
except EOFError:
    pass