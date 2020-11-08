def test_case(word):
    costs = test_p(word, 0)

    if costs is None:
        costs = 0
    
    print(costs)

def test_p(word, i):
    if i >= len(word):
        return 0
    
    if word[i] == 'a':
        test = test_p(word, i + 1)
        return test

    elif word[i] == 'b':
        cost = test_p(word, i + 1)
        cost += test_q(word, i + 1)        
        return cost

def test_q(word, i):
    if i >= len(word):
        return 1
    
    test = test_q(word, i + 1)
    return test * 2


def main():
    case = 1
    try:
        while(True):
            word = input()
            print('Palavra %d' % case)
            test_case(word)
            print()
            case += 1
    except EOFError:
        return

main()