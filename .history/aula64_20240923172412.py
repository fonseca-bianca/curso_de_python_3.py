"""
Criando um gerador de CPF com o algoritmo criado no exercício da aula 61
"""

cpf = "7468248907"
soma_nove_digitos = cpf[:9] #fatiamento do índice zero ao 9, sendo q o 9 NÃO é incluído
contagem_regressiva_1 = 10

resultado_digito_1 = 0
for digito_1 in soma_nove_digitos:
    multiplicacao_digitos = int(digito_1) * contagem_regressiva_1 # int: converte a string pra inteiro
    print(digito_1, contagem_regressiva_1, multiplicacao_digitos) # aq vai mostrar cada dígito do CPF e seu equivalente na contagem regressiva
    resultado_digito_1 += multiplicacao_digitos
    contagem_regressiva_1 -= 1 # mostra a contagem regressiva

print(f"A soma de todos os números multiplicados é: {resultado_digito_1}")

obter_digito_1 = ((resultado_digito_1 * 10) % 11)
obter_digito_1 = obter_digito_1 if obter_digito_1 <= 9 else 0 # ternário
print(obter_digito_1)
