frase = 'O rato roeu a roupa do rei de Roma'

qtd_apareceu_mais_vezes = 0
letra_mais_apareceu = ''

i = 0 
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_mais_apareceu = letra_atual

    print(letra_atual, qtd_atual)
    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_apareceu}" com {qtd_apareceu_mais_vezes} vezes') 