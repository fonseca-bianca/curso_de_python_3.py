"""
Tipos Embutidos:
em Python, quando uma variável é do tipo IMUTÁVEL, 
é possível criar outra variável para atribuir NOVO valor, MAS NÃO pode atribuir
outro valor a ela
"""

#string[:3]} ABC {string[4:]--> :3 inicia no índice 3 | 4:  do índice 4 até o final
string = "Bianca Fonseca"
outra_string = f'{string[:3]}123{string[4:]}'
print(string)
print(outra_string)