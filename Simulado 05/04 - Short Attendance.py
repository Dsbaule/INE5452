
def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        students = input().split()
        attendeance = input().split()

        short_attendance = list()

        for i in range(N):
            A = 0
            P = 0

            for session in attendeance[i]:
                if session == 'A':
                    A += 1
                elif session == 'P':
                    P += 1
            
            if (A * 3) > P:
                short_attendance.append(students[i])

        print(' '.join(short_attendance))


main()