def test():
    try:
        while True:
            n = int(input())

            inserted = list()
            taken = list()
            numbers = list()

            priority_queue = True

            for _ in range(n):
                operation, number = [int(x) for x in input().split()]

                if operation == 1:
                    numbers.append(number)
                    inserted.append(number)
                else:
                    taken.append(number)

                    if number in numbers:
                        numbers.remove(number)
                    else:
                        priority_queue = False
                        
                    if priority_queue and not all(i <= number for i in numbers):
                        priority_queue = False

            queue = (inserted == taken)

            inserted.reverse()
            stack = (inserted == taken)

            if (queue and stack) or (queue and priority_queue) or (stack and priority_queue):
                print('not sure')
            elif queue:
                print('queue')
            elif stack:
                print('stack')
            elif priority_queue:
                print('priority queue')
            else:
                print('impossible')

    except EOFError:
        return


test()