def main():
    while True:
        number = input()

        if number[0] == '-':
            return

        if len(number) > 2 and number[1] == 'x':
            print(int(number, 0))
        else:
            print('0x' + hex(int(number)).upper()[2:])


main()