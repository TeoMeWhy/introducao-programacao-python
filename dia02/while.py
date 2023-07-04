# %%
i = 1
while i <= 10:
    print("FODASE: ", i)
    i += 1

# %%

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        print("Parando o laço WHILE")
        break

# %%

i = int(input("Entre com o valor mínimo para iteração: "))
j = int(input("Entre com o valor máximo para iteração: "))

while i <= j:
    print(i, end=" ")
    i += 1