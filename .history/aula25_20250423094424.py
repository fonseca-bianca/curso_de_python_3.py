""" Interpolação básica de strings:
- se 3 valores forem colocados na Tupla, então a string vai esperar q 3 
- valores sejam passados
- s: string
- d ou i: inteiro (decimal)
- f: float (ponto flutuante)
- x: hexadecimal (letras minúsculas) (ABCDEF0123456789)
- X: hexadecimal (letras maiúsculas)
- %: formatação de strings
"""

nome = "Bianca" # %s = string --> 1º valor da Tupla
cargo = "Dev Python" # %s = string --> 3º valor da Tupla
salario = 3200.005215 # %.2f = float --> 2º valor da Tupla
variavel = (
    "%s, o seu salário aqui na empresa será de R$%.2f "
    "e o seu cargo será %s" % (nome, salario, cargo) # tupla de valores
)
print(variavel)
print(" ")
print("O hexadecimal de %d é %08x" % (15, 15)) # tupla de valores
# 08: vai preencher com ZEROS onde não tem números. 8 casas (0000000f)
# (15, 15): 1º 15 é referente ao valor decimal e o 2º é o valor hexadecimal



""" Tupla de valores:
%: conecta a string com os valores passados
%s, %d, %.2f: formatação dos valores (placeholders)
OBS.: 
- quando houver apenas 1 valor, NÃO é necessário colocar os parênteses,
  poderia colocar somente o nome da variável
"""