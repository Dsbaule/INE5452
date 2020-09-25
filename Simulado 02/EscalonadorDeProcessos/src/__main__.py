""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

União de Conjuntos
"""
from src.EscalonadorDeProcessos.MaxHeap import MaxHeap
from src.EscalonadorDeProcessos.Processo import Processo
from pprint import pp

# Get processing time
tempo_considerado = int(input()) + 1

# Get process groups arriving at each timeslice
grupos_de_processos_num = list()
for _ in range(tempo_considerado):
    grupos_de_processos_num.append([int(x) for x in input().split()])

# Get number of processes
num_processos = int(input())

# Get process info
dados_dos_processos = dict()
for _ in range(num_processos):
    i, t, p, v = [int(x) for x in input().split()]
    dados_dos_processos[i] = (t, p, v)

# Create process heap and computed list
heap_de_processos = MaxHeap(0)
processos_computados = list()
time_slice = 0

# Compute each timeslice
for time_slice in range(tempo_considerado):
    processos_chegando = grupos_de_processos_num[time_slice]
    for num_processo in processos_chegando:
        t, p, v = dados_dos_processos[num_processo]
        heap_de_processos.insere_max_heap(Processo(num_processo, t, p, v, time_slice))
    if heap_de_processos.raiz().processou():
        raiz = heap_de_processos.remove_maximo_max_heap()
        raiz.saiu_da_heap(time_slice)
        processos_computados.append(raiz)

# Compute the rest
while not heap_de_processos.vazia():
    time_slice += 1
    if heap_de_processos.raiz().processou():
        raiz = heap_de_processos.remove_maximo_max_heap()
        raiz.saiu_da_heap(time_slice)
        processos_computados.append(raiz)

print(*processos_computados, sep=' ')