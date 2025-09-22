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
    'nome': 'Luiz Otávio DE ALCÂNTARA',
    'sobrenome': 'Miranda',
    'endereços': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
    # 'seeeeet': {1, 2, 3} # NÃO é suportado pelo JSON  
        # TypeError: Object of type set is not JSON serializable
        # ele não é uma coleção ordenada e seus itens não têm uma ordem fixa 
        # O formato JSON exige q os dados de listas (arrays) mantenham a ordem
}

# salvando o arq:
#.dump(): fazer o dump num arq. Recebe como parâmetros Objeto e Arq
with open('aula117_parte1.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa, 
        arquivo, 
        indent=2, 
        ensure_ascii=False
    ) 
    
# os.remove('aula117.json')  # remove o arq criado
# indent=2: formata o dict com 2 espaços
# ensure_ascii=False: aceita caracteres especiais (acentos, ç, ã...)