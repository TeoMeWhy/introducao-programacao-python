# Faça um programa que receba dois valores A e B.
# Faça a potência desses dois valores e retorne o resultado:
# a ^ b = z

a = float(input("Entre com o valor de A: "))
b = float(input("Entre com o valor de B: "))

print(a, "^", b, "=", a ** b)

msg = f"{a}^{b} = {a**b}"
print(msg)