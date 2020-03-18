yes = list()
no = list()
nameLength = 0;

while(True):
	current = input().split()
	if current == ["FIM"]:
		break

	if current[1] == "YES":
		yes.append(current[0])
		if len(current[0]) > nameLength:
			nameLength = len(current[0])
			winner = current[0]
	else:
		no.append(current[0])

yes = list(dict.fromkeys(yes))
yes.sort()
for name in yes:
	print(name)
no = list(dict.fromkeys(no))
no.sort()
for name in no:
	print(name)
print()
print("Amigo do Habay:")
print(winner)
