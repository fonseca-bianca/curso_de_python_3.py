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
    count = 0 # é objeto Imutável com valor 0
    def counter():
        nonlocal count # nonlocal (funcao interna) acessa count e modifica 
#        o valor da var
        count += 1 
        return count # nonlocal aponta pra var 'count' q está no escopo 
#    externo, no caso, ela é uma variável livre. 
    return counter


counter = make_counter()
print(counter())
print(counter())
print(counter())


print("Variável aponta pra objeto Mutável:")
def make_appender():
    items = []
    def appender(new_item):
        items.append(new_item) # adc novos itens à lista vazia 'items'
        return items
    return appender

appender = make_appender() # função interna = recebe o valor da função externa
print(appender("Item 1"))
print(appender("Item 2"))
print(appender("Item 3"))
        
