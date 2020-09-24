def getAndUpdate(bancos, index):
    if bancos[index] == index:
        return index
    else:
        bancos[index] = getAndUpdate(bancos, bancos[index])
        return bancos[index]

def main():
    n, b = [int(x) for x in input().split()]

    bancos = list()

    bancos.append(n)

    for i in range(1, n + 1):
        bancos.append(i)

    for _ in range(b):
        c, b1, b2 = input().split()
        b1 = int(b1)
        b2 = int(b2)

        if c == 'F':
            if getAndUpdate(bancos, b1) >= getAndUpdate(bancos, b2):
                bancos[bancos[b1]] = bancos[b2]
            else:
                bancos[bancos[b2]] = bancos[b1]
        elif getAndUpdate(bancos, b1) == getAndUpdate(bancos, b2):
            print('S')
        else:
            print('N')
    
        #for i in range(n):
        #    print(bancos[i].get())

main()