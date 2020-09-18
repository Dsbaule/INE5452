def test():
    n = int(input())

    for _ in range(n):
        input()
        trains = [int(x) for x in input().split()]

        sorted_trains = trains.copy()
        sorted_trains.sort()

        swaps = 0
        while trains != sorted_trains:
            for i in range(len(trains) -1):
                if trains[i] > trains[i + 1]:
                    swaps += 1
                    temp = trains[i + 1]
                    trains[i + 1] = trains[i]
                    trains[i] = temp
        
        print("Optimal train swapping takes {} swaps.".format(swaps))

#test()

test()