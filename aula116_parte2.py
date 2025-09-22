"""
os.remove() - Remove um arquivo do sistema
os.unlink() - Remove um arquivo do sistema (funciona da mesma forma que o remove)
os.rename() - Renomeia um arquivo
    * OBS.: qndo renomeamos um arq, esse arq tbm é movido, pois o caminho
            do arq faz parte do nome do arq e ele é alterado
"""

# chama o módulo 'os' no topo do arquivo e depois chama ele onde quiser no 
# cód

import os

os.remove('arquivo_teste.txt')  # remove o arq 'arquivo_teste.txt'
# os.unlink('arquivo_teste.txt')  # remove o arquivo (funciona da mesma forma 
# q o .remove)
# os.rename('arquivo_teste.txt', 'novo_nome.txt')  # renomeia o arq