"""
... continuação sobre List Comprehensions ...

Mapeamento de Dados em List Comprehensions:

"""
# print(list(range(10)))

print("A mesma coisa, mas usando lógica com 'for':")
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

print()

print("A mesma coisa, mas usando List Comprehension: ")
lista = [numero for numero in range(10)]
print(lista)
# A sintaxe é: [expressão for item in iterável]
    # expressão: o que você quer colocar na lista (no caso, é a variável)
    # item: o nome do item atual do iterável
    # iterável: a lista, tupla, string, etc. que você está percorrendo

print()
 
print("Multiplicando cada nº de List Comprehension por 2:")
# pode ser escrito assim, com quebra de linha pra melhor visualização:
lista = [
    numero * 2 
    for numero in range(10)
]
print(lista)


# Mapeamento de Dados em List Comprehensions:
produtos = [
    {'nome': 'Produto 1', 'preco': 10.0},
    {'nome': 'Produto 2', 'preco': 20.0},
    {'nome': 'Produto 3', 'preco': 30.0},
]

