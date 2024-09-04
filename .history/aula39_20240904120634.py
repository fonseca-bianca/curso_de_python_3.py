# nome = "Ana Maria da Silva"

# tamanho_nome = len(nome)
# novo_nome = ""

# while tamanho_nome <= 30:
#     nome = novo_nome + nome + novo_nome
#     tamanho_nome = len(nome)


# novo_nome = ""
# for letra in nome:
#     novo_nome += f"*{letra}"

# nome = novo_nome + "*" * (len(novo_nome))  

# print(nome)
# print(novo_nome)

nome = "Ana Maria da Silva"

# Adiciona asteriscos ao redor do nome até que o comprimento seja pelo menos 30
tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome < 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    novo_nome += "*"

# Corrige o nome para que ele tenha exatamente 30 caracteres
if tamanho_nome <= 30:
    nome = nome

# Gera o novo_nome com asteriscos entre as letras
novo_nome = ""
for letra in nome:
    novo_nome += f"*{letra}"

# Adiciona asteriscos no final do nome para atingir 30 caracteres
nome = novo_nome + "*" * (len(novo_nome))

print(nome)
print(novo_nome)
