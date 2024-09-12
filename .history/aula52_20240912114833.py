"""Tuple: lista imutável. NÃO leva colchetes
uma lista q quer usar futuramente, MAS q NÃO será alterada
lista carrega .métodos()
"""

personagens = ["Harry Potter", "Hermione", "Rony"]
_, _, personagem3, *resto = personagens.append("Severo Snape")
print(personagem3)