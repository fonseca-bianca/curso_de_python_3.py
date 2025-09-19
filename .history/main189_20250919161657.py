caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Atenção!\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )