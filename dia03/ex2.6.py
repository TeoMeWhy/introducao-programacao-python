# Refaça o exercício 2.2 utilizando for e
# listas para receber as notas dos alunos

notas = []
for i in range(0,4):
    n = float(input(f"Entre com a nota {i+1}: "))
    notas.append(n)

media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

print("Média: ", media)
print("Mínimo: ", minimo)
print("Máximo: ", maximo)
