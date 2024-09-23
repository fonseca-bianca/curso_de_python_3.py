"""
Criando um gerador de CPF com o algoritmo criado no exercício da aula 61
"""

import random # pra coisas aleatórias
import sys
# randint (número aleatório inteiro): está DENTRO do Random

# print(random.randint(0, 9)) # queremos número aleatório entre 0 e 9


for _ in range(10): # vamos gerar 10 números de CPF aleatórios
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0 , 9)) # tem q converter o int pra string

    # print(nove_digitos) 
    # sys.exit()

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)