""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

Classe que define um Processo
"""

class Processo:
    def __init__(self, i, t, p, v, heap_time):
        self.i = i
        self.t = t
        self.p = p
        self.v = v
        self.heap_time = -heap_time
    
    def __repr__(self):
        return str(self.v) + '(' + str(self.t) + ')'

    def __str__(self):
        return str(self.v)

    def __eq__(self, p2):
        return (self.p == p2.p) and (self.t == p2.t) and (self.v == p2.v)

    def __ne__(self, p2):
        return not(self.__eq__(p2))
    
    def __gt__(self, p2):
        return (self.p > p2.p) or \
            ((self.p == p2.p) and (self.t < p2.t)) or \
            (((self.p == p2.p) and (self.t == p2.t)) and (self.v < p2.v))
    
    def __ge__(self, p2):
        return self.__gt__(p2) or self.__eq__(p2)
    
    def __lt__(self, p2):
        return not(self.__gt__(p2) or self.__eq__(p2))

    def __le__(self, p2):
        return not(self.__gt__(p2))

    def entrou_na_heap(self, tempo):
        self.heap_time = -tempo
    
    def saiu_da_heap(self, tempo):
        self.heap_time += tempo

    def processou(self):
        self.t -= 1
        return self.t == 0

    