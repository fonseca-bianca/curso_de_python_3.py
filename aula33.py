"""
Tipos Embutidos:
em Python, quando uma variável é do tipo IMUTÁVEL, 
é possível criar outra variável para atribuir NOVO valor, MAS NÃO pode atribuir
outro valor a ela
"""

#string[:3]} ABC {string[4:]--> :3 inicia no índice 3 | 4:  do índice 4 até o final
string = "bianca Fonseca"
outra_string = f'{string[:3]}123{string[4:]}'
print(string)
print(outra_string)
print(string.capitalize()) 
#.capitalize(): esse método é específico da string. Vai transformar o primeiro caractere da string em MAIÚSCULO