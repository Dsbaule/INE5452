""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

União de Conjuntos
"""
from src.EscalonadorDeProcessos.MaxHeap import MaxHeap
from src.EscalonadorDeProcessos.Processo import Processo
from pprint import pp

# Obtem o tempo a ser computado (Para adição de processos)
tempo_considerado = int(input()) + 1

# Obtem os grupos de processos adicionados em cada timeslice
grupos_de_processos_num = list()
for _ in range(tempo_considerado):
    grupos_de_processos_num.append([int(x) for x in input().split()])

# Obtem número de processos
num_processos = int(input())

# Obtem informações dos processos
dados_dos_processos = dict()
for _ in range(num_processos):
    i, t, p, v = [int(x) for x in input().split()]
    dados_dos_processos[i] = (t, p, v)

# Cria a heap e a lista dos processos concluidos
heap_de_processos = MaxHeap(0)
processos_computados = list()
time_slice = 0

# Computa os processos, adicionando os novos grupos na heap de acordo com o timeslice
for time_slice in range(tempo_considerado):
    if not(heap_de_processos.vazia()):
        if heap_de_processos.raiz().processou():
            raiz = heap_de_processos.remove_maximo_max_heap()
            raiz.saiu_da_heap(time_slice)
            processos_computados.append(raiz)
        heap_de_processos.max_heapfica()
    processos_chegando = grupos_de_processos_num[time_slice]
    for num_processo in processos_chegando:
        t, p, v = dados_dos_processos[num_processo]
        heap_de_processos.insere_max_heap(Processo(num_processo, t, p, v, time_slice))

# Computa os processos restantes na heap
while not heap_de_processos.vazia():
    time_slice += 1
    if heap_de_processos.raiz().processou():
        raiz = heap_de_processos.remove_maximo_max_heap()
        raiz.saiu_da_heap(time_slice)
        processos_computados.append(raiz)

# Imprime ordem em que os processos foram computados
ordem_dos_processos = ' '.join([str(x) for x in processos_computados])
print(f'Ordem dos processos: {ordem_dos_processos}')

# Computa demais valores:
processo_0 = processos_computados[0]
identificador_menor_tempo_de_heap = processo_0.v
menor_tempo_de_heap = processo_0.heap_time
identificador_maior_tempo_de_heap = processo_0.v
maior_tempo_de_heap = processo_0.heap_time

for processo in processos_computados[1:]:
    if processo.heap_time < menor_tempo_de_heap or \
    (processo.heap_time == menor_tempo_de_heap and processo.v < identificador_menor_tempo_de_heap):
        identificador_menor_tempo_de_heap = processo.v
        menor_tempo_de_heap = processo.heap_time
    if processo.heap_time > maior_tempo_de_heap or \
    (processo.heap_time == maior_tempo_de_heap and processo.v < identificador_maior_tempo_de_heap):
        identificador_maior_tempo_de_heap = processo.v
        maior_tempo_de_heap = processo.heap_time

print(f'Identificador do processo com menor tempo de heap: {identificador_menor_tempo_de_heap}')
print(f'Valor do menor tempo de heap: {menor_tempo_de_heap}')
print(f'Identificador do processo com maior tempo de heap: {identificador_maior_tempo_de_heap}')
print(f'Valor do maior tempo de heap: {maior_tempo_de_heap}')
