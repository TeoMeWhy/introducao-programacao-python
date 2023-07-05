# Faça um programa que receba um número.
# Verifique se este número é primo ou não, e retorne o resultado:
# 	O número x é primo
# ou
# 	O número x não é primo

# %%
numero = int(input("Entre com um número: "))

check = False
for i in range(2,numero):
    if numero % i == 0:
        check = True
        break

if check:
    print(f"O número {numero} não é primo")

else:
    print("O número é primo!")

# %%

numero = int(input("Entre com um número: "))

check = False
for i in range(2,numero):
    if numero % i == 0:
        print(f"O número {numero} não é primo")
        break

else:
    print("O número é primo!")