def main():
    while True:
        try:
            N = int(input())

            total = 0
            next_t = 1

            process_queue = list()
            for _ in range(N):
                t, c = [int(x) for x in input().split()]
                process_queue.append((t, c))
            
            total = 0
            cur_time = 1
            while len(process_queue) > 0:
                selected = 0

                if process_queue[0][0] >= cur_time:
                    cur_time = process_queue[0][0]
                
                for i in range(1, len(process_queue), 1):
                    if process_queue[i][0] > (process_queue[selected][0] + process_queue[selected][1]):
                        break
                    if process_queue[i][0] <= cur_time:
                        if process_queue[i][1] < process_queue[selected][1]:
                            selected = i
                    else:
                        break

                total += cur_time - process_queue[selected][0]
                cur_time += process_queue[selected][1]
                process_queue.pop(selected)


            print(total)

        except:
            return

main()