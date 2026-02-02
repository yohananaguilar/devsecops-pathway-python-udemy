"""
Formatação básica de strings
s - float
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex. 0>-100, .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')  # Alinha à direita com 10 caracteres
print(f'{variavel:<10}')  # Alinha à esquerda com 10 caracteres
print(f'{variavel:^10}')  # Alinha ao centro com 10 caracteres
print(f'{12092.92932913:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')