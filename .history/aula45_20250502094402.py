"""
O 'for' por 'baixo dos panos'
* iterável: str, range, etc . Método dentro do iterável em Python: 
.__iter__() --> 
retorna um 'iterador' (q é OUTRO Objeto q vai saber entregar um elemento 
por vez da string)
.__iter__() --> pode usar iter() q é mais fácil
* iterador: sabe entregar um valor por vez
* next (chamar dentro do 'iterator'): me entregue o próximo valor
* iter: me entrege o seu Objeto iterador (é outro Objeto, não é a string)
*** quando esgotam os valores das iterações, um erro é levantado 
"StopIteration"
"""

"""
nome = iter("Luiz") # nome = "Luiz".__iter__()
print(next(nome)) # nome.__next__()
"""

nome = "Luiz" # iterável: percorrer os elementos, no caso, caracteres da 
#string 'Luiz'
# iterador = iter(nome) # iterator: criado a partir do iterável. É um obj q 
# sabe COMO percorrer elementos do iterável

# while True:
#     try:
#         letra = next(iterador) #next: obter próximo elemento do iterador. 
# Elemento obtido é armazenado na variável 'letra'
#         print(letra)
#     except StopIteration: #quando iterador esgota todos elementos do 
# iterável, a função next lança a exceção
#         break #interrompe o loop

# mesmo q o de cima com 'while' só q mais simplificado
for letra in nome:
    print(letra)