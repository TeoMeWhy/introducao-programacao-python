# Faça um programa que receba o raio de uma circunferência em centímetros.
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy

raio = float(input("Entre com o tamanho do raio: "))

area = 3.14 * raio * raio # 3.14 * (raio ** 2)
perimetro = 2 * 3.14 * raio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")