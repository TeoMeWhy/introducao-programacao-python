# Escreva um programa que exiba os números de 1 a 100.
# Caso o número seja divisível por 3, exiba “Fizz” no seu lugar, 
# e para múltiplos de 5 exiba “Buzz”.
# Caso seja divisível por ambos, exiba “FizzBuzz”.

for i in range(1, 101):

    msg = ""
    if i % 3 == 0:
        msg = msg + "Fizz"

    if i % 5 == 0:
        msg = msg + "Buzz"

    if msg == "":
        msg = i
    
    print(msg)