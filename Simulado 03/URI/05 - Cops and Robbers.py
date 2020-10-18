def tryPath(gameMap, row = 0, column = 0, tried = None):
    if gameMap[row][column] == 1:
        return False
    if row == 4 and column == 4:
        return True

    if tried == None:
        tried = [[False for _ in range(5)] for _ in range(5)]
    
    tried[row][column] = True
    found = False

    if (row < 4) and (not tried[row + 1][column]) and (gameMap[row + 1][column] == 0):
        found |= tryPath(gameMap, row + 1, column, tried)
    if (not found) and (column < 4) and (not tried[row][column + 1]) and (gameMap[row][column + 1] == 0):
        found |= tryPath(gameMap, row, column + 1, tried)
    if (not found) and (row >= 1) and (not tried[row - 1][column]) and (gameMap[row - 1][column] == 0):
        found |= tryPath(gameMap, row - 1, column, tried)
    if (not found) and (column >= 1) and (not tried[row][column - 1]) and (gameMap[row][column - 1] == 0):
        found |= tryPath(gameMap, row, column - 1, tried)
    
    tried[row][column] = False
    
    return found

def test():
    n = int(input())

    for _ in range(n):
        input()
        gameMap = [[int(x) for x in input().split()] for _ in range(5)]
        print('COPS' if tryPath(gameMap) else 'ROBBERS')

test()