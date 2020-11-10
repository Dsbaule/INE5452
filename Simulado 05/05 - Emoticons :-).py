import string

def remove_emotes(line: string, emoticons: list):
    index = [0 for _ in emoticons]
    chars_swapped = 0

    line = list(line)

    for i in range(len(line)):
        for j in range(len(emoticons)):
            if line[i] == emoticons[j][index[j]]:
                index[j] += 1
            else:
                index[j] = 1 if line[i] == emoticons[j][0] else 0
            
            if index[j] == len(emoticons[j]):
                line[i] = ' '
                chars_swapped += 1
                index = [0 for _ in emoticons]
    
    return chars_swapped

def main():
    while True:
        N, M = [int(x) for x in input().split()]

        if N == 0 and M == 0:
            return

        emoticons = list()
        for _ in range(N):
            emoticons.append(input())
        
        lines = list()
        for _ in range(M):
            lines.append(input())
        
        minimum = 0
        for line in lines:
            minimum += remove_emotes(line, emoticons)
        
        print(minimum)

main()