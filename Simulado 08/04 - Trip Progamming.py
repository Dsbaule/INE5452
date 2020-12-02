class Vertice:
    def __init__(self):
        self.edges = set()
        self.searched = False

def findmax(graph, V):
    if V == 0:
        return ([0], 0)

    min_time = None
    path = []

    graph[V].searched = True

    for city, time in graph[V].edges:
        #print((city, time))
        if not graph[city].searched:
            cur_path, cur_min = findmax(graph, city)
            if cur_min != None:
                cur_min += time
                if min_time == None or cur_min < min_time:
                    min_time = cur_min
                    path = cur_path
    graph[V].searched = False
    return ([V] + path, min_time)

def main():
    while True:
        C, E = [int(x) for x in input().split()]

        if C == E == 0:
            return

        graph = [Vertice() for _ in range(C)]
        for _ in range(E):
            C1, C2, T = [int(x) for x in input().split()]
            C1 -= 1
            C2 -= 1
            graph[C1].edges.add((C2, T))
            graph[C2].edges.add((C1, T))

        D = int(input())

        path, time = findmax(graph, D - 1)
        path = ' '.join(str(x + 1) for x in path)
        late = 120 - time

        if late > 0:
            print('Will not be late. Travel time - %d - best way - %s' % (time, path))
        else:
            print('It will be %d minutes late. Travel time - %d - best way - %s' % (-late, time, path))


main()