lista_nomes = [
    {'nome': 'Luiz', 'sobrenome': 'miranda', 'idade': 30},
    {'nome': 'Maria', 'sobrenome': 'Oliveira', 'idade': 25},
    {'nome': 'Daniel', 'sobrenome': 'Silva', 'idade': 28},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira', 'idade': 35},
    {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 64},
]

def exibir(lista_nomes):
    for item in lista_nomes:
        print(item)

print('Lista ordenada por nome:')        
lista_nomes1 = sorted(lista_nomes, key=lambda item: item['sobrenome'])

print()

print('Lista ordenada por idade:')
lista_nomes2 = sorted(lista_nomes, key=lambda item: item['idade'])

# exibindo as listas sem usar 'print()', mas usando a própria função 'exibir()'
exibir(lista_nomes1)
exibir(lista_nomes2)