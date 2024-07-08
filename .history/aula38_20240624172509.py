qnt_linhas = 5
qnt_colunas = 5

#linha = 1
linha = 0
while linha <= qnt_linhas:
    linha = 1
    coluna = 1
    while coluna <= qnt_colunas:
        print(f"{linha=} {coluna=}") #OU (linha, coluna) OU (f"linha, coluna"): apareceria no console assim: linha, coluna 25x
        coluna += 1
    linha += 1
    break
print("Acabou")

"""
linha = 1
FORA DO LOOP WHILE (primeiro):
- inicializado somente 1x permanecendo o valor de 'linha' constante durante todo o código
- enquanto valor de linha constante, o valor de coluna é incrementado a cada linha
DENTRO DO LOOP WHILE (primeiro): 
- linha inicializada a cada iteração
- todas as linhas terão a mesma sequência de colunas (1,2,3,..., qnt_colunas)
"""