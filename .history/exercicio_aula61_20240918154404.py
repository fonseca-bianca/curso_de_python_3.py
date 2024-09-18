"""
Calculo do primeiro dígito do CPF (70, só o 7, no caso):
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
1º: iniciar contagem regressiva em 10. 10 corresponde ao 1º número do CPF
2º: os 9 primeiros dígitos do CPF serão colocados abaixo da contagem regressiva
com os números respectivos (ex.: 746 = 10 9 8) 
3º: multiplicando cada dígito do CPF pelo número da contagem regressiva respectivamente 

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2  # aq está a contagem regressiva
*  7   4  6  8  2  4  8  9  0  7  # 7 é o PRIMEIRO dígito do CPF
   70 36 48 56 12 20 32 27 0  14  #

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "74682489070"
