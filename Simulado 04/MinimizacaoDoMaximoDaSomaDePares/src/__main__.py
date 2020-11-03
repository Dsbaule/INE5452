""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Quarto simulado - Questoes extra-URI

Minimizaçao do máximo da soma de pares

Para minimizar o máximo da soma de pares, o maior 
número deve ser sempre somado com o menor.

Para isso, primeiro passo é ordenar os números, utilizando o mergesort
devido a complexidade O(n log(n))

As operações restantes tem complexidade linear, tornando a complexidade
total do algorítmo O(n log(n))

É garantido que a soma máxima é a menor possível pois dado o par com a soma
máxima, a troca de qualquer um de seus elementos por um menor resultaria na
soma do elemento substituído com um maior do que o anterior, resultando em
uma soma maior. Isso ocorre pois dado um par (Xi, Yi), para todo par (Xn, Yn)
com Xn < Xi, tem-se Yn >= Yi, e para todo par (Xn, Yn) com Yn < Yi, tem-se
Xn >= Xi.
"""

# Merge sort
def mergeSort(numeros: list) -> list:
    if len(numeros) > 1:
        meio = len(numeros) // 2
        metadeEsquerda = numeros[:meio]
        metadeDireita = numeros[meio:]

        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)

        i=0
        j=0
        k=0

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
    # Obtem a lista de numeros
    numeros = [int(x) for x in input("Digite a sequência de números: ").split()]

    # Verifica se a sequência tem número par de números
    if len(numeros) % 2 != 0:
        print("A sequência deve ter número par de elementos!")
        return
    
    # Ordena os números:
    numeros = mergeSort(numeros)

    # Computa os pares de modo a minimizar a soma máxima:
    pares = list()
    for i in range(len(numeros) // 2):
        pares.append((numeros[i], numeros[-(1+i)], numeros[i] + numeros[-(1+i)]))

    # Imprime os resultados
    print("Somas:")
    maximo = None
    for par in pares:
        print('%d + %d = %d' % par)
        if not maximo or par[2] > maximo:
            maximo = par[2]
    print("Soma máxima = %d" % maximo)

main()