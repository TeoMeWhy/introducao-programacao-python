# Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores. Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

frutas = {
    "maçã":"1.50",
    "banana":"2.75",
    "uva":"1.90",
    "pera":"1.25",
    "laranja":"0.65",
    "limão":"1.25",
    "goiaba":"2.15",
    "abacaxi":"3.20",
    "jaca":"5.80",
}

fruta = input("Entre com o nome de uma fruta: ")

if fruta in frutas.keys():
    preco = frutas[fruta]
    print(f"A fruta {fruta} custa R${preco}")

else:
    print(f"A fruta {fruta} não foi encontrada.")
