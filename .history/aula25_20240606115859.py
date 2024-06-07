#Interpolação básica de strings

nome = "Bianca"
salario = 3200.00
variavel = "%s, o seu salário aqui na empresa será de R$%.2f" % (nome, salario)
print(variavel)

print("O hexadecimal de %d é %08x" % (15, 15))
#08: vai preencher com ZEROS onde não tem números. 8 casas (0000000f)
#x: hexadecimal | X: HEXADECIMAL