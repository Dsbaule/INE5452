def main():
    M, N = [int(x) for x in input().split()]

    if not M and not N:
        return False
    
    with_previous_row = 0
    without_previous_row = 0

    for _ in range(M):

        with_previous_column = 0
        without_previous_column = 0

        row = [int(x) for x in input().split()]
        for j in range(N):
            # Get max
            temp = with_previous_column
            with_previous_column = max(without_previous_column, with_previous_column)
            without_previous_column = temp + row[j]

        temp = with_previous_row
        with_previous_row = max(without_previous_row, with_previous_row)
        without_previous_row = temp + max(without_previous_column, with_previous_column)
            
    print(max(without_previous_row, with_previous_row))
    return True




while(main()):
    pass