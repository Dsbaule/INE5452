def main():
    N = int(input())

    for _ in range(N):
        x, y = [int(x) for x in input().split()]

        rafael = (((3 * x) ** 2) + (y ** 2))
        beto = ((2 * (x ** 2)) + ((5 * y) ** 2))
        carlos = ((-100 * x) + (y ** 3))

        if rafael > carlos :
            if rafael > beto:
                print('Rafael ganhou')
            else:
                print('Beto ganhou')
        else:
            if carlos > beto:
                print('Carlos ganhou')
            else:
                print('Beto ganhou')

main()