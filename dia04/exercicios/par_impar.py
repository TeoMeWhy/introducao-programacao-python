def par_impar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "impar"
    
n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com um número: "))

print(f"O número {n1} é {par_impar(n1)}!")
print(f"O número {n2} é {par_impar(n2)}!")