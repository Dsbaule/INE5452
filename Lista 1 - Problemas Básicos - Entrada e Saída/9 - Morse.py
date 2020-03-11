# -*- coding: utf-8 -*-

morse = {
	"=-" : "a",
	"-===" : "b",
	"-=-=" : "c",
	"-==" : "d",
	"=" : "e",
	"==-=" : "f",
	"--=" : "g",
	"====" : "h",
	"==" : "i",
	"=---" : "j",
	"-=-" : "k",
	"=-==" : "l",
	"--" : "m",
	"-=" : "n",
	"---" : "o",
	"=--=" : "p",
	"--=-" : "q",
	"=-=" : "r",
	"===" : "s",
	"-" : "t",
	"==-" : "u",
	"===-" : "v",
	"=--" : "w",
	"-==-" : "x",
	"-=--" : "y",
	"--==" : "z"
}

numCasos = int(input())

for _ in range(numCasos):
	frase = ""
	words = input().split(".......")
	for word in words:
		letters = word.split("...")
		for letter in letters:
			letter = letter.replace("===","-").replace(".","")
			frase += morse[letter]
		frase += " "
	print(frase.strip())
