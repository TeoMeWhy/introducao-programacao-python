try:
    numero = int(input("Entre com um número da sorte entre 1 e 15: "))

    sorte = 7

    if numero < sorte:
        print("Tente um número maior!")

    elif numero > sorte:
        print("Tente um número menor!")

    else:
        print("Acertou miserávi!")

except ValueError as err:
    print("Deu merda! Tenta um número válido!")
    print(err)