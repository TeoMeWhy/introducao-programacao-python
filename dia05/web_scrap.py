# %%
import requests

url = "https://pt.wikipedia.org/wiki/Brasil"

resposta = requests.get(url)

with open("wiki_brasil.txt", "w") as open_file:
    open_file.write(resposta.text)


# %%

url_poke = "https://pokeapi.co/api/v2/pokemon/ditto"

reposta_poke = requests.get(url_poke)
data = reposta_poke.json()

# %%

data.keys()

# %%

data["stats"]