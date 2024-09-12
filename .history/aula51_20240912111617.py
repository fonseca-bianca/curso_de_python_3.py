"""Introdução ao desempacotamento + tuple
criando variáveis a partir de um pacote (tuple: coleção ordenada e imutável de itens) de valores
CRIAR VARIÁVEL DE RESTO:
vai servir pra armazenar os valores restantes q NÃO foram usados pra nada
como se fosse uma "gaveta" pra armazenar os valores restantes. Isto é, vai ser
'jogado' em uma outra varíavel
- usar *_ (CONVENÇÃO DEVS: asterisco + underline)
OBS.: se colocar nome depois do underline, é como se dissesse q depois aqueles valores serão usados
é como se avisasse pro programa q essa variável 'gaveta' criada existe, mas NÃO será usada
"""


# personagem1, *_ = ["Harry Potter", "Hermione", "Rony"]
# print(personagem1, _)

_, _, personagem3, *_ = ["Harry Potter", "Hermione", "Rony"] # 3 variáveis + a variável de resto '*_'
print(personagem3)


_, _, personagem3, *resto = ["Harry Potter", "Hermione", "Rony"] # 3 variáveis + a variável de resto '*_'
print(personagem3) # irá mostra


# lista_de_personagens = ["Harry Potter", "Hermione", "Rony"]
# personagem1, personagem2, personagem3 = lista_de_personagens
# print(personagem1)


"""ValueError: too many values to unpack (expected 2)
qndo há mais valores pra descompactar do q a qtd de variáveis disponíveis"""
# personagem1, personagem2 = ["Harry Potter", "Hermione", "Rony"]
# print(personagem3) 


"""ValueError: not enough values to unpack (expected 4, got 3)
qndo há valores insuficientes pra descompactar (tem mais variável do q valores)"""
# personagem1, personagem2, personagem3, personagem4= ["Harry Potter", "Hermione", "Rony"]
# print(personagem4)
