"""
Dicionários em Python (tipo dict): 
São estruturas de dados do tipo PAR "chave - key" e "valor - value"
-> Keys: 
podem ser consideradas como índice e podem ser de tipos IMUTÁVEIS como:
int, str, float, bool, tuple (elementos Tupla tbm devem ser Imutáveis).
-> Values:
podem ser de qlqr tipo, podendo ser tbm OUTRO dicionário.
-> Dicionário:
{} ou 
classe dict (ex.: pessoa = dict(nome='Luiz', sobrenome='Miranda') --> args nomeados):
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
    ],
    # em 'endereços' usamos uma lista e dentro dela +2 dicionários cada um com 'rua'...
}

print(pessoa, type(pessoa))

# acessar um valor específico, como se fosse um índice de uma lista
print(pessoa['idade'])