class Pointer:
    def __init__(self, value):
        self.value = value
        self.final = True
    def updateValue(self, value):
        if self.final:
            self.value = value
        else:
            self.value.updateValue(value)
    def update(self, value):
        if self.final:
            self.final = False
            while not value.final:
                value = value.getPointer()
            self.value = value
        else:
            self.value.update(value)
    def get(self):
        if self.final:
            return self.value
        else:
            return self.value.get()
    def getPointer(self):
        return self.value


def main():
    n, b = [int(x) for x in input().split()]

    bancos = list()

    for i in range(n):
        bancos.append(Pointer([x == i for x in range(n)]))

    for _ in range(b):
        c, b1, b2 = input().split()
        b1 = int(b1) - 1
        b2 = int(b2) - 1

        if c == 'F':
            bancos[b1].updateValue([bancos[b1].get()[i] or bancos[b2].get()[i] for i in range(n)])
            bancos[b2].update(bancos[b1])
        elif bancos[b1].get()[b2]:
            print('S')
        else:
            print('N')
    
        #for i in range(n):
        #    print(bancos[i].get())

main()