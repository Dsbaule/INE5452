class Vertice:
    def __init__(self):
        self.edges = set()
        self.searched = False


def count_connections(vertice):
    if vertice.searched:
        return 0

    vertice.searched = True

    count = 1
    for new_vertice in vertice.edges:
        count += count_connections(new_vertice)

    return count


def main():
    H, L = [int(x) for x in input().split()]

    map = list()

    for _ in range(H):
        map.append(input().split())
    
    for i in range(H):
        for j in range(L):
            if map[i][j] == 'C':
                map[i][j] = Vertice()
            else:
                map[i][j] = None
    
    for i in range(H):
        for j in range(L):
            if map[i][j] != None:
                if i > 0 and map[i - 1][j] != None:
                    map[i - 1][j].edges.add(map[i][j])
                if j > 0 and map[i][j - 1] != None:
                    map[i][j - 1].edges.add(map[i][j])

    max_count = 0
    for i in range(H):
        for j in range(L):
            if map[i][j] != None:
                max_count = max(max_count, count_connections(map[i][j]))

    print(max_count)


main()