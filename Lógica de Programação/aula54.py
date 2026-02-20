"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Bil', 'Rodrigo', 'Gabriel', 'Gustavo', 'Nathan']

lista.append('João')

for indice, nome in enumerate(lista):
    print(f'indice: {indice}', f'nome: {nome}')