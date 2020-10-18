def swap(numbers, a, b):
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp

def merge_sort(numbers):
    if len(numbers) < 2:
        return (0, numbers)

    size = len(numbers)//2

    A = numbers[:size]
    B = numbers[size:]

    swaps_a, A = merge_sort(A)
    swaps_b, B = merge_sort(B)

    swaps = swaps_a + swaps_b

    i = j = k = 0

    while i < len(A) and j < len(B): 
        if A[i] < B[j]: 
            numbers[k] = A[i] 
            i+= 1
        else: 
            numbers[k] = B[j]
            swaps += len(A) - i
            j+= 1
        k+= 1
        
    while i < len(A): 
        numbers[k] = A[i] 
        i+= 1
        k+= 1
        
    while j < len(B): 
        numbers[k] = B[j] 
        j+= 1
        k+= 1

    return (swaps, numbers)

def test():
    numbers = [int(x) for x in input().split()]

    if numbers[0] == 0:
        return False
    
    swaps,_ = merge_sort(numbers[1:])

    if swaps % 2:
        print('Marcelo')
    else:
        print('Carlos')

    return True

while(test()):
    pass