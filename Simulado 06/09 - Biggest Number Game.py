import math

def main():
    N = int(input())

    results = list()

    num_lucas = 0
    num_pedro = 0

    for i in range(N):
        a, b = [int(x) for x in input().split('^')]
        n = int(input()[:-1])

        lucas = a ** b
        pedro = math.factorial(n)

        if lucas > pedro:
            results.append('Lucas')
            num_lucas += 1
        else:
            results.append('Pedro')
            num_pedro += 1
    
    if num_lucas > num_pedro:
        print('Campeao: Lucas!')
    elif num_lucas < num_pedro:
        print('Campeao: Pedro!')
    else:
        print('A competicao terminou empatada!')

    for i in range(N):
        print('Rodada #%d: %s foi o vencedor' % (i + 1, results[i]))

main()