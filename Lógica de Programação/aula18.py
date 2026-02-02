# Operadores Lógicos and(e) or(ou) not(não)
# And -> Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy: 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input("Digite 'E' para entrar ou 'S' para sair: ")
senha_digitada = input("Digite a senha: ")

senha_permitida = "123456"

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Você entrou no sistema")
else:
    print("Você saiu do sistema")