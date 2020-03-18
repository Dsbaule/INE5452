num = int(input())

for _ in range(num):
	words = input().split()
	words.sort(key=len, reverse=True)
	answer = ""
	for word in words:
		answer += word + " "
	answer = answer.strip()
	print(answer)