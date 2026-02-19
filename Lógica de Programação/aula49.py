"""
append - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - Apaga um índice
clear - Limpa a lista
extend - Estende a lista
+ - concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_a)