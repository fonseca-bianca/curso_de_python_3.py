nome = "Ana Maria da Silva"

# Gera o novo nome com asteriscos
novo_nome = ""
for letra in nome:
    novo_nome += f"*{letra}"

# Adiciona asteriscos no início e no final do nome
nome = novo_nome + "*" * (20 - len(novo_nome))  # 20 asteriscos no total

print(nome)
print(novo_nome)
