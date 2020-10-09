def find(lista, elemento):
    if len(lista) == 1:
        if elemento < lista[0]:
            return 1
        else:
            return 0
    else:
        index = len(lista)//2
        if elemento < lista[index]:
            return index + find(lista[index:], elemento)
        elif index > 0:
            return find(lista[:index], elemento)
        else:
            return index

def test():
    N = int(input())

    total = 0
    length = 1
    i = 0
    matriculas = None

    for _ in range(N):
        matricula = input()

        if not matriculas:
            matriculas = [matricula,]
        else:
            index = find(matriculas, matricula)
            total += index
            matriculas.insert(index, matricula)
    
    #print(matriculas)
    print(total)


        
try:
    while True:
        test()
except EOFError:
    None