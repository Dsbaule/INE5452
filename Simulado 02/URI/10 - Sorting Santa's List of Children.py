def test():
    n = int(input())
    
    nice = 0
    naugthy = 0

    children = list()

    for _ in range(n):
        behaviour, child = input().split()

        if behaviour == '+':
            nice += 1
        else:
            naugthy += 1
        
        children.append(child)

    children.sort()

    for child in children:
        print(child)

    print('Se comportaram: ' + str(nice) + ' | Nao se comportaram: ' + str(naugthy))

test()