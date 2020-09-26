import bisect

def main():
    while True:
        try:
            N = int(input())

            process_queue = list()
            for _ in range(N):
                t, c = [int(x) for x in input().split()]
                process_queue.append((c, t))
                
            total = 0
            cur_time = 1
            cur_process_queue = list()
            while len(process_queue) > 0 or len(cur_process_queue) > 0:
                while len(process_queue) > 0 and process_queue[0][1] <= cur_time:
                    bisect.insort(cur_process_queue, process_queue.pop(0))
                
                if len(process_queue) > 0 and len(cur_process_queue) == 0:
                    cur_time = process_queue[0][1]
                else:
                    cur_process = cur_process_queue.pop(0)
                    total += cur_time - cur_process[1]
                    cur_time += cur_process[0]

            print(total)

        except:
            return

main()