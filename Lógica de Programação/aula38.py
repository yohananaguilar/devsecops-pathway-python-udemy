""" Calculadora com while """

while True:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    num_validos = None

    try:
        num1 = float(num1)
        num2 = float(num2)
        num_validos = True
    except ValueError:
        print('Número inválido! Tente novamente.')
        num_validos = False

    operacao = input('Digite a operação (+, -, *, /): ')
    operadores_validos = ['+', '-', '*', '/']

    if operacao not in operadores_validos:
        print('Operação inválida! Tente novamente.')
        continue

    if len(operacao) > 1:
        print('Operação inválida! Tente novamente.')
        continue

    if operacao == '+':
        resultado = num1 + num2
        print(f'{num1} + {num2} = {resultado}')
    elif operacao == '-':
        resultado = num1 - num2
        print(f'{num1} - {num2} = {resultado}') 
    elif operacao == '*':
        resultado = num1 * num2
        print(f'{num1} * {num2} = {resultado}')
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f'{num1} / {num2} = {resultado}')
        else:
            print('Erro: Divisão por zero!')
            continue

    sair = input('Deseja sair? (s/n) ').lower().startswith('s')

    if sair is True:
        print('Saindo...')
        break