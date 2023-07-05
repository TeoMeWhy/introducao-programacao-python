# %%

nome = "Téo Calvo"

j = 1
for i in nome:
    print("Elemento ", j, ": ", i, sep="")
    j += 1


# %%
for i in range(10):
    print(i)


# %%
i = int(input("Entre com o valor mínimo: "))
j = int(input("Entre com o valor máximo: "))

for i in range(i, j+1):
    print(i)