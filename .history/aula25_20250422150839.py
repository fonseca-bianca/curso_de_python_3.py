# Interpolação básica de strings

# se 3 valores forem colocados na Tupla, então a string vai esperar q 3 
# valores sejam passados

nome = "Bianca"
cargo = "Dev Python"
salario = 3200.00
variavel = (
    "%s, o seu salário aqui na empresa será de R$%.2f "
    "e o seu cargo será %s" % (nome, salario, cargo)
)
print(variavel)
print(" ")
print("O hexadecimal de %d é %08x" % (15, 15))
# 08: vai preencher com ZEROS onde não tem números. 8 casas (0000000f)
# x: hexadecimal | X: HEXADECIMAL
