def test():
    m = int(input())

    for k in range(m):
        n, _ =  [int(x) for x in input().split()]
        numbers = [int(x) for x in input().split()]

        hash_table = dict()

        for i in range(n):
            hash_table[i] = list()

        for number in numbers:
            hash_table[number % n].append(number)
            
        if k != 0:
            print()
        for i in range(n):
            table_string =  str(i) + ' -> '

            for number in hash_table[i]:
                table_string +=  str(number) + ' -> '
            
            table_string += '\\'

            print(table_string)
            

#test()

test()