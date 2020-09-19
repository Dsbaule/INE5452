def test():
    try:
        while True:
            n = int(input())
            
            queue = list()
            stack = list()
            priority_queue = list()

            is_queue = True
            is_stack = True
            is_priority_queue = True

            for _ in range(n):
                operation, number = [int(x) for x in input().split()]

                if operation == 1:
                    if is_queue:
                        queue.append(number)
                    if is_stack:
                        stack.append(number)
                    if is_priority_queue:
                        priority_queue.append(number)
                else:
                    if is_queue:
                        is_queue = (number == queue.pop(0))
                    if is_stack:
                        is_stack = (number == stack.pop(-1))
                    if is_priority_queue:
                        priority_queue.sort()
                        is_priority_queue = (number == priority_queue.pop(-1))

            if (is_queue and is_stack) or (is_queue and is_priority_queue) or (is_stack and is_priority_queue):
                print('not sure')
            elif is_queue:
                print('queue')
            elif is_stack:
                print('stack')
            elif is_priority_queue:
                print('priority queue')
            else:
                print('impossible')

    except EOFError:
        return


test()