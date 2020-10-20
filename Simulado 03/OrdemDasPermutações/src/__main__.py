""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Ordem das Permutações

A saída resultante difere do exemplo do professor devido a diferente ordenação das 
permutações, até mesmo da resultante do algorítmmo ensinado em sala de aula.
"""

# Outro algorítmo por backtracking para gerar todas as permutações de uma lista
def permutar(n: list) -> list():
    if len(n) == 1:
        return [n]

    permutacoes = list()

    for i in range(len(n)):
        num_restantes = [n[j] for j in range(len(n)) if j != i]
        for resto in permutar(num_restantes):
            permutacoes.append([n[i]] + resto)
    
    return permutacoes


# Algorítmo ensinado pelo professor na aula: (a deve ser uma lista de zeros)
def permutar_2(a: list, k = 0):
    if k == len(a):
        return [a.copy()]
    
    output = list()
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = k + 1
            output += permutar_2(a, k + 1)
            a[i] = 0
    
    return output


def main():
    # Obtem n
    n = int(input('N = '))

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
        C_2.append(1)
        for value in C_1[i]:
            C_2[i] *= value
        C_2[i] %= 26
        
    # Calcula D"
    D_2 = list()
    for i in range(len(r)):
        D_2.append(1)
        for value in D_1[i]:
            D_2[i] *= value
        D_2[i] %= 26

    # Imprime tabela
    row = "{:>20}" * 5
    print()
    print(row.format('r', 'C\'', 'D\'', 'C\"', 'D\"'))
    for i in range(len(r)):
        print(row.format(str(r[i]), str(C_1[i]), str(D_1[i]), str(C_2[i]), str(D_2[i])))

    # Gera a saída ordenada por C", index de r no caso de empate
    output_list = [(C_2[i], i, D_2[i]) for i in range(len(r))]
    output_list.sort()

    # Imprime os valores ordenados de C" e em seguida D"
    print('\nSaída resultante (C" e D"):')
    print(', '.join([str(x[0]) for x in output_list]))
    print(', '.join([str(x[2]) for x in output_list]))

main()