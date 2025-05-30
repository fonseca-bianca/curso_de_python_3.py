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
classe dict (ex.: pessoa = dict(nome='Luiz', sobrenome='Miranda') 
--> args nomeados): usados pra criar os dicionários.
IMUTÁVEIS: int, str, float, bool, tuple
OU
MUTÁVEIS: list, dict

ex.: 
meu_dicionario = {
    "nome": "Bianca",
    "idade": 30,
    "profissao": "Dev Python"
}

    * chaves: "nome", "idade", "profissao"
        são únicas e imutáveis, não podem ser repetidas.
        cada uma tem um valor associado.
        pares key:value separados por vírgula.
    * valores: "Bianca", 30, "Dev Python"
    
    * acessando valores:
    print(meu_dicionario['nome'])  # Saída: Bianca
    
    * adicionando novo valor:
    meu_dicionario['cidade'] = 'Vancouver'
        ficaria:
            meu_dicionario = {
                "nome": "Bianca",
                "idade": 30,
                "profissao": "Dev Python",
                "cidade": "Vancouver"
            }
"""

# Dicionário:
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Av. Paulista', 'numero': 123},
        {'rua': 'Av. Rio Branco', 'numero': 456}
    ],
    # em 'endereços' usamos uma lista e dentro dela +2 dicionários cada um com
    # 'rua'...
}

print(pessoa, type(pessoa))

# acessar uma chave específica e seu respectivo valor, como se fosse um índice 
# de uma lista
print(pessoa['idade'])

print()

# pessoa = dict(nome='Luiz', sobrenome='Miranda')
# print(pessoa, type(pessoa)) 
# output: {'nome': 'Luiz', 'sobrenome': 'Miranda'} <class 'dict'>

for chave in pessoa:
    print(chave)