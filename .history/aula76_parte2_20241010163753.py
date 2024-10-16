"""
Manipulação de keys e values em dict
"""

person = {}

# linhas de cód
# ...

# Atribuição de valor a uma chave: na key 'nome' insira 'Luiz Gustavo' como value
person['nome'] = 'Luiz Gustavo' 
print(person)

# print(pessoa['nome1']) --> KeyError: 'nome1' --> essa chave NÃO existe no dict

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

print(person[key])

for literary_work in list_literary_work:
    print(literary_work)

person[key] = "R. R. Martin"
print(person)