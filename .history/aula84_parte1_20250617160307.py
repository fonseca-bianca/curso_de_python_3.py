"""
Introdução à List Comprehensions:
É uma forma rápida pra criar listas a partir de iteráveis 
(listas, tuplas, strings, etc.) usando uma sintaxe compacta e legível.
O Python faz por debaixo dos panos e, muitas vezes, pode ficar "obscuro"
na leitura, mas é uma forma eficiente de gerar listas

"""

# Usaremos a lista do print abaixo como base pra expandir pro conceito
# de List Comprehension:

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
    # item: o nome do item atual do iterável (no caso, o numero)
    # iterável: a lista, tupla, string, etc. que você está percorrendo 
    #   (no caso, range(10))

print()
 
print("Multiplicando cada nº de List Comprehension por 2:")
# pode ser escrito assim, com quebra de linha pra melhor visualização:
lista = [
    numero * 2 
    for numero in range(10)
]
print(lista)
