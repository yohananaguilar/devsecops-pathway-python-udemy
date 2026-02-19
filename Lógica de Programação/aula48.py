"""
append - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - Apaga um índice
clear - Limpa a lista
extend - Estende a lista
"""

lista = [1, 2, 3, 4, 5, 6]
lista.append('Banana')

item = lista.pop()
lista.append(1234)

del lista[-1]

lista.insert(4, 'Pão')
print(lista)