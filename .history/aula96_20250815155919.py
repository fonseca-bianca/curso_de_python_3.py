# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# 
# print("-------------------------------------------------------------")
# Importando o módulo inteiro:
#   import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

import sys

platform = 'A MINHA'
print(sys.platform) # win32
print(platform) # A MINHA
# sobrescreveu o nome platform com a string 'A MINHA', não poderia mais 
# acessar o módulo platform 'platform.system()' sem antes mudar o nome da 
# variável 

# print("-------------------------------------------------------------")
# Importando partes do módulo:
#   from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform
# print(platform)

# print("-------------------------------------------------------------")
# Importando o módulo com alias (apelido do módulo 'as'):
#   import nome_modulo as apelido

# import sys as s
# 
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# print("-------------------------------------------------------------")
# Importando o módulo com alias (apelido do módulo 'as'):
#   from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
# 
# from sys import exit as ex
# from sys import platform as pf
# print(pf)

# print("-------------------------------------------------------------")
# OBS.: MÁ PRÁTICA:
#   from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
 
# from sys import exit, platform
# 
# print(platform)
# exit()