"""
O 'for' por 'baixo dos panos'
* iterável: str, range, etc . Método dentro do iterável em Python: .__iter__
* iterador: sabe entregar um valor por vez
* next: me entregue o próximo valor
* iter: me entrege o seu iterador
"""

nome = "Luiz"
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
