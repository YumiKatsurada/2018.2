#-*- encoding: utf-8 -*-

#o jogo sempre começa com jake
#jake ganha - numero de inversoes: impar
#finn ganha - numero par

#entrada = str(input("casos de teste"))

#num = entrada[0]

entrada = 32415

for i in range(entrada):
	if entrada[i] > entrada[i+1]:
		aux = entrada[i]
		entrada[i] = entrada[i+1]
		entrada[i+1] = aux

print(entrada)  
