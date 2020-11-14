from math import factorial

limit = 1_000_000_007

def main():
    try:
        while True:
            word = input()
            count_chars = dict()

            for char in word:
                if char in count_chars:
                    count_chars[char] += 1
                else:
                    count_chars[char] = 1
            
            dividend = 1
            for number in count_chars.values():
                dividend *= factorial(number)

            numerator = factorial(len(word))

            print((numerator//dividend) % limit)


    except EOFError:
        return

main()