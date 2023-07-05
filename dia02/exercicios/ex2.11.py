# Faça um programa que receba um número e retorne seu fatorial.

numero = int(input("Entre com um número: "))

fatorial = 1
for i in range(2, numero+1):
    fatorial *= i

print(fatorial)