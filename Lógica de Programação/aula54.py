"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Bil', 'Rodrigo', 'Gabriel', 'Gustavo', 'Nathan']

lista.append('João')

lista_enumerada = enumerate(lista)

for indice, nome in lista_enumerada:
    print(f'indice: {indice}', f'nome: {nome}')