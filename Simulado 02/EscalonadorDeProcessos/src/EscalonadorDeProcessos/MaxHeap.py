class MaxHeap:
    def __init__(self, n):
        self.n = n
        self.maxHeap = [None for _ in range(n + 1)]
        
    
    def __str__(self):
        return str(self.maxHeap)

    # Funções Auxiliares

    @staticmethod
    def pai(i):
        return i//2

    
    @staticmethod
    def filho_esq(i):
        return i * 2


    @staticmethod
    def filho_dir(i):
        return (i * 2) + 1


    def swap(self, i1, i2):
        temp = self.maxHeap[i1]
        self.maxHeap[i1] = self.maxHeap[i2]
        self.maxHeap[i2] = temp
    
    def vazia(self):
        return self.n <= 1

    def check(self):
        valid = True
        for i in range(1, self.n + 1):
            if self.filho_dir(i) <= self.n:
                valid = valid and (self.maxHeap[i] >= self.maxHeap[self.filho_dir(i)])
            if self.filho_esq(i) <= self.n:
                valid = valid and (self.maxHeap[i] >= self.maxHeap[self.filho_esq(i)])
        return valid

    # Funções Principais

    def max_heapfica(self, i):
        e = self.filho_esq(i)
        d = self.filho_dir(i)

        maior = i

        if (e <= self.n) and (self.maxHeap[e] > self.maxHeap[maior]):
            maior = e
        if (d <= self.n) and (self.maxHeap[d] > self.maxHeap[maior]):
            maior = d
        
        if maior != i:
            self.swap(maior, i)
            self.max_heapfica(maior)


    def constroi_max_heap(self, vetor: list):
        self.n = len(vetor)
        self.maxHeap = [None] + vetor

        for i in range(self.pai(self.n), 0, -1):
            self.max_heapfica(i)

    
    def insere_max_heap(self, valor):
        self.n += 1
        if len(self.maxHeap) <= self.n:
            self.maxHeap.append(None)
        self.aumenta_valor_max_heap(self.n, valor)

    
    def remove_maximo_max_heap(self):
        maior = self.maxHeap[1]

        self.maxHeap[1] = self.maxHeap[self.n]
        self.n -= 1

        self.max_heapfica(1)

        return maior
    
    def raiz(self):
        return self.maxHeap[1]

    
    def aumenta_valor_max_heap(self, i, valor):
        self.maxHeap[i] = valor
        while i > 1 and self.maxHeap[self.pai(i)] < self.maxHeap[i]:
            self.swap(i, self.pai(i))
            i = self.pai(i)

    

