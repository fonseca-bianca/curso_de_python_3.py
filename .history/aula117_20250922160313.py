"""
Salvando Dados Python em JSON com módulo JSON:
- JSON:
    É uma estrutura de dados pra transportar OU salvar dados em arquivos;
    SIMILAR do Dicionários do Python;
    utilizado pra receber respostas de APIs;
    * NÃO são suportadas coisas q executam ações, ex:
        - classes, objetos, funções
"""



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