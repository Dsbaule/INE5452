def main():
    frase = input()
    palavras = frase.split(' ')
    
    for i in range(len(palavras)):
        if len(palavras[i]) > 4 and palavras[i][0:2] == palavras[i][2:4]:
            palavras[i] = palavras[i][:2] + palavras[i][4:]

    print(' '.join(palavras))

main()