""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Ordem das Permutações
"""

# Outro algorítmo por backtracking para gerar todas as permutações de uma lista
# (A lista ja deve estar preenchida com numeros de 1-n)
def permutar(n: list):
    # Caso n tenha apenas 1 número
    if len(n) == 1:
        return [n]

    # Cria uma lista de saida
    permutacoes = list()

    # Para cada index da lista
    for i in range(len(n)):
        # Retire o numero deste este numero da lista
        num_restantes = [n[j] for j in range(len(n)) if j != i]
        # Obtenha todas as permutações da lista restante
        for resto in permutar(num_restantes):
            # Para cada permutação, concatene ao numero e adicione ao resultado
            permutacoes.append([n[i]] + resto)
    
    # Retorna o resultado obtido
    return permutacoes


# Algorítmo ensinado pelo professor na aula: (a deve ser uma lista de zeros)
def permutar_2(a: list, k = 0):
    # Caso o ultimo index ja tenha sido preenchido, retorna uma cópia da lista
    if k == len(a):
        return [a.copy()]
    
    # Cria uma lista de saida
    output = list()

    # Para cada index da lista
    for i in range(len(a)):
        # Caso o index não tenha sido preenchido ainda
        if a[i] == 0:
            # Preencha com k + 1
            a[i] = k + 1
            # Obtenha todas as permutações a partir dai e concatene com o resultado
            output += permutar_2(a, k + 1)
            # Restaure o index alterado
            a[i] = 0
    
    # Retorna o resultado obtido
    return output


def main():
    # Obtem n
    n = int(input())

    # Gera as listas crescentes e decrescentes
    c = list(range(1, n + 1))
    d = list(range(n, 0, -1))

    # Gera as permutações
    #r = permutar(c)
    r = permutar_2([0 for _ in range(n)])

    # Calcula C'
    C_1 = list()
    for permutacao in r:
        C_1.append([permutacao[i] + c[i] for i in range(n)])

    # Calcula D'
    D_1 = list()
    for permutacao in r:
        D_1.append([permutacao[i] + d[i] for i in range(n)])

    # Calcula C"
    C_2 = list()
    for i in range(len(r)):
        # Incrementa o tamanho da lista
        C_2.append(1) 
        # Calcula o produtório
        for value in C_1[i]:
            C_2[i] *= value
        # (mod 26)
        C_2[i] %= 26
        
    # Calcula D"
    D_2 = list()
    for i in range(len(r)):
        # Incrementa o tamanho da lista
        D_2.append(1) 
        # Calcula o produtório
        for value in D_1[i]:
            D_2[i] *= value
        # (mod 26)
        D_2[i] %= 26
    
    """ 
    # Imprime tabela
    row = "{:>20}" * 5
    print()
    print(row.format('r', 'C\'', 'D\'', 'C\"', 'D\"'))
    for i in range(len(r)):
        print(row.format(str(r[i]), str(C_1[i]), str(D_1[i]), str(C_2[i]), str(D_2[i])))
    """
    
    # Gera a saída ordenada por C", index de r no caso de empate
    output_list = [(C_2[i], i, D_2[i]) for i in range(len(r))]
    output_list.sort()

    # Imprime os valores ordenados de C" e em seguida D"
    # print('\nSaída resultante (C" e D"):')
    print(' '.join([str(x[0]) for x in output_list]))
    print(' '.join([str(x[2]) for x in output_list]))

main()