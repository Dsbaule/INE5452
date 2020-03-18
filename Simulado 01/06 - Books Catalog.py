P = [int(number) for number in input().split()[1:]]
M = [int(number) for number in input().split()[1:]]
F = [int(number) for number in input().split()[1:]]
Q = [int(number) for number in input().split()[1:]]
B = [int(number) for number in input().split()[1:]]

permutations = list()

for p in P:
	for m in M:
		for f in F:
			for q in Q:
				for b in B:
					permutations.append((p + m + f + q + b))

permutations.sort(reverse=True)

numberOfSets = int(input())

total = sum(permutations[:numberOfSets])

print(str(total))
	