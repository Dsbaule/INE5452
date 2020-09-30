""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

União de Conjuntos - Nó
"""

# Class to implement union find Node
class No:
    # New node has given value, rank 0 and is it's own father
    def __init__(self, valor):
        self.rank = 0
        self.valor = valor
        self.pai = self
    
    # Find root
    def encontrar(self):
        # If not root, make root of father new father
        if self.pai != self:
            self.pai = self.pai.encontrar()
        # Return new father
        return self.pai

    # Union with another node
    def unir (self, no: "No"):
        # Get roots
        root_self = self.encontrar()
        root_no = no.encontrar()
        # If they have the same root, already united
        if root_self == root_no:
            return
        # Make higher ranked one new root  
        if root_self.rank > root_no.rank:
            root_no.pai = root_self
        else:
            root_self.pai = root_no
            # If ranks were equal, increase new root rank
            if root_self.rank == root_no.rank:
                root_no.rank += 1
