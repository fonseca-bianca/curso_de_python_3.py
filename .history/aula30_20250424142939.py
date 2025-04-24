"""
Constante:
- em Python, NÃO há esse conceito
- em razão disso, por convenção, usa-se letras MAIÚSCULAS para nomear 
  variáveis que NÃO devem ser alteradas:
    Ex.: PI, RADAR_1, LOCAL_1, etc.
        RADAR_1: velocidade máxima do radar 1
"""


velocidade = 60 # velocidade atual do carro
quilometro = 102 # quilômetro da estrada onde está o carro, ex.: km 91 da BR-101

RADAR_1 = 60 # velocidade máx radar 1
LOCAL_1 = 100 # local onde o radar 1 está na estrada
RADAR_RANGE = 1 # a distância antes e depois do radar q ele pega o carro

# EVITAR o trecho abaixo, pq o if e o else estão muito grandes = complexo:
# (LOCAL_1 - RADAR_RANGE): quilômetro 99
# (LOCAL_1 + RADAR_RANGE): quilômetro 101
# if quilometro >= (LOCAL_1 - RADAR_RANGE) and \
#     quilometro <= (LOCAL_1 + RADAR_RANGE) \ 
#     and velocidade > RADAR_1: --> \: quebra de linha
#     print("Você está acima da velocidade máxima permitida...
# else:
#     print("Você está na velocidade permitida")

# trecho acima reescrito:
velocidade_carro_multa = velocidade > RADAR_1
carro_passou_radar_1 = (
    quilometro > (LOCAL_1 - RADAR_RANGE) 
    and quilometro < (LOCAL_1 + RADAR_RANGE)
)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_multa

if velocidade_carro_multa:
    print("Carro acima da velocidade máxima.")
    
if carro_passou_radar_1:
    print("Carro passou pelo Radar 1.")
    
if carro_multado_radar_1:
    print("Carro multado no Radar 1")