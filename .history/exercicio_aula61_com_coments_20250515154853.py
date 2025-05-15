"""
EXERCÍCIO: ALGORITMO DO CPF

Calculo dos dígitos do CPF (após traço) (70, só o 7, no caso):
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,multiplicando cada um dos valores por uma contagem 
regressiva começando de 10
1º: iniciar contagem regressiva em 10. 10 corresponde ao 1º número do CPF
2º: os 9 primeiros dígitos do CPF serão colocados abaixo da contagem regressiva
com os números respectivos (ex.: 746 = 10 9 8) 
3º: multiplicando cada dígito do CPF pelo número da contagem regressiva 
respectivamente 

_______________________________________________________________________________
**Cálculo do primeiro dígito do CPF (após traço)**
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por umacontagem regressiva começando de 11

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

Retorno:
O primeiro dígito do CPF é 7
"""

import re
import sys

cpf = input(
    "Digite o seu CPF: "\
    .replace(".", "")\
    .replace("-", "")\
    .replace("/", "")\
    .replace("_", "")\
    .replace(" ", "")
    )
    # .replace("o que se quer substituir", "pelo o que se quer substituir")
    # no caso acima, não queremos substituir por nada específico, por isso 
    # uma string vazia
    
# essa é a forma mais longa e menos usual    
# cpf = "746.824.890-70"\
#     .replace(".", "")\
#     .replace("-", "")\
#     .replace("/", "")\
#     .replace("_", "")\
#     .replace(" ", "")
    
# essa é a forma mais completa, apenas exige a importação da biblioteca re 
# (regular expressions)   
# pode colocar letras e qlqr coisa dentro ("746.824.890aaaaaaaabbbb-70"), 
# pq ele restringe o que ele NÃO quer
cpf = re.sub(
    r'[^0-9]', # tudo o que NÃO for número digitado pelo usuário qndo inserir 
    # o CPF
    "", # irá substituir por nada (o número vai ficar um só)
    "746.824.890-70"
)
print(cpf)

cpf_eh_sequencial = cpf == cpf[0] * len(cpf) # isso é uma flag

if cpf_eh_sequencial:
    print("Você enviou dados sequenciais.")
    sys.exit() # tem q importar biblioteca 'sys'. No caso, se estiver 
    # correto o q o usuário enviar, aq o cód já acaba
    
soma_nove_digitos = cpf[:9] #fatiamento do índice zero ao 9, sendo q o 9 NÃO 
# é incluído
contagem_regressiva_1 = 10

resultado_digito_1 = 0
for digito_1 in soma_nove_digitos:
    multiplicacao_digitos = int(digito_1) * contagem_regressiva_1 # int: 
    # converte a string pra inteiro
    print(digito_1, contagem_regressiva_1, multiplicacao_digitos) # aq vai 
    # mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    resultado_digito_1 += multiplicacao_digitos
    contagem_regressiva_1 -= 1 # mostra a contagem regressiva

print(f"A soma de todos os números multiplicados é: {resultado_digito_1}")

obter_digito_1 = ((resultado_digito_1 * 10) % 11)
obter_digito_1 = obter_digito_1 if obter_digito_1 <= 9 else 0 # ternário
print(obter_digito_1)

    
"""
_______________________________________________________________________________
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

Retorno: 
O segundo dígito do CPF é 0
"""
print("----------------------------------------------------------------")
cpf = "74682489070"
soma_dez_digitos = cpf[:10] # fatiamento do índice zero ao 10, sendo q o 10 
# NÃO é incluído
contagem_regressiva_2 = 11 # os 10 primeiros dígitos são multiplicados pela 
# seq regressiva começando em 11 

resultado_digito_2 = 0 # irá armazenar o somatório das multiplicações

# loop 'for' irá percorrer cada um dos 10 primeiros dígitos armazenados na 
# variável 'soma_dez_digitos'
for digito_2 in soma_dez_digitos:
    multiplicacao_digitos = int(digito_2) * contagem_regressiva_2 # int: 
    # converte a string pra inteiro
    print(digito_2, contagem_regressiva_2, multiplicacao_digitos) # aq vai 
    # mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    resultado_digito_2 += multiplicacao_digitos # 'resultado_digito_2': 
    # a soma dos resultados das multiplicações é colocado aq
    contagem_regressiva_2 -= 1 # mostra a contagem regressiva (decremento)

print(f"A soma de todos os números multiplicados é: {resultado_digito_2}")

# 'obter_digito_2': calcula o último dígito do CPF (o 2º verificador)
obter_digito_2 = ((resultado_digito_2 * 11) % 11) 
# 1º: multiplica valor soma total de 'resultado_digito_2' por 11. 
# 2º: o resto da divisão do valor por 11 é calculado usando '%'. O resto será 
# o valor provisório do 2º verificador

obter_digito_2 = obter_digito_2 if obter_digito_2 <= 9 else 0 # ternário
# ternário: se o valor de 'obter_digito_2' for MAIOR q 9, será ajustado pra 0
print(obter_digito_2)

print("----------------------------------------------------------------")

# Validação do CPF
cpf_completo = f"{soma_nove_digitos}{obter_digito_1}{obter_digito_2}" # 9 
# dígitos + dígito 1 + dígito 2 (após o traço) total = 11 dígitos + dígitos CPF
print(f"O CPF completo é: {cpf_completo}")

if cpf == cpf_completo:
    print(f"O CPF {cpf} enviado pelo cliente é válido.")
else:
    print(f"O CPF {cpf} enviado pelo cliente é inválido.")