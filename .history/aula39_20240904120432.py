nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome <= 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)


novo_nome = ""
for letra in nome:
    novo_nome += f"*{letra}"

nome = novo_nome + "*" * (len(novo_nome))  

print(nome)
print(novo_nome)
