"""
Métodos úteis dos dict em Python:
-> len: quantas chaves
-> keys: iterável com chaves
-> values: iterável com valores
-> items: iterável com chaves E valores
-> setdefault: adc valor SE a chave NÃO existe
-> copy: retorna cópia rasa (shallow copy)
-> get: obtém uma chave
-> pop: apaga um item com a chave especificada (del)
-> popitem: apaga o último item adc
-> update: atualiza um dicionário com outro
"""

dict_1 = {
    'key_1': 1,
    'key_2': 2,
}

dict_2 = dict_1.copy()

dict_2['key_1'] = 1000
print(dict_1)
print(dict_2)