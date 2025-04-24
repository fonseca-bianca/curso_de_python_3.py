"""
IDENTIDADE DO VALOR Q ESTÁ NA MEMÓRIA:
Se colocarmos o MESMO valor em variáveis diferentes, o Python vai interpretar 
como valores literais e, portanto, iguais, logo, ambas as variáveis diferentes
terão o MESMO endereço na Memória
"""
"""
v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça nada")
    
if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")