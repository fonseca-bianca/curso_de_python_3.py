"""
Variáveis livres + nonlocal (locals, globals):

"""

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


counter = make_counter()

counter()
1
counter()
2
counter()
3