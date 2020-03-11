num = int(input())

for i in range(1, num + 1):
    a, b = input().split()
    
    if a == b:
        print('Caso #' + str(i) + ': De novo!')
    elif a == 'tesoura':
        if b == 'papel' or b == 'lagarto':
            print('Caso #' + str(i) + ': Bazinga!')
        else:
            print('Caso #' + str(i) + ': Raj trapaceou!')
    elif a == 'papel':
        if b == 'pedra' or b == 'Spock':
            print('Caso #' + str(i) + ': Bazinga!')
        else:
            print('Caso #' + str(i) + ': Raj trapaceou!')
    elif a == 'pedra':
        if b == 'lagarto' or b == 'tesoura':
            print('Caso #' + str(i) + ': Bazinga!')
        else:
            print('Caso #' + str(i) + ': Raj trapaceou!')
    elif a == 'lagarto':
        if b == 'Spock' or b == 'papel':
            print('Caso #' + str(i) + ': Bazinga!')
        else:
            print('Caso #' + str(i) + ': Raj trapaceou!')
    else:
        if b == 'tesoura' or b == 'pedra':
            print('Caso #' + str(i) + ': Bazinga!')
        else:
            print('Caso #' + str(i) + ': Raj trapaceou!')
            
