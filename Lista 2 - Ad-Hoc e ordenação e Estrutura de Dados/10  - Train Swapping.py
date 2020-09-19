def swap(train, a, b):
    temp = train[a]
    train[a] = train[b]
    train[b] = temp

def sort_train(train):
    swaps = 0

    while True:
        something_changed = False

        for i in range(len(train) - 1):
            if train[i] > train[i + 1]:
                something_changed = True
                swaps += 1
                swap(train, i, i+1)

        if not something_changed:
            break
    
    return swaps


def test():
    n = int(input())

    for _ in range(n):
        input()
        trains = [int(x) for x in input().split()]
        
        #print(trains)
        swaps = sort_train(trains)
        #print(trains)
        
        print("Optimal train swapping takes {} swaps.".format(swaps))

#test()

test()