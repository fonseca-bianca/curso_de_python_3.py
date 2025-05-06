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
# OBS.:
    Cuidar pra incluir ou excluir itens de uma lista, pq isso requer processa-
    mento do Python, então, pensando em listas grandes, o ideal é sempre 
    tentar mover o último item da lista, pq daí o Python só vai precisar mexer
    no item anterior ao último
"""

# type: mostra o tipo de valores
string = "abc" # seus índices poderiam ser percorridos pela função (len())

#               0     1        2        3    4 --> itens 
minha_lista = [123, True, "Ana Maria", 1.2, []] 

print(minha_lista[2].upper(), type(minha_lista[2]))
minha_lista[2] = "Rhaenyra Targaryen" # altera o índice na própria lista, 
# nem aparece a string anterior, já aparece alterada no print seguinte
print(minha_lista)

print(bool(minha_lista)) # falsy: quando lista está vazia ela é SEMPRE false
# print(minha_lista, type(minha_lista))

print(minha_lista, "Removido o item", minha_lista.pop())

# removendo um item específico da lista:
minha_lista.__delitem__(1)
print(minha_lista, "Removido o item de índice 2") # no caso, o True

# o .__delitem__(1) no print apresenta um retorno diferente:
print(minha_lista, "Removido o item de índice 2", minha_lista.__delitem__(1))

print("----------------------------")

minha_lista.append(200)
print(minha_lista, "Adicionado o item", 200)

# o .append no print apresenta um retorno diferente:
print(minha_lista, "Adicionado o item", minha_lista.append(200)) 
# output: [123, True, 'Rhaenyra Targaryen', 1.2, 200] Adicionado o item None
# None: o retorno de .append() no print() é None --> comportamento padrão