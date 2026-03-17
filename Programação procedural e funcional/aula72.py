# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro

number = int(input('Digite um número: '))

def duplicar(multiplicador):
    def multiplicar(number):
        return number * multiplicador
    return multiplicar

duplicar_numero = duplicar(2)
triplicar_numero = duplicar(3)
quadruplicar_numero = duplicar(4)

print(duplicar_numero(number))
print(triplicar_numero(number))
print(quadruplicar_numero(number))