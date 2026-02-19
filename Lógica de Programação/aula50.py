"""
Cuidados com dados mutáveis
= - copiado o valor (imútaveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Barrocos']
lista_b = lista_a

lista_a[0] = 'Santos'
print(lista_b)