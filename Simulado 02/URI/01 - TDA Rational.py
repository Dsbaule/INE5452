from math import gcd

def calc(input_string):
    n1, _, d1, op, n2, _, d2 = input_string.split()

    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if op == '+':
        numerator = (n1 * d2) + (n2 * d1)
        denominator = (d1 * d2)
    elif op == '-':
        numerator = (n1 * d2) - (n2 * d1)
        denominator = (d1 * d2)
    elif op == '*':
        numerator = (n1 * n2)
        denominator = (d1 * d2)
    elif op == '/':
        numerator = (n1 * d2)
        denominator = (n2 * d1)

    if numerator == 0:
        out_string = f'{numerator}/{denominator} = 0/1'
    else:
        out_string = f'{numerator}/{denominator} = {numerator//gcd(numerator,denominator)}/{denominator//gcd(numerator,denominator)}'

    return out_string


n = int(input())

for _ in range(n):
    print(calc(input()))