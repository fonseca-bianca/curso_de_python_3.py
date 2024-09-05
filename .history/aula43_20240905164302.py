"""Introdução ao for / in - estrutura repetição para coisas FINITAS"""

texto = "Python"

for letra in texto:
    print(letra)
    
    
################################################################################
# Código semelhante, mas com uso do 'while'
# fica mais longo e mais confuso quando é para repetições de coisas Finitas

# o código abaixo vai solicitar a senha infinitas vzs até que o usuário digite ela 
# corretamente conforme a senha que ele salvou
# senha_salva = "123456"
# senha_digitada = " "
# repeticoes_senha = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes_senha}x): ')
    
#     repeticoes_senha += 1
    
# print(repeticoes_senha)
# print('Aquele laço acima pode ter repetições infinitas')