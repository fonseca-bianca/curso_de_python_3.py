from sys import path
# import aula99_package

print(*path, sep='\n')

print(__name__)


from aula99_package.modulo import soma
print(soma(1,2))

import aula99_package.modulo
print(aula99_package.modulo.soma(3,4))

from aula99_package import modulo
print(modulo.soma(5,6))



