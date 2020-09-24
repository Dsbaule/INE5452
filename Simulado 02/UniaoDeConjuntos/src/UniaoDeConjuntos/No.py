class No:
    def __init__(self, valor):
        self.rank = 0
        self.valor = valor
        self.pai = self
    
    def encontrar(self):
        if self.pai != self:
            self.pai = self.pai.encontrar()
        return self.pai

    def unir (self, no):
        root_self = self.encontrar()
        root_no = no.encontrar()

        if root_self == root_no:
            return
        
        if root_self.rank > root_no.rank:
            root_no.pai = root_self
        else:
            root_self.pai = root_no
            if root_self.rank == root_no.rank:
                root_no.rank += 1
