"""
Operação ternária
if-else em uma linha
É condicional de uma única linha
<valor> if <condicao> else <outro_valor>
"""

condicao = 10 == 10 # não é usada depois, só pra teste
variavel_ternaria = "Valor" if True else "Outro valor"
print(variavel_ternaria)

valor_digitado = 1.5 # quando variável 'digito' for > 9 = 0 (retorne zero)
novo_valor_digitado = valor_digitado if valor_digitado <= 9 else 0
novo_valor_digitado = 0 if valor_digitado > 9 else valor_digitado
print(novo_valor_digitado)

"""
se digito for 11, vai imprimir 0
se digito for 9 ou menor, vai imprimir o próprio número digitado
"""