# Class to implement union find Node
class No:
    # New node has given value, rank 0 and is it's own father
    def __init__(self):
        self.rank = 0
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

def main():
    while True:
        m, n = [int(x) for x in input().split()]

        if m == n == 0:
            return

        roads = list()
        total_cost = 0

        for _ in range(n):
            x, y, z = [int(x) for x in input().split()]
            roads.append((z, x, y))
            total_cost += z

        roads.sort()

        junctions = [No() for _ in range(m)]
        new_cost = 0

        while roads:
            z, x, y = roads.pop(0)

            if junctions[x].encontrar() != junctions[y].encontrar():
                junctions[x].unir(junctions[y])
                new_cost += z

        print(new_cost)

main()