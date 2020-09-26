import heapq

class Caixa:
    def __init__(self, id, v, t):
        self.id = id
        self.v = v
        self.t = t
    def __eq__(self, c2):
        return self.id == c2.id
    def __gt__(self, c2):
        return (self.t > c2.t) or ((self.t == c2.t) and (self.id > c2.id))
    def __ge__(self, c2):
        return self.__gt__(c2) or self.__eq__(c2)
    def __lt__(self, c2):
        return not(self.__ge__(c2))
    def __le__(self, c2):
        return not(self.__gt__(c2))

def main():

    N, M = [int(x) for x in input().split()]

    lista_caixas = list()
    v = [int(x) for x in input().split()]
    for i in range(N):
        caixa = Caixa(i + 1, v[i], 0)
        heapq.heappush(lista_caixas, caixa)
    
    c = [int(x) for x in input().split()]
    for i in range(M):
        caixa_atual = heapq.heappop(lista_caixas)
        caixa_atual.t += c[i] * caixa_atual.v
        heapq.heappush(lista_caixas, caixa_atual)
    
    ultimo_caixa = heapq.nlargest(1, lista_caixas).pop()
    print(ultimo_caixa.t)


main()
