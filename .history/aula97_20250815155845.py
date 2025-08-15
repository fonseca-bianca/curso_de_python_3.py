# Entendendo os próprios módulos do Python:
#     - o 1º módulo executado chama-se __main__
#     podemos importar outro módulo inteiro ou parte do módulo
#     o Python conhece a pasta onde o __main__ está e as pastas q estão abaixo 
# dele
#     o Python NÃO reconhece as pastas e os módulos acima do __main__ por 
# default
#     o Python conhece TODOS os módulos e pacotes presentes nos caminhos de 
# sys.path

import sys

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')

print("----------------------------------------")
import aula97_m

print(aula97_m.variavel_modulo)