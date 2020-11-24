def main():
    while True:
        x, y = input().split()

        if x == y == "0":
            return

        x = x.rjust(10,"0")
        y = y.rjust(10,"0")
        
        num_carries = 0
        carry = 0

        for i in range(9,-1,-1):
            cur_x = int(x[i])
            cur_y = int(y[i])

            result = cur_x + cur_y + carry
            carry = 0

            if result >= 10:
                num_carries += 1
                carry = 1
        
        if num_carries == 0:
            print('No carry operation.')
        elif num_carries == 1:
            print('1 carry operation.')
        else:
            print('%d carry operations.' % num_carries)

main()