nome = "Ana Maria da Silva"
indice = 0
tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome < 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    novo_nome += "*"

nome_intercalado = ""
for indice in nome:
    nome_intercalado += f"*{indice}"
    
print(nome)
print(nome_intercalado.strip("*"[0])) #remove asteriscos antes e depois do nome


