""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Algorítmo de Strassen
"""
# Soma duas matrizes
def sum_matrix(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1))] for i in range(len(m1))]

# Subtrai duas matrizes
def sub_matrix(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(len(m1))] for i in range(len(m1))]

# Divide o número por bits transformando em uma string
def strassen(m1, m2):
    # Inicializa o array para a resposta no tamanho correto
    C = [[0 for _ in range(len(m1))] for _ in range(len(m1))]

    # Caso a matriz seja 2x2, 4 equações:
    if len(m1) <= 2:
        C[0][0] = (m1[0][0] * m2[0][0]) + (m1[0][1] * m2[1][0])
        C[0][1] = (m1[0][0] * m2[0][1]) + (m1[0][1] * m2[1][1])
        C[1][0] = (m1[1][0] * m2[0][0]) + (m1[1][1] * m2[1][0])
        C[1][1] = (m1[1][0] * m2[0][1]) + (m1[1][1] * m2[1][1])
        return C
    
    # Encontra o meio
    mid = len(m1)//2
    
    # Apenas para facilitar a comparação com as equações
    # Inicializa duas matrizes para armazenar as submatrizes
    A = [[0 for _ in range(4)] for _ in range(4)]
    B = [[0 for _ in range(4)] for _ in range(4)]

    # Obtem 4 submatrizes de m1 com mesmo tamanho
    A[0][0] = [m1[x][:mid] for x in range(mid)]
    A[0][1] = [m1[x][mid:] for x in range(mid)]
    A[1][0] = [m1[x][:mid] for x in range(mid,len(m1))]
    A[1][1] = [m1[x][mid:] for x in range(mid,len(m1))]

    # Obtem 4 submatrizes de m1 com mesmo tamanho
    B[0][0] = [m2[x][:mid] for x in range(mid)]
    B[0][1] = [m2[x][mid:] for x in range(mid)]
    B[1][0] = [m2[x][:mid] for x in range(mid,len(m1))]
    B[1][1] = [m2[x][mid:] for x in range(mid,len(m1))]

    # Realiza as 7 multiplicações de Strassen
    M1 = strassen(sum_matrix(A[0][0], A[1][1]), sum_matrix(B[0][0], B[1][1]))
    M2 = strassen(sum_matrix(A[1][0], A[1][1]), B[0][0])
    M3 = strassen(A[0][0], sub_matrix(B[0][1], B[1][1]))
    M4 = strassen(A[1][1], sub_matrix(B[1][0], B[0][0]))
    M5 = strassen(sum_matrix(A[0][0], A[0][1]), B[1][1])
    M6 = strassen(sub_matrix(A[1][0], A[0][0]), sum_matrix(B[0][0], B[0][1]))
    M7 = strassen(sub_matrix(A[0][1], A[1][1]), sum_matrix(B[1][0], B[1][1]))

    # Calcula as 4 submatrizes do resultado
    C11 = sum_matrix(sub_matrix(sum_matrix(M1, M4), M5), M7)
    C12 = sum_matrix(M3, M5)
    C21 = sum_matrix(M2, M4)
    C22 = sum_matrix(sub_matrix(M1, M2), sum_matrix(M3, M6))
    
    # Concatena as submatrizes obtidas
    for i in range(mid):
        C[i][:mid] = C11[i]
        C[i][mid:] = C12[i]
        C[mid + i][:mid] = C21[i]
        C[mid + i][mid:] = C22[i]
    
    # Retorna a matriz resultante
    return C

def main():
    # Le o tamanho das matrizes
    n = int(input())

    # Le a primeira
    m1 = list()
    for _ in range(n):
        m1.append([int(x) for x in input().split()])

    # Le a segunda matriz
    m2 = list()
    for _ in range(n):
        m2.append([int(x) for x in input().split()])

    # Imprime o resultado da multiplicação de maneira legivel
    for linha in strassen(m1, m2):
        print(*linha, sep=' ')

main()