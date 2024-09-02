import pandas as pd
dados = [[1186,1751], [21328,25280], [947,18432], [29,280]]
linhas = ["Estadual", "Privada", "Municipal", "Federal"]
colunas = ["Número de alunos", "Número de professores"]
df = pd.DataFrame(dados, index=linhas, columns=colunas)
print(df)