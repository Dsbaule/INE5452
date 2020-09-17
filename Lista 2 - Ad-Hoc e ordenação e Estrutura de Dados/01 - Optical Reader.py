alternativas = ['A', 'B', 'C', 'D', 'E']

def checkAnswer(n):
    gray = None
    for i in range(5):
        if n[i] <= 127:
            if gray is not None:
                return None
            gray = i
    return gray

while True:
    n =  input().split()

    if len(n) == 1:
        n = int(n[0])
        if n == 0:
            break
    else:
        n = [int(x) for x in n]

        gray = checkAnswer(n)

        if gray is not None:
            print(alternativas[gray])
        else:
            print('*')