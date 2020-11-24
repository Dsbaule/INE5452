class Vertice:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.edges1 = set()
        self.edges2 = set()
        self.used = False


def find_longest_path_from(vertice, n):
    longest_path = 0
    vertice.used = True

    if n == vertice.n1:
        for connected_vertice in vertice.edges2:
            if not connected_vertice.used:
                longest_path = max(longest_path, find_longest_path_from(connected_vertice, vertice.n2))
    if n == vertice.n2:
        for connected_vertice in vertice.edges1:
            if not connected_vertice.used:
                longest_path = max(longest_path, find_longest_path_from(connected_vertice, vertice.n1))

    vertice.used = False
    return longest_path + 1


def find_longest_path(vertices):
    longest_path = 0
    for vertice in vertices:
        longest_path = max(longest_path, find_longest_path_from(vertice, vertice.n1))
        longest_path = max(longest_path, find_longest_path_from(vertice, vertice.n2))
    return longest_path


def main():
    N = int(input())

    pieces_containing_number = [set() for _ in range(10)]
    vertices = set()

    for _ in range(N):
        n1, n2 = [int(x) for x in input().split()]
        vertice = Vertice(n1, n2)
        vertices.add(vertice)
        pieces_containing_number[n1].add(vertice)
        pieces_containing_number[n2].add(vertice)
    
    for i in range(10):
        for piece in pieces_containing_number[i]:
            if piece.n1 == i:
                piece.edges1 = pieces_containing_number[i]
            if piece.n2 == i:
                piece.edges2 = pieces_containing_number[i]
    
    print(find_longest_path(vertices))

try:
    while True:
        main()
except EOFError:
    pass