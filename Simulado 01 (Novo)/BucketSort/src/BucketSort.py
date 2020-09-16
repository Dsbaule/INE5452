""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Primeiro simulado - Questoes extra-URI

Pontos resolvidos:
    1. 1 simbolo;
    2. k símbolos; e
    3. qualquer quantidade de símbolos

Não realizei a checagem dos baldes não vazios devido a facilidade do python
de lidar com este problema na hora de concatena-los.
"""

import string

def bucket_sort(input_list: list, index_to_sort = None):

    # If list wasn't partially sorted, start from the last index:
    if index_to_sort is None:
        # Get maximum word length
        max_length = 0
        for word in input_list:
            max_length = max(max_length, len(word))
        # Start from last character
        index_to_sort = max_length

    # Get possible characters
    alphabet = list(string.digits + string.ascii_lowercase)

    # Create one bucket for each type of char
    buckets = [list() for _ in range(len(alphabet))]

    # Create an extra "bucket" to keep words smaller than current character
    too_small = list()

    # Insert each word on correct bucket based on current index:
    for word in input_list:
        # If word is too small, skip it
        if len(word) <= index_to_sort:
            too_small.append(word)
        # Otherwise, sort
        else:
            # Check character at current index
            char = word[index_to_sort]
            # Insert word in correct bucket
            buckets[alphabet.index(char)].append(word)

    # Join buckets in order, starting with words that were smaller than current index
    sorted_list = too_small
    for bucket in buckets:
        sorted_list += bucket

    # If list is still not fully sorted, sort next index
    if index_to_sort > 0:
        sorted_list = bucket_sort(sorted_list, index_to_sort=(index_to_sort - 1))
    
    # Return sorted list
    return sorted_list