""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Quarto simulado - Questoes extra-URI

Menor Conjunto de Intervalos Fechados

É sempre necessário um intervalo que contenha o menor ponto na reta,
e esse intervalo cobre [x, x+1], contendo todos os pontos neste intervalo.
A partir deste ponto, voltamos ao inicio do problema.

Novamente, a complexidade é dada pela ordenação dos pontos, uma vez que o
restante do algoritmo tem complexidade linear.

Devido a utilização do Mergesort, a complexidade é O(n log(n))
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


def main():
    # Obtem a lista de pontos
    numeros = [float(x) for x in input("Digite a sequência de números: ").split()]
    
    # Ordena os números: O(n log(n))
    numeros = mergeSort(numeros)

    # Computa os pares de modo a minimizar a soma máxima:
    # Cada ponto é analisado apenas uma vez: O(n)
    intervalos = list()
    while numeros:
        numero = numeros.pop(0)
        intervalo = (numero, numero + 1)

        while numeros and numeros[0] <= numero + 1:
            numeros.pop(0)

        intervalos.append(intervalo)

    # Imprime os resultados
    print("\nIntervalos fechados:")
    string = ''
    for intervalo in intervalos:
        string += '[%f, %f] ' % intervalo
    print(string)

    print('\nNúmero de intervalos: %d' % len(intervalos))

main()