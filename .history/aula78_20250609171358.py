"""
Introdução ao tipo Set em Python - Conjuntos sets.
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo conjunto de Venn.

Parecem dict MAS NÃO tem par de {key: value}, eles têm somente {valor}
ex.:
    s1 = set() # iterável. Esse é um set vazio
    OU
    s1 = set{} --> isso aq é um DICIONÁRIO
    s1 = {1, 2, 3} --> isso é um set 
    print(s1)

Sets em Python são MUTÁVEIS, PORÉM, aceitam apenas Tipos Imutáveis como valor 
interno.
No entanto, os elementos individuais que compõem um set precisam ser IMUTÁVEIS. 
Isso significa que em um set NÃO podem ser adc tipos Mutáveis, como listas ou 
outros sets, como se fossem elementos dentro de um set.


Criando um set:
conjunto_1 = set([1, 2, 3]) --> forma mais versátil de criar um conjunto, 
pois podemos passar qualquer iterável (lista, tupla, string, etc.) para set() 
e ele converterá para um conjunto.

OU

conjunto_2 = {1,2,3} -->  SÓ tem valor. Formato é útil para conjuntos pequenos 
ou com valores fixos
OBS.1: criar {} chave vazia é Dicionário e NÃO set
       cria set vazio => set(): cria uma função set 
OBS.2: se um conjunto de valores aparece entre chaves e NÃO há pares chave: 
valor, o Python interpreta isso como um set.

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
    # Output: [1, 2, 3] --> como era tipo set, foram removidos os valores 
    # repetidos
    e a lista passou a ter somente valores NÃO repetidos
    
    - Facilita pra NÃO necessitar fazer um loop for só pra remover itens 
    repetidos 

EX.:
    s1 = {1, 2, 3}
        print(3 not in s1)
        for numero in s1:
            print(numero)

Métodos úteis:
EX.: s1 = set()
- .add():
    só aceita 1 argumento por vez
    s1.add("Luiz")
- .update():
    s1.update(("Olá mundo", 1, 2, 3)) --> Output: {3, 1, 'olá mundo', 2}
        * resultado está embaralhado pq o set NÃO mantém a ordem e NÃO aceitam
        duplicatas
- .clear():
    s1.clear()
- .discard(): 
    eliminar o próprio valor, já q NÃO há index no set
    s1.discard("olá mundo")


Operadores úteis:
- união | união (union) => une (|: pipeline)
- interseção: & (intersection) => itens presentes em ambos
- diferença (-): => itens presentes APENAS no set da esquerda
- diferença simétrica: ^ => itens q NÃO estão em ambos os SETS.
    OBS.: Diferença simétrica retorna um NOVO SET (conjunto) contendo apenas
    os itens EXCLUSIVOS de cada SET, NÃO retorna valores repetidos em ambos 
    os SETS
"""
# union | :
print("Union | :")
set_1 = {"A", "B", "C"}
set_2 = {"C", "B", "D"}
set_3 = set_1 | set_2
print(set_3) 
# vai unis, MAS NÃO repetirá os itens duplicados, no caso o 'B' e o 'C'

print()
print("Interseção &:")
# interseção & :
set_4 = {"A", "B", "C"}
set_5 = {"C", "B", "D"}
set_6 = set_4 & set_5
print(set_6) 
# irá mostrar os itens q se repetem em AMBOS, no caso o 'B' e o 'C'

print()
print("Diferença - :")
# diferença - :
set_7 = {"A", "B", "F"}
set_8 = {"C", "D", "E", "A"}
set_9 = set_7 - set_8
set_10 = set_8 - set_7
print(set_9) 
# irá mostrar os itens q NÃO se repetem em AMBOS os sets
# NÃO vai mostrar o 'A' pq ele está em AMBOS os sets
print(set_10) 

print()
print("Diferença simétrica ^ :")
# Diferença simétrica ^ :
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
set_difference_symmetric = set_A ^ set_B
print(set_difference_symmetric) 
# output: {1, 2, 5, 6}
# mostra apenas os itens q NÃO estão em AMBOS os sets
# NÃO vai mostrar: 3, 4