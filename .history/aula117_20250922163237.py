"""
Salvando Dados Python em JSON com módulo JSON:
- JSON:
    É uma estrutura de dados pra transportar OU salvar dados em arquivos;
    SIMILAR do Dicionários do Python;
    utilizado pra receber respostas de APIs;
    * NÃO são suportadas coisas q executam ações, ex:
        - classes, métodos, funções, set
    todos os números são Number (sem distinção de tipo);
    
"""

import json # importa o módulo json
import os # importa o módulo os

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'endereços': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# salvando o arq:
#.dump(): fazer o dump num arq. Recebe como parâmetros Objeto e Arq
with open('aula117.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa, 
        arquivo, 
        indent=2, 
        ensure_ascii=False
    ) 
# indent=2: formata o dict com 2 espaços
# ensure_ascii=False: aceita caracteres especiais (acentos, ç, ã...)