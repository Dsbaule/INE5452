""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Quarto simulado - Questoes extra-URI

Escalonamento de Intervalos com Pesos


"""

# Classe para representação de uma requisição
class Requisicao():
    def __init__(self, values: list):
        self.s, self.f, self.v = values

    def __init__(self, s: int, f: int, v: int):
        self.s = s
        self.f = f
        self.v = v
    
    def __lt__(self, requisicao):
        return self.f < requisicao.f

    def __repr__(self):
        return "|%d %d %d %d|" % (self.s, self.f, self.v, self.p)


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

def calculaPesos(requisicoes: list) -> list:
    for i in range(len(requisicoes) - 1, -1, -1):
        peso = -1
        for j in range(i - 1, -1, -1):
            if requisicoes[j].f < requisicoes[i].s:
                peso = j
                break
        requisicoes[i].p = peso

# Versão simples, tempo exponencial
def computa_OPT(requisicoes: list, j:int):
    # OPT do primeiro elemento é 0
    if j < 0:
        return 0
    # Compute e retorne o resultado
    return max(requisicoes[j].v + computa_OPT(requisicoes, requisicoes[j].p), computa_OPT(requisicoes, j - 1))

# Versão com memória, tempo linear
def computa_OPT_memorizado(requisicoes: list, j:int, M: list = None):
    # OPT do primeiro elemento é 0
    if j < 0:
        return 0
    
    # Se a lista não existe inicie uma lista vazia do tamanho correto
    if not M:
        M = [None for _ in range(len(requisicoes))]
    
    # Se o valor não foi computado ainda, compute e preencha a lista
    if not M[j]:
        M[j] = max(requisicoes[j].v + computa_OPT_memorizado(requisicoes, requisicoes[j].p, M), computa_OPT_memorizado(requisicoes, j - 1, M))
    
    # Retorne o resultado
    return M[j]
    
def obtem_subconjunto_por_peso(requisicoes: list, peso:int, t: int = 0):
    if len(requisicoes) == 0:
        return [], 0

    requisicao = requisicoes.pop(0)

    requisicoes_restantes = []
    valor_obtido = 0

    if requisicao.s >= t:
        requisicoes_restantes, valor_obtido = obtem_subconjunto_por_peso(requisicoes, peso - requisicao.v, requisicao.f)
        if valor_obtido + requisicao.v == peso:
            valor_obtido = valor_obtido + requisicao.v
            requisicoes_restantes.insert(0, requisicao)

    if requisicoes_restantes == []:
        requisicoes_restantes, valor_obtido = obtem_subconjunto_por_peso(requisicoes, peso, t)

    requisicoes.insert(0, requisicao)

    return requisicoes_restantes, valor_obtido


def obtem_subconjunto_maximo(especifico:bool = False):
    # Obtem o numero de requisições
    numeroRequisicoes = int(input("\nNúmero de Requisições: "))
    
    # Obtem os valores de s, f e v para cada requisição
    requisicoes = list()
    print("\nPara cada requisição i, digite: \"si fi vi\":")
    for i in range(numeroRequisicoes):
        s, f, v = [int(x) for x in input("Requisição %d: " % (i + 1)).split()]
        requisicoes.append(Requisicao(s, f, v))

    # Ordena as requisições pelo seu tempo final
    mergeSort(requisicoes)
        
    # Calcula o peso de cada requisição
    calculaPesos(requisicoes)

    # Se for o caso 1, obtenha o peso maximo
    if not especifico:
        # Obtem o valor do subconjunto compativel de peso maximo
        pesoMaximo = computa_OPT_memorizado(requisicoes, len(requisicoes) - 1)

        # Imprime o resultado
        print("\nPeso máximo = " + str(pesoMaximo))
    
    # Se for o caso 2, onde o peso esperado é dado, obtenha o conjunto
    else:
        # Obtem o peso esperado
        peso = int(input("Peso esperado: "))

        # Obtem o valor do subconjunto compativel com um certo peso
        conjunto, _ = obtem_subconjunto_por_peso(requisicoes, peso)

        # Imprime os resultados
        if conjunto == [] and peso != 0:
            print("\nNão existe um subconjunto compatível com este peso!")
        else:
            conjunto = [str(requisicoes.index(x) + 1) for x in conjunto]
            print('\nConjunto Obtido: {%s}' % ', '.join(conjunto))


def main():
    while(True):
        # Menu simples para navegação:
        print("\nProblema da Mochila:")
        print("1 - Valor de subconjunto compatível de peso máximo")
        print("2 - Preenchimento de subconjunto com certo peso")
        print("Digite qualquer outra coisa para sair")

        alternativa = input("Seleção: ")

        if alternativa == '1':
            obtem_subconjunto_maximo(especifico=False)
        elif alternativa == '2':
            obtem_subconjunto_maximo(especifico=True)
        else:
            return

main()