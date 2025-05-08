"""Introdução ao desempacotamento:
- pra iteráveis;
- ideal pra quando se tem MUITOS valores, mas só queremos
- criando variáveis a partir de um pacote (tuple: coleção ordenada e imutável 
de itens) de valores

CRIAR VARIÁVEL DE *RESTO:
- vai servir pra armazenar os valores restantes q NÃO foram usados pra nada
- como se fosse uma "gaveta" pra armazenar os valores restantes. Isto é, 
vai ser "jogado" em uma outra varíavel
- usar *_ (CONVENÇÃO DEVS Python: asterisco + underline):
    OBS.: 
        *resto → armazena e permite usar
                Captura todos os itens restantes como lista
            ex.: _, _,personagem3, *resto = ["Harry Potter", "Hermione", 
            "Rony"] 
                 print(personagem3, resto) # output: Rony []
            OU
        *_ → ignora o valor (NÃO vai usar)
            Captura todos os itens restantes, mas “ignora” por convenção
            ex.: _, _, personagem3, *_ = ["Harry Potter", "Hermione", "Rony"]
                 print(personagem) 
            OU
        _ → Apenas uma variável comum que, por convenção, é ignorada
"""

# personagem1, *_ = ["Harry Potter", "Hermione", "Rony"]
# print(personagem1, _)

_, personagem2, personagem3, *_ = ["Harry Potter", "Hermione", "Rony"] 
# 3 variáveis + a variável resto *_ (esta armazena uma lista vazia)
# _, _, : ignora os dois primeiros itens
print(personagem3, *_) # NÃO vai mostrar lista vazia

# a variável que armazena o “resto” se chama *_, e o underline (_) é uma 
# convenção usada em Python para indicar que não vamos usar aquele valor. 
# Então, mesmo que ele contenha a lista vazia, o Python entende que você 
# não quer usá-la, por isso não aparece nada no print
# *_ → ignora o valor

print(20*"-")

print(personagem2, _) # vai usar o valor. Output: Herminione ['Rony']

print(20*"-")

_, _, personagem3, *resto = ["Harry Potter", "Hermione", "Rony"] 
# 3 variáveis + a variável de resto '*_'
print(personagem3, resto) 
# irá mostrar a var *resto q é uma lista vazia 
# personagem3 = 'Rony', resto = []
# nome útil à variável (*resto), então o conteúdo (mesmo que vazio) fica 
# acessível e visível no print().
# *resto → armazena e permite usar


# lista_de_personagens = ["Harry Potter", "Hermione", "Rony"]
# personagem1, personagem2, personagem3 = lista_de_personagens
# print(personagem1)


""" ValueError: too many values to unpack (expected 2):
qndo há mais valores pra descompactar do q a qtd de variáveis disponíveis
"""
# personagem1, personagem2 = ["Harry Potter", "Hermione", "Rony"]
# print(personagem3) 


""" ValueError: not enough values to unpack (expected 4, got 3):
qndo há valores insuficientes pra descompactar (tem mais variável do 
q valores)
"""
# personagem1, personagem2, personagem3, personagem4= ["Harry Potter", 
# "Hermione", "Rony"]
# print(personagem4)
