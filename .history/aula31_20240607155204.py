"""
IDENTIDADE DO VALOR Q ESTÁ NA MEMÓRIA:
Se colocarmos o MESMO valor em variáveis diferentes, o Python vai interpretar como
valores literais e, portanto, iguais, logo, ambas as variáveis diferentes terão 
o MESMO endereço na Memória
"""

v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))