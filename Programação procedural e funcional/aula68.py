# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero

    return total

total_multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(total_multiplicacao)


