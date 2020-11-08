import string

def main():
    n = int(input())

    for _ in range(n):
        frase = input().lower()
        most_common = list()
        num_most_common = 0

        for char in string.ascii_lowercase:
            count_char = frase.count(char)
            if count_char > num_most_common:
                num_most_common = count_char
                most_common = [char]
            elif count_char == num_most_common:
                most_common.append(char)

        most_common.sort()
        print(''.join(most_common))



main()