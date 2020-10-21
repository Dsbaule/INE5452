""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Rainhas Amigas com uma Intriga
"""

# Tenta posicionar a rainha causadora de intriga de forma a minimizar o número de rainhas
def intriga(n):
    # Inicializa um tabuleiro sem rainhas
    tabuleiro = [None for _ in range(n)]

    # Inicializa o numero minimo de rainhas com o máximo de rainhas possivel (numero de linhas)
    minimum = len(tabuleiro)
    minimum_pos = list()

    # Testa a rainha causadora de intrigas em cada posição
    # Testa cada linha
    for i in range(len(tabuleiro)):
        # Testa cada coluna
        for j in range(len(tabuleiro)):
            tabuleiro[i] = j

            # Para cada posicao, verifica o numero maximo de rainhas amigas possivel
            cur_min = rainha(tabuleiro, 1)

            # Caso seja menor do que o menor obtido até agora, descarta os resultados anteriores
            if cur_min < minimum:
                minimum = cur_min
                minimum_pos = [(i, j)]

            # Caso seja igual, concatena a posição atual aos resultados anteriores
            elif cur_min == minimum:
                minimum_pos.append((i, j))
        
        # Reseta a posição atual
        tabuleiro[i] = None
    
    # Retorna o menor numero de rainhas amigas possivel encontrado e as posições correspondentes
    # para a rainha causadora de intrigas
    return minimum, minimum_pos

# Tenta posicionar as demais rainhas de forma a maximizar o número de rainhas
def rainha(tabuleiro, k, i = 0):
    maximum = k
    
    # Caso a posição esteja fora do tabuleiro, retorne o numero de rainhas até agora
    if i >= len(tabuleiro):
        return maximum

    # Caso ja tenha alguma rainha na linha atual, teste a proxima posição
    if tabuleiro[i] != None:
        return rainha(tabuleiro, k, i + 1)

    # Para cada coluna possivel    
    for j in range(len(tabuleiro)):
        # Se a posição for livre de intrigas
        if safe(tabuleiro, i, j):
            # Posicione uma rainha nela
            tabuleiro[i] = j

            # Obtenha o maximo possivel com essa rainha posicionada
            cur_max = rainha(tabuleiro, k + 1, i + 1)

            # Se for maior que o maximo obtido anteriormente, substitua
            if cur_max > maximum:
                maximum = cur_max
    
    # Retira a rainha da posição
    tabuleiro[i] = None
    
    # Teste uma ultima vez, com a linha vazia
    cur_max = rainha(tabuleiro, k, i + 1)
    # Se for maior que o maximo obtido anteriormente, substitua
    if cur_max > maximum:
        maximum = cur_max

    # Retorne o valor máximo obtido
    return maximum

# Verifica se há uma intriga com uma posição do tabuleiro
def safe(tabuleiro, i, j):
    for linha in range(len(tabuleiro)):
        if (linha != i) and (tabuleiro[linha] != None):
            if (tabuleiro[linha] == j) or (abs(linha - i) == abs(tabuleiro[linha] - j)):
                return False
    return True

def main():
    # Obtem o tamanho do tabuleiro
    n = int(input("n = "))

    # Obtem os resultados
    num_rainhas, posicoes = intriga(n)

    # Normaliza as posições para iniciarem em 1
    num_rainhas += 1
    posicoes = [(i + 1, j + 1) for (i, j) in posicoes]

    # Imprime resultado
    print('Uma rainha em qualquer uma das seguintes posições minimiza o número de rainhas amigas no tabuleiro para {}:'.format(num_rainhas))
    print(*posicoes, sep=' ')

main()