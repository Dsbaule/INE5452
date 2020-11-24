def pathR(edges, v, searched, depth=2):
    if searched[v]:
        return False
    
    searched[v] = True

    printed = False

    for w in range(len(edges)):
        if w in edges[v]:
            printed = True
            if not searched[w]:
                print('%s%d-%d pathR(G,%d)' % (' ' * depth, v, w, w))
                pathR(edges, w, searched, depth + 2)
            else:
                print('%s%d-%d' % (' ' * depth, v, w))
    
    return printed


def main():
    N = int(input())

    for i in range(1, N + 1):
        V, E = [int(x) for x in input().split()]

        edges = [set() for _ in range(V)]

        for _ in range(E):
            v1, v2 = [int(x) for x in input().split()]
            edges[v1].add(v2)

        print("Caso %d:" % i)

        searched = [False for _ in range(V)]

        for j in range(V):
            if pathR(edges, j, searched):
                print()


main()