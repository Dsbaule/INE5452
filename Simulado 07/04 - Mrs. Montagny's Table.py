class Vertice:
    def __init__(self, number):
        self.number = number
        self.edges = set()
        self.colour = None

    def __repr__(self):
        return f'{self.number} - {self.colour}'


def colour_guest(guest, value = True):
    guest.colour = value

    new_guests = set()
    for friend in guest.edges:
        if friend.colour == value:
            return False
        if friend.colour == None:
            friend.colour = not value
            new_guests.add(friend)

    for friend in new_guests:
        if not colour_guest(friend, not value):
            return False
    
    return True


def main(numInstance: int):
    n, m = [int(x) for x in input().split()]

    guests = [Vertice(i) for i in range(n)]

    for _ in range(m):
        u, v = [int(x) for x in input().split()]

        u -= 1
        v -= 1

        guests[v].edges.add(guests[u])
        guests[u].edges.add(guests[v])
    
    print('Instancia %d' % numInstance)

    for guest in guests:
        if guest.colour == None:
            if not colour_guest(guest):
                print('nao')
                return
    
    print('sim')

try:
    i = 1
    while True:
        main(i)
        print()
        i += 1
except EOFError:
    pass