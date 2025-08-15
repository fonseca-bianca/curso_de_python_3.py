# Entendendo os próprios módulos do Python:
#     - o 1º módulo executado chama-se __main__
#     podemos importar outro módulo inteiro ou parte do módulo
#     o Python conhece a pasta onde o __main__ está e as pastas q estão abaixo 
# dele
#     o Python NÃO reconhece as pastas e os módulos acima do __main__ por 
# default
#     o Python conhece TODOS os módulos e pacotes presentes nos caminhos de 
# sys.path
# OBS.:
#     se eu quisesse importar de fora, então eu deveria usar nome_modulo.path,
# isto é, se o módulo estiver em um caminho listado em sys.path, devemos 
# importar usando 'nome_modulo.path'
    

import sys

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')

print("----------------------------------------")
import aula97_m # importando o módulo criado onde está a var 'Luiz'
print(aula97_m.variavel_modulo)

from aula97_m import variavel_modulo # importando a variável do módulo
print(variavel_modulo)