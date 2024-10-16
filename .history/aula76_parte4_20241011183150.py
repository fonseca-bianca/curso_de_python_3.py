"""
Ainda sobre métodos úteis em Python:
"""

person_1 = {
    "first_name": "Lucke",
    "last_name": "Skywalker"
}

print("Get:")
print(person_1.get("first_name")) 
# O método get retorna o valor associado à chave "first_name" se ela existir. 
# Caso a chave não exista, retorna None (ou um valor padrão se especificado).

print(person_1["first_name"])
# Acessa o valor diretamente pela chave. Se a chave não existir, lança um 
# erro KeyError.


print()
print("Pop:")
name = person_1.pop("first_name")
print(name)
print(person_1)
