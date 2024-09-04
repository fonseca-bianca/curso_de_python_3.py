nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = ""
indice = 0

while tamanho_nome <= 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    novo_nome += "*"

    while indice < len(nome):
        letra = nome[indice]
        novo_nome += f"*{letra}"
        indice += 1
   
        
print(nome)
print(novo_nome)


