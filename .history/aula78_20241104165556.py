"""
Introdução ao tipo Set em Python - Conjuntos sets.
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo conjunto de Venn.
Sets em Python são mutáveis, isto é, NÃO aceitam TIPOS MUTÁVEIS como valor interno.
No entanto, os elementos individuais que compõem um set precisam ser IMUTÁVEIS. 
Isso significa que em um set NÃO podem ser adc tipos Mutáveis, como listas ou outros sets, como elementos dentro de um set.

Criando um set:
conjunto_1 = set([1, 2, 3]) --> forma mais versátil de criar um conjunto, 
pois podemos passar qualquer iterável (lista, tupla, string, etc.) para set() 
e ele converterá para um conjunto.

OU

conjunto_2 = {1,2,3} -->  SÓ tem valor. Formato é útil para conjuntos pequenos 
ou com valores fixos
OBS.: criar {} chave vazia é Dicionário e NÃO set

São eficientes pra REMOVER valores duplicados de iteráveis.
Sets:
- NÃO têm index;
- NÃO garantem ordem;
- SÃO iteráveis (for, in, not, not in)

Métodos úteis:
- add;
- update;
- clear;
- discard;
"""