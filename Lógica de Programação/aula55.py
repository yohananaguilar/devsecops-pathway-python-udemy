"""
Faça uma lista de comprar com listas 
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    print('Selecione uma opção')
    opcoes = input('[i]nserir [a]pagar [l]istar [e]ncerrar: ')

    if opcoes == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_de_compras.append(valor)

    elif opcoes == 'a':
        os.system('cls')
        indice = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(indice)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')

    elif opcoes == 'l':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('Nada para listar') 

        for indice, produto in enumerate(lista_de_compras):
                print(f'{indice}', f' {produto}')
