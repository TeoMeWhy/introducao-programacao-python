# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

menor = min(lista)
maior = max(lista)

menor_index = lista.index(menor)
maior_index = lista.index(maior)

print("O maior valor está na posição: ", maior_index)
print("O menor valor está na posição: ", menor_index)