# Escreva um programa que receba uma lista de números do usuário
# e conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

numeros = []

while True:
    entrada = input("Entre com um número: ")

    if entrada == "":
        break

    numeros.append(int(entrada))

numero_check = int(input("Entre com um número para checar a quantidade: "))

total = 0
for i in numeros:
    if i == numero_check:
        total += 1

print(f"O número {numero_check} aparece {total} vezes.")
print(f"Ou {numeros.count(numero_check)}")