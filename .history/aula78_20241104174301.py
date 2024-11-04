"""
Introdução ao tipo Set em Python - Conjuntos sets.
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo conjunto de Venn.
Sets em Python são mutáveis, isto é, NÃO aceitam TIPOS MUTÁVEIS como valor interno.
No entanto, os elementos individuais que compõem um set precisam ser IMUTÁVEIS. 
Isso significa que em um set NÃO podem ser adc tipos Mutáveis, como listas ou outros sets, 
como se fossem elementos dentro de um set.


Criando um set:
conjunto_1 = set([1, 2, 3]) --> forma mais versátil de criar um conjunto, 
pois podemos passar qualquer iterável (lista, tupla, string, etc.) para set() 
e ele converterá para um conjunto.

OU

conjunto_2 = {1,2,3} -->  SÓ tem valor. Formato é útil para conjuntos pequenos 
ou com valores fixos
OBS.1: criar {} chave vazia é Dicionário e NÃO set
OBS.2: se um conjunto de valores aparece entre chaves e NÃO há pares chave: valor, 
o Python interpreta isso como um set.

Sets:
- NÃO têm index;
- NÃO garantem ordem;
- SÃO iteráveis (for, in, not, not in)
- Seus valores serão sempre ÚNICOS
- ELIMINAM valores duplicados de iteráveis
EX.:
    l1 = [1, 2, 3, 3, 3, 3, 3, 1]
    s1 = set(l1) --> transforma a lista no tipo set
    l2 = list(s1) --> pega o set1 e o transforma em uma lista nova (l2)
    print(l2)
    # Output: [1, 2, 3] --> como era tipo set, foram removidos os valores repetidos
    e a lista passou a ter somente valores NÃO repetidos
    
    - Facilita pra NÃO necessitar fazer um loop for só pra remover itens repetidos 

EX.:
    s1 = {1, 2, 3}
        print(3 not in s1)
        for numero in s1:
            print(numero)

Métodos úteis:
- add;
- update;
- clear;
- discard;
"""