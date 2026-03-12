"""
args - Argumentos não nomeados
* - *args(empacotamento e desempacotamento)
"""

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma(1, 2, 3)
print(soma_1)

soma_2 = soma(4, 5, 6)
print(soma_2)

numeros = 1, 2, 3, 4, 5, 6
soma_3 = soma(*numeros)
print(soma_3)

print(sum(numeros))