# %%

# lista vazia
minha_lista = list()
minha_lista

# %%
dados_teo = ["Teo", "Calvo", 31, "Natalia", ["Maria", "Stefani", "Josefina"] ]
dados_teo

# %%
type(dados_teo)

# %%
exs = dados_teo[-1]
print(exs)
print(type(exs))

# %%
print(exs[-1])
print(dados_teo[-1][-1])

print(dados_teo[-1][:2])

print(dados_teo[3][:3].upper())

# %%
len(dados_teo)

# %%

idades = [34,37,30,19,25,26,26,21,33]
media = sum(idades) / len(idades)

# %%
total = 0
for i in idades:
    total += i

media = total / len(idades)
print(media)

# %%

idades.sort(reverse=True)
idades

# %%
idades.append(26)
idades

# %%
novas_idades = [56, 27, 36, 19, 30, 34, 25, 45, 19, 27, 52, 33]
novas_idades

# %%
idades.append(novas_idades)
idades.remove(novas_idades)
print(idades)

# %%
idades.extend(novas_idades)
# idades = idades + novas_idades
idades

# %%

a = [1,2,3]
b = a.copy()
# ou b = a[:]

b.remove(2)
print("b:", b)
print("a:", a)

# %%

