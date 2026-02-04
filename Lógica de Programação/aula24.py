"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] onde i = início, f = fim e p = passo
Obs: a função len retorna a quantidade de caracteres da str
"""
variavel = 'Olá Mundo'
print(variavel[4:8])  # Exibe "Mund"
print(len(variavel))  # Exibe o comprimento da string (9 caracteres)
print(variavel[0:len(variavel):1])  # Exibe a string completa com passo 1
print(variavel[::-1])  # Exibe a string invertida