"""
Ainda sobre métodos úteis em Python:
"""

person_1 = {
    "first_name": "Lucke",
    "middle_name": "Vader's son",
    "last_name": "Skywalker",
}

print("Update:")
person_1.update({
    "name": "Leia",
    "middle_name": "Organa", 
})
print(person_1)
# atualiza o dict 

print()
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
# apaga o item q tiver a chave especificada, no caso, é "first_name"


print()
print("Popitem:")
name = person_1.popitem()
print(name)
print(person_1)
# NÃO passar chave como Argumento.
# ele vai retornar a última chave



