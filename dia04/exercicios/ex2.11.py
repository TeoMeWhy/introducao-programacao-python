# Faça um programa que receba um número e retorne seu fatorial.

def fat(x):
    total = 1
    for i in range(2,x+1):
        total *= i
    return total

n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com um número: "))

fat_n1 = fat(n1)
fat_n2 = fat(n2)

print(f"{n1}! = {fat_n1}")
print(f"{n2}! = {fat_n2}")