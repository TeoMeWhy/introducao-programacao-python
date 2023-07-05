# Faça um programa que receba um número.
# Este número corresponde a uma posição na sequência
# de Fibonacci: 0, 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y

numero = int(input("Entre com um numero correspondente à posição Fibonacci: "))

fib_0 = 0
fib_1 = 1

i = 1
while i < numero:
    fib_n = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_n
    i += 1

print(f"A posição {numero} corresponde ao número {fib_0}")
