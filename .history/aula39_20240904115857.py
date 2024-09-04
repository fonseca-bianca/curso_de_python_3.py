nome = "Ana Maria da Silva"
tamanho_desejado = 30  # Número de asteriscos desejado em cada lado do nome

# Inicializa o novo_nome com os asteriscos iniciais
novo_nome = "*" * (tamanho_desejado // 2)

# Constrói o novo nome adicionando asteriscos entre cada caractere
for caractere in nome:
    novo_nome += caractere + "*"

# Adiciona os asteriscos finais
novo_nome += "*" * (tamanho_desejado - len(novo_nome))

print(novo_nome)
