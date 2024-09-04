nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = "Maria dos Santos"

while tamanho_nome <= 30:
    nome += novo_nome
    tamanho_nome = len(nome)
    
print(nome)
print(nome[5])