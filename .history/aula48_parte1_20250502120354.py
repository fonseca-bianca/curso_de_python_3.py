"""Introdução às Listas Mutáveis em Python
Tipo: list (é mutável)
suporta muitos tipos de valores
índices e fatiamento (reutilização de cód) 
Métodos: 
.append(): adc item ao final da lista
.insert(): adc item no índice escolhido
-- tem q passar na ordem:
    (índice, qual o valor quer inserir)
.pop(): remove item ao final ou no índice escolhido da lista
.del(): apaga item no índice escolhido
.clear(): limpa a lista
.extend(): estende a lista
+: concatena as listas
CRUD (Creat, Read, Update, Delete) = minha_lista[i]
"""

# type: mostra o tipo de valores
string = "abc" # seus índices poderiam ser percorridos pela função (len())
minha_lista = [123, True, "Ana Maria", 1.2, []] # é o mesmo que uma string vazia ""

print(minha_lista[2].upper(), type(minha_lista[2]))
minha_lista[2] = "Rhaenyra Targaryen" # altera o índice na própria lista, nem aparece a string anterior, já aparece alterada 
print(minha_lista)

# print(bool(minha_lista)) # falsy: quando uma lista está vazia ela é SEMPRE false
# print(minha_lista, type(minha_lista))