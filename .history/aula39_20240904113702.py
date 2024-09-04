nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = "*"

while tamanho_nome <= 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)

nome_intercalado = "*"
for letra in nome.strip("*"):
    nome_intercalado += f"{letra}*"

# Remove o último asterisco adicionado ao final e mantém um asterisco no início e no final
nome_intercalado = nome_intercalado.rstrip("*")
nome_intercalado = f"*{nome_intercalado}*"

    
print(nome)
print(nome_intercalado)
