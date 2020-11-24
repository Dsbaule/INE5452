class Vertice:
    def __init__(self):
        self.edges = set()
        self.searched = False

def search(vertice, vertices):
    group = [vertice]
    vertices[vertice].searched = True

    for new_vertice in vertices[vertice].edges:
        if not vertices[new_vertice].searched:
            group += search(new_vertice, vertices)
    
    return group

def main():
    T = int(input())
    
    for i in range(1, T + 1):

        input_string = input().split()
        N = int(input_string[0])
        if len(input_string) > 1:
            M = int(input_string[1])
        else:
            M = int(input())

        vertices = [Vertice() for _ in range(N)]

        for _ in range(M):
            v1, v2 = [int(x) for x in input().split()]
            vertices[v1 - 1].edges.add(v2 - 1)
            vertices[v2 - 1].edges.add(v1 - 1)
        
        connected_groups = list()
        for j in range(N):
            if not vertices[j].searched:
                connected_groups.append(search(j, vertices))

        roads_left = len(connected_groups) - 1

        if roads_left == 0:
            print('Caso #%d: a promessa foi cumprida' % i)
        else:
            print('Caso #%d: ainda falta(m) %d estrada(s)' % (i, roads_left))

main()