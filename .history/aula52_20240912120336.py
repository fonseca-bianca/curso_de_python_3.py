"""Tuple: lista imutável. NÃO leva colchetes
uma lista q quer usar futuramente, MAS q NÃO será alterada
lista carrega .métodos()
"""

personagens = "Harry Potter", "Hermione", "Rony"

# vai gerar erro, pq .append() é método exclusivo de listas (mutáveis)
# personagens.append("Severo Snape") 

print(personagens)