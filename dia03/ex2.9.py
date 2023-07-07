# Faça um programa com uma função que recebe uma frase.
# Para cada palavra nesta frase, inverta a ordem das letras.
# Exiba o resultado:

# 	Esta é a frase original
# 	atsE é a esarf lanigiro

frase = input("Entre com uma frase: ")

texto = ""
for palavra in frase.split():
    texto += palavra[::-1] + " "

print(texto)


### OUTRA VERSÃO

frase_invertida = []
for palavra in frase.split():
    frase_invertida.append(palavra[::-1])

print(" ".join(frase_invertida))