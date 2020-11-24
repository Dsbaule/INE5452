class Vertice:
    def __init__(self):
        self.edges = set()
        self.searched = False

def main():
    n, G = [int(x) for x in input().split()]

    relationships = dict()
    relationships['Rerisson'] = Vertice()

    for _ in range(n):
        S, T = input().split()

        person = relationships.get(S, None)

        if person is None:
            relationships[S] = Vertice()
            person = relationships[S]
        
        person.edges.add(T)

        person = relationships.get(T, None)

        if person is None:
            relationships[T] = Vertice()
            person = relationships[T]
        
        person.edges.add(S)
    
    depth_search = [set() for _ in range(G)]

    depth_search[0] = relationships.get('Rerisson').edges
    relationships.get('Rerisson').searched = True

    invited = set()

    for i in range(G):
        if not depth_search[i]:
            break
        for person in depth_search[i]:
            invited.add(person)
            if person in relationships and not relationships[person].searched:
                relationships[person].searched = True
                if i < (G - 1):
                    depth_search[i + 1].update(relationships[person].edges)
    
    invited.discard('Rerisson')
    invited = list(invited)
    invited.sort()

    print(len(invited))
    for person in invited:
        print(person)
    

main()