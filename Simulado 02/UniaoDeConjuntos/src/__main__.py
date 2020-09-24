from src.UniaoDeConjuntos.No import No

n = int(input("Número de Conjuntos: "))

conjuntos = list()

for conjunto in range(n):
    conjuntos.append([int(x) for x in input(f"Conjunto {conjunto + 1}: ").split()])

m = int(input("Número de Operações: "))

for operacao in range(m):
    i, j = [int(x) for x in input(f"Operação {operacao + 1}: ").split()]