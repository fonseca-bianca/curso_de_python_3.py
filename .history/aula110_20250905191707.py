"""
Groupby - intertools em Python

PROBLEMA GERADO:

COMO RESOLVER O PROBLEMA?
1. Classificar os dados:
    1.a. in the case down, we need to group the employees by department
    importar a biblioteca itertools
    podemos usar a função sorted() aq
2. 





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


grouped_by_department = itertools.groupby(employees, lambda x: x[1])
for i, j in grouped_by_department:
    print(i, list(j))