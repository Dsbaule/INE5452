import string

def remove_emotes(line: string, emoticons: list):
    minimum = 0

    #print(line)
    
    for i in range(len(line)):
        for emote in emoticons:
            if line[i:].startswith(emote):
                """
                cur_minimum = len(line)
                for j in range(len(emote)):
                    character = line
                    cur_minimum = min(cur_minimum, remove_emotes(line[:i + j] + line[i + j + 1:], emoticons))
                """
                return 1 + remove_emotes(line[:i] + line[i + len(emote):], emoticons)
    
    return minimum


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
