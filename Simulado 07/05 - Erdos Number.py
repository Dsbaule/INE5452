class Vertice:
    def __init__(self, name):
        self.name = name
        self.first_name = name.split('. ')[0]
        self.last_name = name.split('. ')[-1]
        self.edges = set()
        self.searched = False
        self.erdos_number = 'infinito'

    def __lt__(self, other_vertice):
        if self.last_name < other_vertice.last_name:
            return True
        elif self.first_name < other_vertice.first_name:
            return True
        else:
            return False


def main(num_teste):
    A = int(input())

    if A == 0:
        return False
    
    authors = dict()
    #authors['P. Erdos'] = Vertice('P. Erdos')

    for _ in range(A):
        article_authors = input()[:-1].split(', ')
        for author in article_authors:
            if authors.get(author, None) is None:
                authors[author] = Vertice(author)
        for author in article_authors:
            authors[author].edges.update(authors[x] for x in article_authors if x != author)

    erdos = authors.get('P. Erdos', None)

    if erdos:
        erdos_authors = [[erdos]]

        i = 0
        while True:
            if not erdos_authors[i]:
                break
            
            erdos_authors.append([])

            for author in erdos_authors[i]:
                author.erdos_number = str(i)
                author.searched = True
            
            for author in erdos_authors[i]:
                for new_author in author.edges:
                    if not new_author.searched:
                        erdos_authors[i + 1].append(new_author)
            
            i += 1

    author_list = list(authors.values())
    author_list.sort()

    print('Teste %d' % num_teste)
    for author in author_list:
        if author.name != 'P. Erdos':
            print('%s: %s' % (author.name, author.erdos_number))

    return True

i = 1
while main(i):
    i += 1
    print()
