"""
Operação ternária
if-else em uma linha
É condicional de uma única linha
<valor> if <condicao> else <outro_valor>
"""

condicao = 10 == 10
variavel_ternaria = "Valor" if condicao else "Outro valor"

print(variavel_ternaria)

digito = 10 # quando variável 'digito' for > 9 = 0 (retorne zero)
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

"""
se digito for 11, vai imprimir 0
se digito for 9 ou menor, vai imprimir o próprio número digitado
"""