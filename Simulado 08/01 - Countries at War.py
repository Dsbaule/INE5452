class Vertice:
    def __init__(self, N):
        self.edges = [1000000 for _ in range(N)]

def main():
    N, E = (int(x) for x in input().split())
    
    if N == E == 0:
        return False

    cities = [Vertice(N) for _ in range(N)]

    for i in range(N):
        cities[i].edges[i] = 0

    for _ in range(E):
        X, Y, H = (int(x) - 1 for x in input().split())
        cities[X].edges[Y] = H + 1
    
    dist = [cities[i].edges.copy() for i in range(N)]

    """ 
    dist = [[_ for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = cities[i].edges[j]
    """
    for i in range(N):
        for j in range(N):
            if (cities[i].edges[j] < 1000000) and (cities[j].edges[i] < 1000000):
                dist[i][j] = 0
                dist[j][i] = 0
                
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > (dist[i][k] + dist[k][j]):
                    dist[i][j] = (dist[i][k] + dist[k][j])



    K = int(input())

    for _ in range(K):
        O, D = (int(x) - 1 for x in input().split())
        
        if dist[O][D] == 1000000:
            print('Nao e possivel entregar a carta')
        else:
            print(dist[O][D])

    return True

while main():
    print()