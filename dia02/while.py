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

i = 1
while True:
    
    if i % 2 == 0:
        print("par")
        continue

    if i % 3 == 0:
        pass    

    if i > 10:
        print("Parando o laço WHILE")
        break

    i += 1



# %%

i = int(input("Entre com o valor mínimo para iteração: "))
j = int(input("Entre com o valor máximo para iteração: "))

while i <= j:
    print(i, end=" ")
    i += 1