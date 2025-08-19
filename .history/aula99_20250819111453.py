from sys import path

print(*path, sep='\n')

print(__name__)

from aula99_package.modulo import soma
print(soma(1,2))

