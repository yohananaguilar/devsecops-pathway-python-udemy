"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um código não tem fim
"""
contador = 0

while contador < 10:
    print(contador)
    contador += 1

    if contador == 6:
        print('Cheguei no 6')
        continue

    if contador == 8:
        print('Estou no 8, vou sair')
        break

print('Acabou o loop')
