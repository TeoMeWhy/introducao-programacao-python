# Faça um programa que receba 4 notas de um aluno.
# Retorne a média dessas notas, a menor e a maior nota:
# Média: x
# Menor: y
# Maior: z

n1 = float(input("Entre com a nota 1: "))
n2 = float(input("Entre com a nota 2: "))
n3 = float(input("Entre com a nota 3: "))
n4 = float(input("Entre com a nota 4: "))

notas = [n1,n2,n3,n4]

media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

print("Média:", media)
print("Menor:", minimo)
print("Maior:", maximo)