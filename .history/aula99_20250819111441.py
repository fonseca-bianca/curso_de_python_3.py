from sys import path

print(*path, sep='\n')

from aula99_package.modulo import soma
print(soma(1,2))

print(__name__)