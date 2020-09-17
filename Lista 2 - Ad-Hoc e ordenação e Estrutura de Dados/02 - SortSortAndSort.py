def sort(numbers, integer):
    buckets  = [[] for _ in range((integer * 2) - 1)]

    for number in numbers:
        buckets[integer - 1 + mod(number, integer)].append(number)
    
    sorted_numbers = list()
    for bucket in buckets:
        sorted_numbers += sort_bucket(bucket)
    
    return sorted_numbers

def sort_bucket(bucket):
    odd = list()
    even = list()

    for number in bucket:
        if mod(number, 2) == 0:
            even.append(number)
        else:
            odd.append(number)
    
    return sort_odds(odd) + sort_even(even)

def sort_even(numbers):
    numbers.sort()
    return numbers

def sort_odds(numbers):
    numbers.sort(reverse=True)
    return numbers

def mod(n, d):
    if n < 0:
        return -((-n) % d)
    else:
        return n % d

while True:
    n, m = (int(x) for x in input().split())
    print(str(n) + ' ' + str(m))

    if n == 0 and m == 0:
        break

    numbers = list()
    for _ in range(n):
        numbers.append(int(input()))

    for number in sort(numbers, m):
        print(number)
