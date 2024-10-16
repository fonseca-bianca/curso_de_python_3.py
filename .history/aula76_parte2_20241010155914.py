"""
Manipulação de keys e values em dict
"""

pessoa = {}

# linhas de cód
# ...

# Atribuição de valor a uma chave: na key 'nome' insira 'Luiz Gustavo' como value
pessoa['nome'] = 'Luiz Gustavo' 
print(pessoa)

# print(pessoa['nome1']) --> KeyError: 'nome1' --> essa chave NÃO existe no dict

# Criação de Chave Dinâmica:

chave = "nome_completo"

pessoa[chave] = "Agatha Christie"
lista = ["Obras mais conhecidas: ", 
    "Murder on the Orient Express;",
    "Death on the Nile;",
    "Crooked House;",
    "A Murder Is Announced."
]

print(pessoa[chave])

for obra in lista:
    print(obra)
