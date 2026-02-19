"""
append - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - Apaga um índice
clear - Limpa a lista
extend - Estende a lista
"""

lista = [10, 20, 30, 40, 50]

indice = int(input('Digite algo para adicionar na lista: '))
lista.append(indice)

print(lista)

indice_removido = int(input('Digite qual índice deseja remover: '))
removido = lista.pop(indice_removido)

print(f'O {removido} foi removido da lista = {lista}')