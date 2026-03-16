"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

funcao_executada = executa(saudacao, 'Bom dia', 'Luiz')
print(funcao_executada)