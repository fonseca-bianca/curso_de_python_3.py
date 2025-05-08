""" Tuple: 
- lista imutável. Somente qndo NÃO se pretende alterar valores
- NÃO leva colchetes
- PODE colocar parênteses (forma explícita de declarar) 
--> ("Harry Potter", "Hermione", "Rony")
- SEM parênteses (forma implícita de declarar)
--> "Harry Potter", "Hermione", "Rony"
- uma lista q quer usar futuramente, MAS q NÃO será alterada
- OBS.:
    Tupla:
        NÃO carrega .metodos() de lista:
            Não possui métodos de modificação como:
                append(), remove() ou sort()
        carrega seus próprios .metodos() como:
            .count() 
            .index()
            ex.:
                tupla = (1, 2, 3, 2)
                print(tupla.count(2))  # 2
                print(tupla.index(3))  # 2
"""

personagens = ["Harry Potter", "Hermione", "Rony"]
personagens = tuple(personagens) # converte lista pra tupla

# Formas válidas de escrever uma Tupla:
# personagens = ("Harry Potter", "Hermione", "Rony")
# OU
# personagens = "Harry Potter", "Hermione", "Rony"

# personagens[1] = "Severo Snape" # TypeError: 'tuple' object does not...
# vai gerar erro, pq .append() é método exclusivo de listas (mutáveis)
# personagens.append("Severo Snape") # AttributeError: 'tuple' object has...

print(personagens)
print(personagens[0])