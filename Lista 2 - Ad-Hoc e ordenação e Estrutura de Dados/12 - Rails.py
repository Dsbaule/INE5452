def checkPermutation(n, permutation):
    curr = 0
    station = []
    for i in range(1, n + 1):

        station.append(i)

        while station and station[-1] == permutation[curr]:
            station.pop()
            curr += 1
        
    return curr >= len(permutation)


    

def main():
    while True:
        n = int(input())

        if n == 0:
            return

        while True:
            input_string = input()

            if input_string == '0':
                print()
                break

            permutation = [int(x) for x in input_string.split()]

            if checkPermutation(n, permutation):
                print('Yes')
            else:
                print('No')

main()