def main():
    T = int(input())

    for i in range(T):
        team = [int(x) for x in input().split()][1:]
        print('Case %d: %d' % (i + 1, team[len(team)//2]))

main()