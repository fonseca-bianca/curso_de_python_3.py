"""
Ainda sobre Closure, a variável poderá apontar pra um objeto:
    Mutável
    OU
    Imutável
Variáveis livres + nonlocal (locals, globals):
- nonlocal:
    aponta pra um objeto Imutável
    indica q podemos reutilizar a variável de escopo NÃO local
"""

print("Variável aponta pra objeto Imutável:")
def make_counter():
    count = 0 # é o valor inteiro Imutável
    def counter():
        nonlocal count 
        count += 1
        return count
    return counter


counter = make_counter()
print(counter())
print(counter())
print(counter())


print("Variável aponta pra objeto Mutável:")