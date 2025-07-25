"""
Métodos úteis dos dict em Python:
Shallow copy vs. Deep copy em dados mutáveis no Python
-> len: quantas chaves
    ao invés de passar o dunderline '__' para o método,
    pode usar a função 'len()' para obter o tamanho do dicionário
        Dunder:
            ex.:
                print(pessoa.__len__()) # 5
-> keys: iterável com chaves
-> values: iterável com valores
-> items: iterável com chaves E valores
-> setdefault: adc valor SE a chave NÃO existe
-> copy: retorna cópia rasa (shallow copy) do dict original
Copia valores IMUTÁVEIS.
Valores MUTÁVEIS: AMBOS os dicionários irão apontar pra MESMA lista na memória.
Cópia rasa significa q um NOVO dict é criado (chaves e valores dict original
são copiados pro NOVO dict).
Esses dicts NÃO compartilham endereços na memória, ambos são INDEPENDENTES.
copia os dados do dicionário, mas não o próprio dicionário ou seu endereço 
na memória. Isso significa que o novo dicionário criado (dict_2) terá uma 
cópia dos elementos de dict_1, mas ele será independente do original, com 
seu próprio espaço na memória.
-> get: obtém uma chave
-> pop: apaga um item com a chave especificada (parecido com o 'del')
-> popitem: apaga o último item adc
-> update: atualiza um dicionário com outro
"""
print("Shallow Copy:")
dict_1 = {
    'key_1': 1,
    'key_2': 2,
    'list_1': [0, 1, 2], # NÃO vai entrar nos itens da lista, vai ser 
    # Shallow Copy (cópia rasa):
    # ou seja, os dicts vão compartilhar a mesma lista na memória
    # se tiver uma lista dentro de uma lista, ele NÃO vai entrar nos itens
    # da lista interna, vai copiar a lista inteira.
}

dict_2 = dict_1.copy() 
# usando o Método '.copy()', 

dict_2['key_1'] = 1000
dict_2['list_1'][1] = 9999 # AMBOS os dicts apontam pra mesma lista, mesmo 
# colocando só o índice 1 da lista_1

print(dict_1)
print(dict_2)

print()

"""
Deep Copy:
copia a estrutura e os objetos internos, criando uma duplicata completa e 
independente do original
"""

import copy # importando o módulo copy para usar a função deepcopy

dict_2 = copy.copy(dict_1)
print("Shallow copy com uso copy.copy()", dict_2) # cópia rasa (shallow copy) do dict_1
# ou seja, os dicts vão compartilhar a mesma lista na memória

print("Deep Copy:")
dict_1 = {
    'key_1': 1,
    'key_2': 2,
    'list_1': [0, 1, 2], 
}

dict_2 = copy.deepcopy(dict_1)  

dict_2['key_1'] = 1000
dict_2['list_1'][1] = 9999 

print(dict_1)
print(dict_2)


person = {
    'nome': 'Luiz Gustavo',
    'sobrenome': 'Miranda',
}

print(len(person))  # 2
print(list(person.keys()))  # SEM CONVERSÃO: dict_keys(['nome', 'sobrenome'])
print(list(person.values()))  # SEM CONVERSÃO: 
# dict_values(['Luiz Gustavo', 'Miranda'])

print(list(person.items()))  # SEM CONVERSÃO: 
# dict_items([('nome', 'Luiz Gustavo'), ('sobrenome', 'Miranda')]) ==> TUPLAS
#                 0          1                0           1        ==> ÍNDICES
#          OU
for key, value in person.items():
    print(key, value) 
    # key:      | value:
    # nome      | Luiz Gustavo
    # sobrenome | Miranda