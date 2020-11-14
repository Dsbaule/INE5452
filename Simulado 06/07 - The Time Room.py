import math

T = int(input())

for _ in range(T):
    x, y = [int(x) for x in input().split()]

    if y > x:
        print('2')
    else:
        k = x // y

        if (k % y) != 0:
            k += 1            

        print(k)