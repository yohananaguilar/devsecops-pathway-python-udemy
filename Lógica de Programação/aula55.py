"""
Faça uma lista de comprar com listas 
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

lista_de_compras = []

while True:
    print('Selecione uma opção')
    opcoes = input('[i]nserir [a]pagar [l]istar [e]ncerrar: ')

    LETRAS_PERMITIDAS = ('i', 'a', 'l', 'e')

    if not LETRAS_PERMITIDAS:
        print('Tente novamente, opção inválida!')
        continue

    elif opcoes == 'i':
        valor = input('Valor: ')
        lista_de_compras.append(valor)
        print(lista_de_compras)
        continue

    elif opcoes == 'a':
        indice = int(input('Escolha o índice para apagar: '))
        lista_de_compras.pop(indice)
        print(lista_de_compras)
        continue

    elif opcoes == 'l':
        for indice, produto in enumerate(lista_de_compras):
                print(f'{indice}', f' {produto}')

    if opcoes == 'e':
        print('Programa encerrado')
        break  