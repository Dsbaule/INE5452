import string

def main():
    N = int(input())

    for _ in range(N):
        M = int(input())

        prices = dict()

        for _ in range(M):
            product, price = input().split()
            prices[product] = float(price)
        
        P = int(input())

        total = 0
        for _ in range(P):
            product, quantity = input().split()
            total += prices[product] * int(quantity)
        
        print('R$ %.2f' % total)
 

main()