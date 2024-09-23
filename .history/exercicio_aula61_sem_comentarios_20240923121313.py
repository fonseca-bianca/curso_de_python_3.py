"""
Calculo dos dígitos após o traço/a barra do CPF:

Coletar a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO após o traço,
multiplicando cada um dos valores por uma contagem regressiva começando de 10
1º: iniciar contagem regressiva em 10. 10 corresponde ao 1º número do CPF
2º: os 9 primeiros dígitos do CPF serão colocados abaixo da contagem regressiva
com os números respectivos (ex.: 746 = 10 9 8) 
3º: multiplicando cada dígito do CPF pelo número da contagem regressiva respectivamente 

________________________________________________________________________________________
**Cálculo do primeiro dígito do CPF (após o traço)**

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores
por uma contagem regressiva começando de 10.

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
Multiplicar o resultado anterior por 10
Obter o resto da divisão da conta anterior por 11
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
--> Mesma lógica pra usar no 2º dígito após o traço
"""

cpf = input("Insira o número do seu CPF (não isenrir símbolos): ")
soma_nove_digitos = cpf[:9] 
contagem_regressiva_1 = 10

resultado_digito_1 = 0
for digito_1 in soma_nove_digitos:
    multiplicacao_digitos = int(digito_1) * contagem_regressiva_1 
    print(digito_1, contagem_regressiva_1, multiplicacao_digitos)  
    resultado_digito_1 += multiplicacao_digitos
    contagem_regressiva_1 -= 1 

print(f"A soma de todos os números multiplicados é: {resultado_digito_1}")

obter_digito_1 = ((resultado_digito_1 * 10) % 11)
obter_digito_1 = obter_digito_1 if obter_digito_1 <= 9 else 0 
print(obter_digito_1)
    
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
print("----------------------------------------------------------------") 
soma_dez_digitos = cpf[:10] 
contagem_regressiva_2 = 11 

resultado_digito_2 = 0 


for digito_2 in soma_dez_digitos:
    multiplicacao_digitos = int(digito_2) * contagem_regressiva_2 
    print(digito_2, contagem_regressiva_2, multiplicacao_digitos) 
    resultado_digito_2 += multiplicacao_digitos 
    contagem_regressiva_2 -= 1 

print(f"A soma de todos os números multiplicados é: {resultado_digito_2}")

obter_digito_2 = ((resultado_digito_2 * 11) % 11) 

obter_digito_2 = obter_digito_2 if obter_digito_2 <= 9 else 0 

print(obter_digito_2)

print("----------------------------------------------------------------")

# Validação do CPF
cpf_completo = f"{soma_nove_digitos}{obter_digito_1}{obter_digito_2}" 
print(f"O CPF completo é: {cpf_completo}")

if cpf == cpf_completo:
    print(f"O CPF {cpf} enviado pelo cliente é válido.")
else:
    print(f"O CPF {cpf} enviado pelo cliente é inválido.")