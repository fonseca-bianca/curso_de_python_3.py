nome = "Ana Maria da Silva"

tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome < 30:
    nome = novo_nome + nome + novo_nome
    tamanho_nome = len(nome)
    novo_nome += "*"

nome_intercalado = ""
for letra in nome:
    nome_intercalado += f"*{letra}"

    
print(nome)
print(nome_intercalado.strip("*")) #remove asteriscos antes e depois do nome


