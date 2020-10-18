from pprint import pprint

class Student:
    def __init__(self, string):
        self.string1, self.string2 = string.split('/')
    def __repr__(self):
        return self.string1 + '/' + self.string2
    def __eq__(self, otherStudent):
        return self.string1 == otherStudent.string1 and self.string2 == otherStudent.string2
    def __lt__(self, otherStudent):
        if self.string1 == otherStudent.string1:
            return int(self.string2) < int(otherStudent.string2)
        return self.string1 < otherStudent.string1
    def __le__(self, otherStudent):
        return self.__eq__(otherStudent) or self.__lt__(otherStudent)


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
        if A[i] <= B[j]: 
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
    n = int(input())
    
    students = list()

    for _ in range(n):
        students.append(Student(input()))
    
    swaps,students = merge_sort(students)

    print(swaps)
    pprint(students)

test()
