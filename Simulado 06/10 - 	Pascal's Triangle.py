def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        result = 1
        for i in range(N - 1):
            result += (2 << i)

        print(result)

main()