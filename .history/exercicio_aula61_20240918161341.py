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

________________________________________________________________________________________
**Cálculo do primeiro dígito do CPF**
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7 (3010 / 11 = 273(inteiro) --> 273 * 11 = 3003 - 3010 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

________________________________________________________________________________________
**Cálculo do 2º dígito do CPF**
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2  # aq está a contagem regressiva
*  7   4  6  8  2  4  8  9  0  7  # 7 é o PRIMEIRO dígito do CPF
   77 40 54 64 14 20 40 36  0 14  # resutado de cada multiplicação

Somar todos os resultados: 
77+40+54+64+14+20+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0 (3630 / 11 = 330 (int)) --> 273 * 11 = 3630 --> 3630 - 3630 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = "74682489070"
soma_nove_digitos = cpf[:10] #fatiamento do índice zero ao 9, sendo q o 9 NÃO é incluído
contagem_regressiva = 11

multiplicacao_valores = 0
for digito in soma_nove_digitos:
    print(digito, contagem_regressiva) # aq vai mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    contagem_regressiva -= 1 # mostra a contagem regressiva
    
    multiplicacao_valores = digito * contagem_regressiva
print(multiplicacao_valores)

