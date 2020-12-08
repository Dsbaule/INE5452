sizes = ['XXL', 'XL', 'L', 'M', 'S', 'XS']

def check_volunteers(volunteers, available_tshirts, n):
    if n >= len(volunteers):
        return True

    for size in volunteers[n]:
        if available_tshirts[size] > 0:
            available_tshirts[size] -= 1
            if check_volunteers(volunteers, available_tshirts, n + 1):
                return True
            available_tshirts[size] += 1
    
    return False

def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n, m = [int(x) for x in input().split()]
        n = n // 6

        available_tshirts = dict()
        for size in sizes:
            available_tshirts[size] = n

        volunteers = list()
        for _ in range(m):
            volunteers.append(input().split())

        if check_volunteers(volunteers, available_tshirts, 0):
            print('YES')
        else:
            print('NO')

main()
