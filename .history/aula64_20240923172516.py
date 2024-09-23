"""
Criando um gerador de CPF com o algoritmo criado no exercício da aula 61
"""

cpf = "7468248907"
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

cpf_completo = f"{soma_nove_digitos}{obter_digito_1}{obter_digito_2}"
print(f"O CPF completo é: {cpf_completo}")

if cpf == cpf_completo:
    print(f"O CPF {cpf} enviado pelo cliente é válido.")
else:
    print(f"O CPF {cpf} enviado pelo cliente é inválido.")