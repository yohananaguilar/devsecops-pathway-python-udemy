"""
Flag(Bandeira) Marcar um local
None = Não valor
is e is not = Operadores de identidade para verificar se duas variáveis referenciam o mesmo objeto na memória
id = identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else: 
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')