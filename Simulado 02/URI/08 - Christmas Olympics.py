import bisect

def main():
    quadro_de_medalhas = dict()

    while True:
        try:
            description = input()
            gold = input()
            silver = input()
            bronze = input()

            winner = quadro_de_medalhas.get(gold, [0, 0, 0])
            winner[0] += 1
            quadro_de_medalhas[gold] = winner

            winner = quadro_de_medalhas.get(silver, [0, 0, 0])
            winner[1] += 1
            quadro_de_medalhas[silver] = winner

            winner = quadro_de_medalhas.get(bronze, [0, 0, 0])
            winner[2] += 1
            quadro_de_medalhas[bronze] = winner

            
        except EOFError:
            result = list()
            for key in quadro_de_medalhas.keys():
                winner = quadro_de_medalhas[key]
                result.append((winner + [key,]))
            result.sort(key=lambda x: x[3], reverse=False)
            result.sort(key=lambda x: x[2], reverse=True)
            result.sort(key=lambda x: x[1], reverse=True)
            result.sort(key=lambda x: x[0], reverse=True)
            print('Quadro de Medalhas')
            for winner in result:
                print('%s %d %d %d' % (winner[3], winner[0], winner[1], winner[2]))
            return

main()