nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = "*"

while tamanho_nome <= 30:
    nome += novo_nome
    tamanho_nome = len(nome)
    
print(novo_nome[:1])
print(nome[5])