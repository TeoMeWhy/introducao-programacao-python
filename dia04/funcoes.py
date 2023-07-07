# y = f(x) = x + 2 * (3 + x)

# y = f(x=1) = 1 + 2 * (3 + 1)
# y = 9

# y = f(x=0) = 0 + 2 * (3 + 0)
# y = 6

# %%
def f(x):
    print("calculando....")
    resultado = x + 2 * (3 + x)
    print("cálculo feito!")
    return resultado

y = f(0)
print(y)

# %%

def soma(a, b=0):
    """
    Função soma realiza a soma de dois valores (a,b). Onde esses dois valores podem ser de qualquer tipo.
    """

    return a + b

soma(10)

# %%
