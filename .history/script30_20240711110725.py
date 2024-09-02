import os
import errno

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido")
except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio")
    else:
        print("Erro inesperado")
    print("Descrição erro:", erro)

print("Programa encerrado")