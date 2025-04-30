"""Introdução ao for / in - estrutura repetição para coisas FINITAS"""

palavra = "Python"

nova_palavra = ""
for letra in palavra:
    nova_palavra += f'*{letra}'
    print(letra)
print(nova_palavra + '*') # inclui asterisco ao final da palavra
    
# 'letra' é a variável criada para fazer a iteração. Esta irá 
# ocorrer na palavra 'Python'
    
    
# Código semelhante, mas com uso do 'while'
# fica mais longo e mais confuso quando é para repetições de coisas Finitas

# o código abaixo vai solicitar a senha infinitas vzs até que o usuário 
# digite ela corretamente conforme a senha que ele salvou

# Cód:
senha_salva = "123456"
senha_digitada = ""
# OBS.: se colocar um espaço em branco na 'senha_digitada', então ela já 
# terá um caractere, o espaço (" "), o que a torna diferente de '123456', 
# pq daí a senha correta seria: ' 123456'
repeticoes_senha = 0
limite_repeticoes = 5

while senha_salva != senha_digitada and repeticoes_senha < limite_repeticoes:
    senha_digitada = input(f'Sua senha ({repeticoes_senha + 1}x): ')
    
    repeticoes_senha += 1
    
if senha_digitada == senha_salva:
    print(f"A {senha_digitada} está correta")
else:
    print("Número de tentativas excedido, Aguarde 2h para tentar novamente.")
    
print(repeticoes_senha)
print('Aquele laço acima pode ter repetições infinitas')