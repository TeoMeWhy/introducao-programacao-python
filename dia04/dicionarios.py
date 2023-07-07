# %%

meus_dados = {}

meus_dados["nome"] = "Téo"

meus_dados["sobrenome"] = "Calvo"

meus_dados["esposa"] = {"nome":"Nah", "idade":32}

meus_dados["exs"] = ['Stéfani', "Maria", "Clara"]

meus_dados['descendentes'] = [{"nome":"Maricota"}, {"nome":"Raul"}]

meus_dados

# %%

meus_dados["esposa"]["idade"]

meus_dados["esposa"]["profissao"] = "Artesã"

meus_dados

# %%

meus_dados["descendentes"].append({"nome": "Pedrinho"})
meus_dados

# %%

# Descobrindo as chaves de um dicionário
meus_dados.keys()

# %%

# Descobrindo valores
meus_dados.values()

# %%

# Tuplas de chave/valor
meus_dados.items()

# %%

del meus_dados["exs"]
meus_dados
# %%

teo = {"nome":"Téo", "idade":30}

mais_infos = {"profissao": "streamer",
              "tempo no cargo": 2}

novas_infos = {"esposa":"Nah"}

teo.update(mais_infos)
teo.update(novas_infos)
teo