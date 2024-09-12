"""Tuple: lista imutável. Somente qndo NÃO se pretende alterar valores
NÃO leva colchetes
PODE colocar parênteses (forma explícita de declarar) --> ("Harry Potter", "Hermione", "Rony")
SEM parênteses (forma implícita de declarar) --> "Harry Potter", "Hermione", "Rony"
uma lista q quer usar futuramente, MAS q NÃO será alterada
lista carrega .métodos()
"""

personagens = ["Harry Potter", "Hermione", "Rony"]
personagens = tuple(personagens) # converte lista pra tupla

# personagens[1] = "Severo Snape" #TypeError: 'tuple' object does not support item assignment
# vai gerar erro, pq .append() é método exclusivo de listas (mutáveis)
# personagens.append("Severo Snape") # AttributeError: 'tuple' object has no attribute 'append'-

print(personagens)
print(personagens[0])