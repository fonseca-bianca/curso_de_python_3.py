"""
Dicionários em Python (tipo dict): 
São estruturas de dados do tipo PAR "chave - key" e "valor - value"
-> Keys: 
podem ser consideradas como índice e podem ser de tipos IMUTÁVEIS como:
int, str, float, bool, tuple (elementos Tupla tbm devem ser Imutáveis).
-> Values:
podem ser de qlqr tipo, podendo ser tbm OUTRO dicionário.
-> Dicionário:
{} ou classe dict:
usados pra criar os dicionários.
IMUTÁVEIS: int, str, float, bool, tuple
OU
MUTÁVEIS: list, dict
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Av. Paulista', 'numero': 123},
        {'rua': 'Av. Rio Branco', 'numero': 456}
    ]
}

print(pessoa, type(pessoa))