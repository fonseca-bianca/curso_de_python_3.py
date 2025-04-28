nome = "Ana Maria da Silva"
indice = 0
tamanho_nome = len(nome)
novo_nome = ""

while tamanho_nome < 30:
    nome = novo_nome + nome + novo_nome # ******Ana Maria da Silva******
    tamanho_nome = len(nome) 
    novo_nome += "*"

nome_intercalado = ""
for indice in nome: # ******Ana Maria da Silva******
    nome_intercalado += f"*{indice}"
    
print(nome) # output: nome com asteriscos ******Ana Maria da Silva******
print(nome_intercalado.strip("*")) # output: remove asteriscos antes e 
    # depois do nome A*n*a* *M*a*r*i*a* *d*a* *S*i*l*v*a


