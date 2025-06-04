"""
Ainda sobre métodos úteis em Python:
"""

person_1 = {
    "first_name": "Luke",
    "middle_name": "Vader's son",
    "last_name": "Skywalker",
}


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
print(person_1) # 'first_name' já NÃO estará mais dentro da chave 'name'
# apaga o item q tiver a chave especificada, no caso, é "first_name"


print()
print("Popitem:")
name = person_1.popitem()
print(name)
print(person_1)
# NÃO passar chave como Argumento.
# remove a última chave do dict

print()
print("Update:")
person_1.update({
    "first_name": "Leia",
    "last_name": "Organa", 
})
print(person_1)
# atualiza o dict com os valores especificados
# se NÃO especificar nada, ele não fará nada
# pode atualizar um valor ou criar uma nova chave
# se a chave já existir, o valor será atualizado
# Update: mexe no próprio dict

print()
print("Update: (2ª forma de escrevê-lo)")
person_1.update(name="R2D2", age=30) # argumentos nomeados
print(person_1)

print()
print("Update: (3ª forma de escrevê-lo usando Tupla)")
tuple_registration_data = ('name', 'novo_valor'),
person_1.update(tuple_registration_data)
print(person_1)
# Output:
# {'first_name': 'Luke', 'middle_name': "Vader's son", 'last_name': 'Skywalker', 'name': 'profession'}

print()
print("Update: (3ª forma de escrevê-lo usando Lista -> iterável que se comporta como um dicionário)")
list_registration_data = ['name', 'profession'],
person_1.update(list_registration_data)
print(person_1)
# Output:
# {'first_name': 'Luke', 'middle_name': "Vader's son", 'last_name': 'Skywalker', 'name': 'profession'}