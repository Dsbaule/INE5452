""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Quarto simulado - Questoes extra-URI

Problema da mochila
"""

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
    print("\nValor da mochila máxima: %d" % mochila_maxima)


# Problema da mochila sem repetições
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
                K[w][j] = max(mochila_sem_repeticoes(itens, W - itens[j - 1].w, max_j - 1,
                                                     K) + itens[j - 1].v, mochila_sem_repeticoes(itens, W, max_j - 1, K))

    # Retorna o valor máximo
    return K[W][max_j]

# Problema da mochila com repetições
def mochila_com_repeticoes(itens: list, W: int) -> int:
    # Explora todas as possibilidades de preenchimento
    # da mochila e retorna aquela com o maior valor
    return max([0] + [x.v + mochila_com_repeticoes(itens, W - x.w)
                      for x in itens if x.w <= W])

# Problema da mochila modificado
def encontra_itens(repeticoes: bool = True):
    # Obtem o número de itens em I:
    numeroRequisicoes = int(input("\nNúmero de itens em I: "))

    # Obtem os valores de w e v para cada item em I
    itens = list()
    print("\nPara cada ítem em I, digite: \"wi vi\":")
    for i in range(numeroRequisicoes):
        w, v = [int(x) for x in input("Item %d: " % (i + 1)).split()]
        itens.append(Item(w, v))

    # Obtem o valor da mochila maxima esperado:
    W = int(input("Valor da mochila maxima: "))

    # Obtem os itens:
    if repeticoes:
        resultado = itens_com_repeticoes(itens, W)
    else:
        resultado = itens_sem_repeticoes(itens.copy(), W)

    # Imprime o resultado:
    if resultado is None:
        print("Não existe combinação de itens que resulte neste valor de mochila!")
    else:
        # Imprime as ocorrências de cada item
        row_format = "{:>15}" * 4
        print("\nCombinação encontrada:")
        print(row_format.format("___i___", "___w___", "___v___", "Quantidade"))
        for i in range(len(itens)):
            print(row_format.format(
                i + 1, itens[i].w, itens[i].v, resultado[0].count(itens[i])))

# Encontrar uma mochila específica dentro do espaço de soluções sem repetições
def itens_sem_repeticoes(itens: list, V: int) -> (list, int):
    # Retorna conjunto vazio caso valor ou lista vazio
    if V == 0 or len(itens) == 0:
        return [], 0

    # Valor Invalido
    if V < 0:
        return None

    # Remove o item
    item = itens.pop()

    # Testa combinações restantes com o item, caso valor menor ou igual ao esperado
    if item.v <= V:
        com_item = itens_sem_repeticoes(itens, V - item.v)
        # Desempacota o resultado, caso enncontrado
        if com_item != None:
            outros_itens, valor_mochila_restante = com_item
            # Verifica se o resultado era o esperado
            if valor_mochila_restante + item.v == V:
                itens_resultantes = outros_itens + [item]
                return itens_resultantes, V

    # Testa combinações sem o item
    sem_item = itens_sem_repeticoes(itens, V)

    # Desempacota o resultado, caso enncontrado
    if sem_item != None:
        outros_itens, valor_mochila_restante = sem_item
        # Verifica se o resultado era o esperado
        if valor_mochila_restante == V:
            itens_resultantes = outros_itens + [item]
            return itens_resultantes, V

    # Readiciona o item para proximos testes
    itens.append(item)

    # Caso resultado não tenha sido encontrado, retorne
    return None

# Encontrar uma mochila específica dentro do espaço de soluções com repetições
def itens_com_repeticoes(itens: list, V: int) -> int:
    # Retorna conjunto vazio caso valor ou lista vazio
    if V == 0:
        return [], 0

    # Valor Invalido
    if V < 0:
        return None

    # Explora todas as possibilidades de preenchimento
    # da mochila e retorna aquela com o maior valor
    for item in itens:
        com_item = itens_com_repeticoes(itens, V - item.v)
        if com_item != None:
            outros_itens, valor_mochila_restante = com_item
            if valor_mochila_restante + item.v == V:
                itens_resultantes = outros_itens + [item]
                return itens_resultantes, V

    return None


def main():
    while(True):
        # Menu simples para navegação:
        print("\nProblema da Mochila:")
        print("1 - Calculo da mochila máxima com repetição")
        print("2 - Preenchimento de mochila máxima com repetição")
        print("3 - Calculo da mochila máxima sem repetição")
        print("4 - Preenchimento de mochila máxima sem repetição")
        print("Digite qualquer outra coisa para sair")

        alternativa = input("Seleção: ")

        if alternativa == '1':
            problema_da_mochila(repeticoes=True)
        elif alternativa == '2':
            encontra_itens(repeticoes=True)
        elif alternativa == '3':
            problema_da_mochila(repeticoes=False)
        elif alternativa == '4':
            encontra_itens(repeticoes=False)
        else:
            return


main()
