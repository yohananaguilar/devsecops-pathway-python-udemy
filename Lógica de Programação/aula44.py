for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, saindo...')
        break

    for j in range(1, 3):
        print(f'i: {i}, j: {j}')

else:
    print('O loop for foi finalizado sem o break.')