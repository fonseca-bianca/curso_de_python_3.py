"""
'yield from' em Generator functions:
    Retorna dados de outro Generator ou Iterable (normalmente anterior a ele)
"""

def gen_1():
    yield 1
    yield 2
    yield 3
    
def gen_2():
    yield from gen_1()
    yield 4
    yield 5
    yield 6
    
gen = gen_2()
for numero in gen:
    print(numero, end="")
    
# output:
# 1
# 2
# 3
# 4
# 5
# 6