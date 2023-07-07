# %%
arquivo = open("meu_arquivo.txt", "w")
arquivo.write("Sint consectetur velit officia eu enim ad consequat minim duis in tempor. Consequat sit laboris pariatur pariatur sit enim incididunt dolore fugiat amet labore veniam. Est laborum dolore nulla velit ad in voluptate sunt velit nostrud aliqua non. Voluptate irure nostrud ipsum ea amet eiusmod. Ad excepteur magna exercitation cillum enim proident Lorem officia excepteur laborum pariatur pariatur do. Commodo irure deserunt cupidatat occaecat. Do proident qui ullamco nulla voluptate reprehenderit ullamco quis incididunt in.")
arquivo.close()

# %%

with open("meu_arquivo.txt", "a") as open_file:
    open_file.write("e mais uma vez\n")

# %%

with open("main", "r", encoding='latin1') as open_file:
    text_bin = open_file.read()

print(text_bin)

# %%

with open("dados.csv", "r") as open_file:
    dados = open_file.readlines()

cabecalho = dados[0].replace("\n", "").split(";")

data_dict = {}

for i in cabecalho:
    data_dict[i]=[]

data_dict

for i in dados[1:]:
    valores = i.replace("\n", "").split(";")
    for i in range(len(cabecalho)):
        data_dict[cabecalho[i]].append(valores[i])

data_dict