def main():
    while True:
        n = int(input())

        if n == 0:
            return

        numbers = [int(x) for x in input().split()]

        seen = set()

        for number in numbers:
            if number not in seen:
                seen.add(number)
            else:
                seen.remove(number)
        
        print(seen.pop())

main()