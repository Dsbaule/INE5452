""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

União de Conjuntos - Versão para testes
"""

from src.UniaoDeConjuntos.No import No
from pprint import pp

# Get input sets
n = int(input("Número de Conjuntos: "))
conjuntos = list()
for conjunto in range(n):
    conjuntos.append([int(x) for x in input(f"Conjunto {conjunto + 1}: ").split()])

# For each set, create nodes for all elements and unite them
conjunto_dict = dict()
for conjunto in conjuntos:
    conjunto_dict[conjunto[0]] = No(conjunto[0])
    for no in conjunto[1:]:
        conjunto_dict[no] = No(no)
        conjunto_dict[no].unir(conjunto_dict[conjunto[0]])

# Get input values and execute new unions
m = int(input("Número de Operações: "))
for operacao in range(m):
    i, j = [int(x) for x in input(f"Operação {operacao + 1}: ").split()]
    conjunto_dict[i].unir(conjunto_dict[j])

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
print("Conjuntos Resultantes:")
for sorted_set in sorted_sets:
    print(*sorted_set, sep=' ')
