""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Rainhas Amigas com uma Intriga
"""

def intriga(n):
    tabuleiro = [None for _ in range(n)]

    minimum = len(tabuleiro)
    minimum_pos = list()

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            tabuleiro[i] = j
            cur_min = rainha(tabuleiro, 1)
            if cur_min < minimum:
                minimum = cur_min
                minimum_pos = [(i, j)]
            elif cur_min == minimum:
                minimum_pos.append((i, j))
        tabuleiro[i] = None
    
    return minimum, minimum_pos


def rainha(tabuleiro, k):
    i = 0
    while (i < len(tabuleiro)) and (tabuleiro[i] != None):
        i += 1
    
    if i > len(tabuleiro):
        return (k, [tabuleiro.copy()])

    maximum = k
    
    for j in range(len(tabuleiro)):
        if safe(tabuleiro, i, j):
            tabuleiro[i] = j
            cur_max = rainha(tabuleiro, k + 1)
            if cur_max > maximum:
                maximum = cur_max

    return maximum

def safe(tabuleiro, i, j):
    for linha in range(len(tabuleiro)):
        if (linha != i) and (tabuleiro[linha] != None):
            if (tabuleiro[linha] == j):
                return False
            if (abs(linha - i) == abs(tabuleiro[linha] - j)):
                return False
    return True


def main():
    n = int(input("n = "))
    print(intriga(n))



main()