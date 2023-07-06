# %%
meu_nome = "Teodoro calvo"
type(meu_nome)

# %%

meu_nome_upper =  meu_nome.upper()

print(meu_nome_upper)
print(meu_nome)

# %%

meu_nome_lower =  meu_nome.lower()

print(meu_nome_lower)
print(meu_nome)

# %%
# caixa alta para início de palavras
meu_nome.title()

# %%
meu_nome.endswith("calvo")

# %%
meu_nome.startswith("Teo")

# %%
meu_nome.lower().startswith("teo")

#########################################
## FATIAMENTO
#########################################

# %%

# posição 0 (primeira posição)
meu_nome[0]

# %%
meu_nome[1]

# %%
len(meu_nome)
# 13

# %%
meu_nome[12]

# %%
meu_nome[len(meu_nome)-1]

# %%
meu_nome[-3]

# %%
meu_nome[0:3] # start:stop (range = stop - start)

# %%
meu_nome[0:-1]

# %%
meu_nome[:-2]

# %%
meu_nome[3:]

# %%
meu_nome[:]

# %%
meu_nome[3:10:2]

# %%
meu_nome[::2]

# %%
meu_nome[::-1]