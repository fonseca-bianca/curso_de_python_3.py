"""
Groupby - intertools em Python
"""

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# A chave 'nota' é usada para agrupar os alunos
def ordena_por_nota(aluno):
    return aluno['nota']

# A chave 'nome' é usada para ordenar os alunos por nome
def ordena_por_nome(aluno):
    return aluno['nome']

# 1. Primeiro, agrupamos os alunos por nota. O groupby exige que a 
# lista esteja previamente ordenada.
alunos_ordenados_por_nota = sorted(alunos, key=ordena_por_nota)
grupos = groupby(alunos_ordenados_por_nota, key=ordena_por_nota)

# 2. Agora, iteramos sobre os grupos
for nota, grupo in grupos:
    print(f'Nota: {nota}')

    # 3. Para cada grupo, ordenamos os alunos por nome antes de imprimi-los
    alunos_do_grupo_ordenados = sorted(list(grupo), key=ordena_por_nome)

    for aluno in alunos_do_grupo_ordenados:
        print(f'  {aluno,["nome"]}')
    print()
