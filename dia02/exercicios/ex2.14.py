# Escreva um programa que solicite ao usuário um número
# e exiba a tabuada desse número de 1 a 10.

numero = int(input("Entre com um número: "))

for i in range(1,11):
    res = numero * i
    txt = f"{numero:2} x {i:2} = {res}"
    print(txt)