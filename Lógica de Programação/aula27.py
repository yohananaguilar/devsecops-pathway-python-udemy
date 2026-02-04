"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if(ruim) <- Contagem de complexidade(ruim)
"""

velocidade = 61  # km/h
local_carro = 100  # km

RADAR_1 = 60  # Velocidade máxima do radar 1
LOCAL_1 = 100  # Local onde o radar 1 está
RADAR_RANGE = 1  # A distância que o radar pega

vel_carr = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and vel_carr
if vel_carr:
    print('Velocidade do carro acima do limite permitido')

if carro_multado and vel_carr:
    print('Carro multado')