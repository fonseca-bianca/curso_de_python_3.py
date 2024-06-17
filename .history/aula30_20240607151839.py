velocidade = 60 #velocidade atual do carro
quilometro = 100 #quilômetro da estrada onde está o carro, ex.: km 91 da BR-101

RADAR_1 = 60 #velocidade máx radar 1
LOCAL_1 = 100 # local onde o radar 1 está na estrada
RADAR_RANGE = 1 #a distância antes e depois do radar q ele pega o carro

#(LOCAL_1 - RADAR_RANGE): quilômetro 99
#(LOCAL_1 + RADAR_RANGE): quilômetro 101
if quilometro >= (LOCAL_1 - RADAR_RANGE) and quilometro <= (LOCAL_1 + RADAR_RANGE) \
    and velocidade > RADAR_1:
    print("Você está acima da velocidade máxima permitida. Carro multado em Radar 1")