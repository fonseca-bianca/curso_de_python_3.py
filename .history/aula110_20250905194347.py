"""
Groupby - intertools em Python

PROBLEMA GERADO:
Com o cód com problema, o retorno NÃO são 2 grupos (IT e ADMIN), mas sim 5:
IT [('Vera', 'IT'), ('Chuck', 'IT')] --> grupo 1
ADMIN [('Dave', 'ADMIN')]            --> grupo 2
IT [('Karl', 'IT')]                  --> grupo 3
ADMIN [('Janet', 'ADMIN')]           --> grupo 4
IT [('Jack', 'IT')]                  --> grupo 5

Pq aconteceu isso?
    Com base na doc PEP-8, a operação 'groupby()' gera uma pausa (break) ou um
    NOVO grupo TODA vez q o valor da função chave muda). Por isso, ele agrupa
    os dois primeiros nomes da lista em IT e depois CRIA um segundo grupo pro
    ADMIN, MAS, ao invés de adicionar o próximo da lista a um dos DOIS GRUPOS
    já criados, ele cria um NOVO grupo pra cada próximo elemento da lista que
    vier (ser for mais 99 elementos, ele vai criar mais 99 listas pra cada um)


COMO RESOLVER O PROBLEMA?
1. Classificar os dados:
    1.a. in the case down, we need to group the employees by department
    importar a biblioteca itertools
    podemos usar a função sorted() aq
2. usar o grupo criado de employees como parâmetro da função groupby

** OBS.: caso NÃO queira fazer a classificação e o agrupamento dos dados em
2 etapas (acima), pode usar:

- dict {} como alternativa
(excluir o código abaixo usado e usar este aqui:)
1. criar um dict vazio
2. adc nomes dos funcionários aos departamentos existentes
3. fazer um 'if'
4. se a chave do departamento ainda não existir, criar uma NOVA lista (dentro
do if, pode usar um else)

import itertools 

employees = [
    ("Vera", "IT"),
    ("Chuck", "IT"),
    ("Dave", "ADMIN"),
    ("Karl", "IT"),
    ("Janet", "ADMIN"),
    ("Jack", "IT")
]

# IT: Chuck, Dave, Karl, Jack
# ADMIN: Vera, Janet


grouped_by_department = {}
for bname, department in employees:
    if department not in grouped_by_department:
        grouped_by_department[department].append()
    else:
        grouped_by_department[department] = [name]
for department, names in grouped_by_department.items():
    print(department, names)

"""
# COM erro no output:

# import itertools 

# employees = [
#     ("Vera", "IT"),
#     ("Chuck", "IT"),
#     ("Dave", "ADMIN"),
#     ("Karl", "IT"),
#     ("Janet", "ADMIN"),
#     ("Jack", "IT")
# ]

# # IT: Chuck, Dave, Karl, Jack
# # ADMIN: Vera, Janet


# grouped_by_department = itertools.groupby(employees, lambda x: x[1])
# for i, j in grouped_by_department:
#     print(i, list(j))
    

# SEM erro no output:

# import itertools 

# employees = [
#     ("Vera", "IT"),
#     ("Chuck", "IT"),
#     ("Dave", "ADMIN"),
#     ("Karl", "IT"),
#     ("Janet", "ADMIN"),
#     ("Jack", "IT")
# ]

# # IT: Chuck, Dave, Karl, Jack
# # ADMIN: Vera, Janet


# grouped_by_department = itertools.groupby(employees, lambda x: x[1])
# for i, j in grouped_by_department:
#     print(i, list(j))
    

import itertools 

employees = [
    ("Vera", "IT"),
    ("Chuck", "IT"),
    ("Dave", "ADMIN"),
    ("Karl", "IT"),
    ("Janet", "ADMIN"),
    ("Jack", "IT")
]

# IT: Chuck, Dave, Karl, Jack
# ADMIN: Vera, Janet


grouped_by_department = {}
for name, department in employees:
    if department in grouped_by_department:
        grouped_by_department[department].append()
    else:
        grouped_by_department[department] = [name]
for department, names in grouped_by_department.items():
    print(department, names)