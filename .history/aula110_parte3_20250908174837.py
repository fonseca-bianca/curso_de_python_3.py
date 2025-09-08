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

def ordena(item):
    return item['nota']

alunos_ordenados = sorted(alunos, key=ordena)
grupos = groupby(alunos_ordenados, key=ordena)

for nota, grupo in grupos:
    # 1. Extrai os nomes do grupo
    nomes_do_grupo = [aluno['nome'] for aluno in grupo]
    
    # 2. Ordena os nomes em ordem alfabética
    nomes_ordenados = sorted(nomes_do_grupo)

    # 3. Formata a saída como uma string única
    nomes_formatados = ', '.join(nomes_ordenados)

    print(f'Nota: {nota}')
    print(f"({nomes_formatados})")
    print()