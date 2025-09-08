"""
Groupby - intertools em Python

- código gerado no Gemini AI pra colocar os nomes em ordem alfabética conforme
cada nota
"""

   
from itertools import groupby # Importa a função 'groupby' do módulo itertools

# Cria uma lista de dicionários, onde cada dicionário representa um aluno
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

def ordena(aluno): # Define uma função simples que retorna a nota de cada aluno
    return aluno['nota'] # recebe 'aluno' e retorna a nota associada a cada um

# --- Agrupando os alunos por nota ---
alunos_ordenados = sorted(alunos, key=ordena) 
# Ordena a lista de alunos com base na 'nota'. Isso é um pré-requisito 
# para o groupby funcionar
# chave é a função 'ordena' (a qual extrai as notas de cada aluno)

grupos = groupby(alunos_ordenados, key=ordena)
# Agrupa os alunos ordenados em grupos. Cada grupo é um iterador.

# --- Iterando sobre os grupos e formatando a saída ---
for nota, grupo in grupos: 
# Inicia um loop que percorre cada grupo. 'nota' é a chave de agrupamento 
# (ex: 'A'), e 'grupo' é o iterador com os alunos daquela nota.
    nomes_do_grupo = [aluno['nome'] for aluno in grupo]
    # Cria uma nova lista, extraindo apenas os nomes dos alunos que estão no 
    # grupo atual.
    
    nomes_ordenados = sorted(nomes_do_grupo)
    # Ordena a nova lista de nomes em ordem alfabética.

    nomes_formatados = ', '.join(nomes_ordenados)
    # Junta todos os nomes da lista em uma única string, separados por vírgula 
    # e espaço.

    print(f'Nota: {nota}')
    # Imprime a nota atual (ex: 'Nota: A').
    
    print(f"({nomes_formatados})")
    # Imprime os nomes dos alunos formatados, isto é, em ordem alfabética
    
    print()
    # Adiciona uma linha em branco para separar os grupos, tornando a saída 
    # mais fácil de ler.






