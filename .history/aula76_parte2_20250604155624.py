"""
Manipulação de keys e values em dict
"""

person = {} # dict

# linhas de cód
# ...

# Atribuição de valor a uma chave: na key 'nome' insira 'Luiz Gustavo' como 
# value
person['nome'] = 'Luiz Gustavo' 
print(person)

person['sobrenome'] = "Miranda"
# print(pessoa['nome1']) --> KeyError: 'nome1' --> essa chave NÃO existe no 
# dict

print()

# Criação de Chave Dinâmica:

key = "nome_completo"

person[key] = "Agatha Christie"
list_literary_work = ["Obras mais conhecidas: ", 
    "Murder on the Orient Express;",
    "Death on the Nile;",
    "Crooked House;",
    "A Murder Is Announced."
]

print(person) 
# mostra o dicionário completo com Agatha Christie ANTES 
# de ter sido sobrescrita por R. R. Martin
print(person[key])

for literary_work in list_literary_work:
    print(literary_work)

person[key] = "R. R. Martin"

del person['sobrenome'] # apaga a chave 'sobrenome'
print(person)

if person.get('sobrenome') is None: # qndo chave inexistente, o retorno 
    # padrão é 'NONE'
    print("Chave inexistente")
else:
    print(f"Sobrenome: {person['sobrenome']}")
    



"""
1) Por que não imprimiu 'Agatha Christie' como dicionário?
O valor "Agatha Christie" foi atribuído à chave "nome_completo", mas, 
em seguida, você substituiu esse valor com "R. R. Martin". Como o código 
continua
e imprime o dicionário completo apenas após a substituição, o valor 
"Agatha Christie" foi sobrescrito antes que o dicionário fosse impresso. 
Portanto, no final, o dicionário mostra apenas "R. R. Martin" para a chave 
"nome_completo".

2) Qual a diferença entre: print(person) e print(person[key])?
print(person): Imprime o dicionário inteiro. No seu exemplo, ele exibe todas as 
chaves e valores armazenados no dicionário person, como 
{'nome': 'Luiz Gustavo', 'nome_completo': 'R. R. Martin'}.
-------------------------------------------------------------------------------
print(person[key]): Imprime o valor associado à chave especificada (key). 
No exemplo, a chave "nome_completo" foi definida como "R. R. Martin", então 
o comando imprimirá "R. R. Martin". Se você quisesse imprimir 
"Agatha Christie", teria que fazer isso ANTES de sobrescrever o valor 
dessa chave.
"""