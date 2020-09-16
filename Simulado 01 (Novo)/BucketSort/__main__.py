""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Primeiro simulado - Questoes extra-URI

Pontos resolvidos:
    1. 1 simbolo;
    2. k símbolos; e
    3. qualquer quantidade de símbolos

Devido a utilização da linguagem python, o número de caracteres da entrada não afeta a 
execução do código, mas devido ao enunciado, foi adicionada uma validação adicional da
entrada, levantando uma exceção no caso de entrada invalida.
"""

from BucketSort.src.BucketSort import bucket_sort

def main():

    # Get input
    n, k = input().split()
    input_list = input().split()

    # Check if input is correct length
    if len(input_list) != int(n):
        raise Exception("Invalid input")

    # Check if input is valid
    if k != 'x':
        k = int(k)
        for element in input_list:
            if len(element) != k:
                raise Exception("Invalid input")

    # Sort input
    sorted_list = bucket_sort(input_list)

    # Format output
    output = ""
    for element in sorted_list:
        output += str(element) + " "
    output = output[:-1]

    # Print
    print(output)

main()