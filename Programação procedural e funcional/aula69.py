# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O número>: {numero} é par'
    return f'O número: {numero} é impar'
    
print(par_ou_impar(1))
