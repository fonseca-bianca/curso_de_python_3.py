# abrindo o arq JSON:
import json

with open('aula117_parte1.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))  # o tipo é dict