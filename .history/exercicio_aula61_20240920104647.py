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
"""

cpf = "74682489070"
soma_dez_digitos = cpf[:9] #fatiamento do índice zero ao 9, sendo q o 9 NÃO é incluído
contagem_regressiva_2 = 10

resultado_digito_2 = 0
for digito_2 in soma_dez_digitos:
    multiplicacao_digitos = int(digito_2) * contagem_regressiva_2 # int: converte a string pra inteiro
    print(digito_2, contagem_regressiva_2, multiplicacao_digitos) # aq vai mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    resultado_digito_2 += multiplicacao_digitos
    contagem_regressiva_2 -= 1 # mostra a contagem regressiva

print(f"A soma de todos os números multiplicados é: {resultado_digito_2}")


obter_digito_2 = ((resultado_digito_2 * 10) % 11)
obter_digito_2 = obter_digito_2 if obter_digito_2 <= 9 else 0 # ternário
print(obter_digito_2)

    
"""
_______________________________________________________________________________________
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
soma_dez_digitos = cpf[:10] #fatiamento do índice zero ao 10, sendo q o 10 NÃO é incluído
contagem_regressiva_2 = 11

resultado_digito_2 = 0
for digito_2 in soma_dez_digitos:
    multiplicacao_digitos = int(digito_2) * contagem_regressiva_2 # int: converte a string pra inteiro
    print(digito_2, contagem_regressiva_2, multiplicacao_digitos) # aq vai mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    resultado_digito_2 += multiplicacao_digitos
    contagem_regressiva_2 -= 1 # mostra a contagem regressiva

print(f"A soma de todos os números multiplicados é: {resultado_digito_2}")


obter_digito_2 = ((resultado_digito_2 * 10) % 11)
obter_digito_2 = obter_digito_2 if obter_digito_2 <= 9 else 0 # ternário
print(obter_digito_2)