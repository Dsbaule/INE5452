""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

União de Conjuntos - Versão para testes
"""

from src.UniaoDeConjuntos.No import No
from pprint import pp

def test(n, conjuntos, m, operacoes, test_number='X'):
    print(f'\n\n-------------------- TEST {test_number} --------------------')
    print(f'n = {n}')
    string = '  '
    print(f'Conjuntos de entrada =  {string.join([str(x) for x in conjuntos])}')
    print(f'm = {m}')
    print(f'Operacoes de união de entrada = {string.join([str(x) for x in operacoes])}')

    # For each set, create nodes for all elements and unite them
    conjunto_dict = dict()
    for conjunto in conjuntos:
        conjunto_dict[conjunto[0]] = No(conjunto[0])
        for no in conjunto[1:]:
            conjunto_dict[no] = No(no)
            conjunto_dict[no].unir(conjunto_dict[conjunto[0]])

    # Print starting state:
    conjuntos.sort()
    print(f'\nConjuntos iniciais:')
    print(*conjuntos, sep="  ")

    print('\nNós iniciais (No formato Nó(Pai)):')
    nos = list(conjunto_dict.values())
    nos.sort(key = lambda x: x.pai.valor)
    print(*nos, sep="  ")

    # Get input values and execute new unions
    for operacao in operacoes:
        i, j = operacao
        conjunto_dict[i].unir(conjunto_dict[j])
        print(f'\nApós união entre {i} e {j}:')

        # Go through all nodes, grouping them by root to obtain sets
        final_sets = dict()
        for no in conjunto_dict.values():
            no_raiz = no.encontrar()
            set_conjunto = final_sets.get(no_raiz, None)
            if set_conjunto is None:
                final_sets[no_raiz] = {no.valor}
            else:
                final_sets[no_raiz].add(no.valor)

        # Sort each set
        sorted_sets = [list(final_set) for final_set in final_sets.values()]
        for sorted_set in sorted_sets:
            sorted_set.sort()
        # Sort sets in relation to each other based on first element
        sorted_sets.sort()

        print(*sorted_sets, sep='  ')

        nos = list(conjunto_dict.values())
        nos.sort(key = lambda x: x.pai.valor)
        print(*nos, sep="  ")

    # Go through all nodes, grouping them by root to obtain sets
    final_sets = dict()
    for no in conjunto_dict.values():
        no_raiz = no.encontrar()
        set_conjunto = final_sets.get(no_raiz, None)
        if set_conjunto is None:
            final_sets[no_raiz] = {no.valor}
        else:
            final_sets[no_raiz].add(no.valor)

    # Sort each set
    sorted_sets = [list(final_set) for final_set in final_sets.values()]
    for sorted_set in sorted_sets:
        sorted_set.sort()
    # Sort sets in relation to each other based on first element
    sorted_sets.sort()

    # Print resulting sets
    print("\nConjuntos Resultantes:")
    for sorted_set in sorted_sets:
        print(*sorted_set, sep=' ')
