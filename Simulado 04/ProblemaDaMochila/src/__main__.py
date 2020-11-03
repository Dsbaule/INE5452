""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Quarto simulado - Questoes extra-URI

Problema da mochila
"""

# Merge sort
def mergeSort(numeros: list) -> list:
    if len(numeros) > 1:
        meio = len(numeros) // 2
        metadeEsquerda = numeros[:meio]
        metadeDireita = numeros[meio:]

        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)

        i = 0
        j = 0
        k = 0

        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if metadeEsquerda[i] < metadeDireita[j]:
                numeros[k] = metadeEsquerda[i]
                i = i + 1
            else:
                numeros[k] = metadeDireita[j]
                j = j + 1
            k = k + 1

        while i < len(metadeEsquerda):
            numeros[k] = metadeEsquerda[i]
            i = i + 1
            k = k + 1

        while j < len(metadeDireita):
            numeros[k] = metadeDireita[j]
            j = j + 1
            k = k + 1

    return numeros


# Classe que representa um Item da mochila
class Item():
    def __init__(self, values: list):
        self.w, self.v = values

    def __init__(self, w: int, v: int):
        self.w = w
        self.v = v

    def __repr__(self):
        return "|%d %d|" % (self.w, self.v)

# Problema da Mochila
def problema_da_mochila(repeticoes: bool = True):
    # Obtem o número de itens em I:
    numeroRequisicoes = int(input("\nNúmero de itens em I: "))

    # Obtem os valores de w e v para cada item em I
    itens = list()
    print("\nPara cada ítem em I, digite: \"wi vi\":")
    for i in range(numeroRequisicoes):
        w, v = [int(x) for x in input("Item %d: " % (i + 1)).split()]
        itens.append(Item(w, v))

    # Obtem a capacidade da mochila:
    W = int(input("Capacidade da mochila: "))

    # Obtem o valor da mochila máxima:
    if repeticoes:
        mochila_maxima = mochila_com_repeticoes(itens, W)
    else:
        mochila_maxima = mochila_sem_repeticoes(itens, W)

    # Imprime o resultado:
    print("\nValor da mochila máxima: %d\n" % mochila_maxima)

def mochila_sem_repeticoes(itens: list, W: int, max_j: int = None, K: list = None) -> int:
    # Na chamada inicial não é passado o valor máximo de j
    if max_j == None:
        max_j = len(itens)
    
    # Na chamada inicial não é passada a matriz
    if K == None:
        K = [[0 for _ in range(len(itens) + 1)] for _ in range(W + 1)]
    
    # Caso os valores sejam fora do esperado, maximo 0
    if max_j <= 0 or W <= 0:
        return 0

    # Preenche a matriz
    for j in range(1, max_j + 1):
        for w in range(1, W + 1):
            if itens[j - 1].w > w:
                K[w][j] = K[w][j - 1]
            else:
                K[w][j] = max(mochila_sem_repeticoes(itens, W - itens[j - 1].w, max_j - 1, K) + itens[j - 1].v, mochila_sem_repeticoes(itens, W, max_j - 1, K))

    # Retorna o valor máximo
    return K[W][max_j]

def mochila_com_repeticoes(itens: list, W: int) -> int:
    # Explora todas as possibilidades de preenchimento
    # da mochila e retorna aquela com o maior valor
    return max([0] + [x.v + mochila_com_repeticoes(itens, W - x.w) \
        for x in itens if x.w <= W])


def main():
    while(True):
        # Menu simples para navegação:
        print("Problema da Mochila:")
        print("1 - Calculo da mochila máxima com repetição")
        print("3 - Calculo da mochila máxima sem repetição")
        print("Digite qualquer outra coisa para sair")
        
        alternativa = input("Seleção: ")

        if alternativa == '1':
            problema_da_mochila(repeticoes=True)
        elif alternativa == '2':
            pass
        elif alternativa == '3':
            problema_da_mochila(repeticoes=False)
        elif alternativa == '4':
            pass
        else:
            return
    

main()