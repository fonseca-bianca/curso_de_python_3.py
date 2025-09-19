caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
    arquivo.write('Atenção!\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    
# output no arquivo aula116.txt:
# Aten��o!
# ficou desconfigurado por causa da Tabela ENCODE

# colocando o  encoding="utf-8":
# Atenção!
# imprime certinho com os acentos e caracteres especiais