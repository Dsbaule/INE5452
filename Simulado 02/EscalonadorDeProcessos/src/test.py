from EscalonadorDeProcessos.MaxHeap import MaxHeap

lista = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

max_heap = MaxHeap(len(lista))
max_heap.constroi_max_heap(lista)

print(max_heap.check())
print(max_heap)