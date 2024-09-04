nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome < 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    novo_nome += "*"

print(nome)

nome_intercalado = ""
for letra in nome:
    nome_intercalado += f"*{letra}"
    
nome_intercalado += "*"
print(nome_intercalado)


