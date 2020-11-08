def test_one():
    word = input()
    letters = set(word)

    num_letters = 0

    for letter in letters:
        if word.count(letter) % 2 != 0:
            num_letters += 1

    print(max(num_letters - 1, 0))

def main():
    try:
        while True:
            test_one()
    except EOFError:
        return

main()