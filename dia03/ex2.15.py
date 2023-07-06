# Escreva um programa que solicite ao usuário uma palavra
# e verifique se a palavra é um palíndromo
# (ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input("Entre com um palavra: ")

if palavra.lower() == palavra[::-1].lower():
    print(f"A palavra {palavra} é palindromo!")

else:
    print(f"A palavra {palavra} não é palindromo!")