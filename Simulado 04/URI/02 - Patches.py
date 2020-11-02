def main():
    N, C, T1, T2 = [int(x) for x in input().split()]

    LG = max(T1, T2)
    SM = min(T1, T2)

    holes = [int(x) for x in input().split()]
    #print(holes)

    minLen = None    

    diffs = list()
    for i in range(len(holes) - 1):
        diffs.append(holes[i + 1] - holes[i])
    print(str(holes) + ' ' + str(diffs))

    minLen = 0
    leftover = -1
    i = 0
    while(i < len(diffs)):

        numLG = 0
        sumLG = 0
        while i + numLG < len(diffs) and sumLG < LG:
            sumLG += diffs[i + numLG]
            numLG += 1
        
        numSM = 0
        sumSM = 0
        while i + numSM < len(diffs) and sumSM < SM:
            sumSM += diffs[i + numSM]
            numSM += 1
        
        if numLG > numSM:
            leftover = LG
        else:
            leftover = SM

        minLen += leftover
        leftover -= 1

        while((i < len(diffs)) and (leftover > 0)):
            leftover -= diffs[i]
            i += 1

    print(minLen)
    


try:
    while(True):
        main()
except EOFError:
    pass