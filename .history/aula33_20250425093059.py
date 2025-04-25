"""
Tipos Embutidos:
em Python, quando uma variável é do tipo IMUTÁVEL, 
é possível criar outra variável para atribuir NOVO valor, MAS NÃO pode 
atribuir outro valor a ela
"""

# string[:3]} ABC {string[4:]--> :3 inicia no índice 3 | 4:  do índice 4 até 
# o final
# NÃO daria pra fazer: string[0] = "E" porque a string é Imutável
string = "bruna Fonseca" 

# criação variável 'outra_string' com interpolação de strings (f-string)
# string[:3]: pega os 3 primeiros caracteres da string, ou seja, "bru"
# 123 é uma sequência de caracteres adc diretamente
# string[:4]: pega a partir do 5º caractere e vai até o final da string 
# original, ou seja, "a Fonseca"

outra_string = f'{string[:3]}123{string[4:]}'
print(string.zfill(20)) 

print(outra_string)
print(string.capitalize()) 

print(string.title())

