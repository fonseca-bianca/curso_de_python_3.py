nome = "Ana Maria da Silva"

indice = 0
tamanho_nome = len(nome)
novo_nome = "*"

while tamanho_nome <= 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1


    
print(nome)
print(novo_nome)
