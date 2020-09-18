def test():
    n = [int(x) for x in input().split()]

    i = 0

    for i in range(len(n) - 1):
        if(n[i] > n[i+1]):
            break

    print('i - ' + str(i))

    if i == (len(n) - 2):
        print('C')
        return
        
    for i in range(len(n) - 1):
        if(n[i] < n[i+1]):
            break

    if i == (len(n) - 2):
        print('D')
        return

    print('N')

test()