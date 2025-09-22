"""
Manipulação de Arquivos em Python:
Criando arquivos com Python + Context Manager with
Usamos a função open() pra abrir um arquivo em Python (ele pode ou não existir)
    Modos:
        -> r (leitura), w (escrita), x (para criação)
        -> a (escreve ao final), b (binário)
        -> t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)
    Métodos úteis:
    ->   write, read (escrever e ler)
    ->   writelines (escrever várias linhas):
            ex.:
                arquivo.writelines(
                    ['Linha 1\n', 'Linha 2\n']
                )
    ->   seek (move o cursor):
            ex.:
                arquivo.seek(0,0) -> início do arquivo
    ->   readline (ler linha):
            lê linha por linha, como se fosse o next()
    ->   readlines (ler linhas)
    ->   close (fecha o arquivo)
    
    OBS.:
        w+ : escrita + leitura
        r+ : leitura + escrita
        a+ : escrita no final do arquivo + leitura
            é o append mode:
                útil pra arqs de log, q são extensos e não queremos perder dados
        
    
Vamos falar mais sobre o módulo os, mas:
    os.remove ou unlink - apaga o arquivo
    os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
    json.dump = Gera um arquivo json
    json.load = Lê um arquivo json
"""

# Criando um arquivo .txt na pasta (raiz) do projeto
caminho_arquivo = 'aula116.txt' 

# desta forma, é necessário colocar o close():
# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# usando o 'with', não é necessário colocar o close():

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo observações')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # remove a quebra de linha extra
    print(arquivo.readline().strip()) # remove espaços em branco
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

    
# no Python, \ (barra invertida) é um caractere de escape, portanto, qndo 
# for trabalhar com caminhos de arquivos, use \\ (duas barras invertidas)
# ou r'C:\Users\... (coloque o r antes da string)
# 
# ex.:
# caminho_arq = "C:\\Users\\fonse\\Desktop\\dev_bianca\\udemy\\python_completo"
# caminho_arq += "aula116.txt"
# print(caminho_arq)
# output: C:\Users\fonse\Desktop\dev_bianca\udemy\python_completo\aula116.txt


