def test_one():
    w1 = input()
    w2 = input()
    display = input()

    first_letter = None
    second_letter = None

    for i in range(len(display)):
        if display[i] == '_':
            if first_letter is None:
                first_letter = i
            else:
                second_letter = i
                break
    
    print('Y' if w1[first_letter] == w2[second_letter] or w1[second_letter] == w2[first_letter] else 'N')

def main():
    N = int(input())

    for _ in range(N):
        test_one()

main()