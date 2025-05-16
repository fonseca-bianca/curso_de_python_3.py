"""
Criando um gerador de CPF com o algoritmo criado no exercício da aula 61
"""

import random # pra coisas aleatórias
# import sys
# randint (número aleatório inteiro): está DENTRO do Random

# print(random.randint(0, 9)) # queremos número aleatório entre 0 e 9


# 'for' de fora vai gerar 10 CPFs
# 'for' de dentro vai gerar 9 dígitos aleatórios de cada um dos 10 CPFs
for _ in range(10): # vamos gerar 10 CPFs de números aleatórios
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0 , 9)) # tem q converter o int 
        # pra string

    # print(nove_digitos) 
    # sys.exit()

    contador_regressivo_digito_10 = 10

    resultado_digito_10 = 0
    for digito in nove_digitos:
        resultado_digito_10 += int(digito) * contador_regressivo_digito_10
        contador_regressivo_digito_10 -= 1
    digito_10 = (resultado_digito_10 * 10) % 11
    digito_10 = digito_10 if digito_10 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_10)
    contador_regressivo_digito_11 = 11

    resultado_digito_11 = 0
    for digito in dez_digitos:
        resultado_digito_11 += int(digito) * contador_regressivo_digito_11
        contador_regressivo_digito_11 -= 1
    digito_11 = (resultado_digito_11 * 10) % 11
    digito_11 = digito_11 if digito_11 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_10}{digito_11}'

    print(cpf_gerado_pelo_calculo)