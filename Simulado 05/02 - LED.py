numLeds = [
    6,
    2,
    5,
    5,
    4,
    5,
    6,
    3,
    7,
    6
]

def main():
    n = int(input())

    for _ in range(n):
        number = input()

        sumLeds = 0
        for char in number:
            sumLeds += numLeds[int(char)]

        print('%d leds' % sumLeds)

main()