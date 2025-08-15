"""
Recarregando módulos:
    importlib:
        importa biblioteca
    singleton:
        só pode existir 1 instância no programa inteiro
        
OBS.:
    só irá ocorrer o recarregamento do módulo se o dev assim desejar e fizer
o comando pro código
"""

import importlib
import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # reload: recarrega o código inteiro do módulo
    print(i)
    
print('Fim')
