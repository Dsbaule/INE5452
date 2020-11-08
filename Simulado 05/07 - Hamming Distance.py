def main():
    while (True):
        x, y = [int(x) for x in input().split()]

        if x == 0 and y == 0:
            return

        diff = x ^ y

        print(bin(diff)[2:].count('1'))

main()