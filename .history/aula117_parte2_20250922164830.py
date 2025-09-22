# abrindo o arq JSON:
import json

with open('aula117_parte1.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
    # Luiz Otávio DE ALCÂNTARA
    # ou seja, ele leu o arq JSON q é externo a ele e exibiu o resultado na
    # tela
    print(type(pessoa))  # o tipo é dict