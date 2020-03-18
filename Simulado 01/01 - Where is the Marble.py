maxNumber = 10000

line = [int(number) for number in input().split()]
N = line[0]
Q = line[1]

while((N is not 0) or (Q is not 0)):
	marbles[maxNumber] = 0
	for _ in range(N):
		marble = int(input())
		marbles[marble] += 1
	for case in range(Q):
		query = int(input())

		print("CASE# " + str(case + 1) + ":")
		if marbles[query] > 0:
			total = 1;
			for marble in marbles[:query]:
				total += marble
			print(str(query) + " found at " + str(total))
		else:
			print(str(query) + " not found")
	line = [int(number) for number in input().split()]
	N = line[0]
	Q = line[1]
