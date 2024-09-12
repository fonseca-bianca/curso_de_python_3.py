"""Introdução ao desempacotamento + tuple
criando variáveis a partir de um pacote (tuple: coleção ordenada e imutável de itens) de valores"""


# lista_de_personagens = ["Harry Potter", "Hermione", "Rony"]
# personagem1, personagem2, personagem3 = lista_de_personagens
# print(personagem1)


"""ValueError: too many values to unpack (expected 2)
qndo há mais valores pra descompactar do q a qtd de variáveis disponíveis"""
# personagem1, personagem2 = ["Harry Potter", "Hermione", "Rony"]
# print(personagem3) 


"""ValueError: not enough values to unpack (expected 4, got 3)
qndo há valores insuficientes pra descompactar"""
personagem1, personagem2, personagem3, personagem4= ["Harry Potter", "Hermione", "Rony"]
print(personagem4)
